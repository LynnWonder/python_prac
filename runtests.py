#!/usr/bin/env python3
import argparse
import subprocess
import sys
from typing import AnyStr, List, Optional

import pytest


def exit_on_failure(ret):
    if ret:
        sys.exit(ret)


def perform_test(args: Optional[List[AnyStr]] = None):
    print('Running unit test...')
    return pytest.main(args or [])


def perform_flake8(args: Optional[List[AnyStr]] = None):
    print('Running flake8 code linting...')
    r = subprocess.call(['flake8'] + (args or []))
    print('flake8 failed' if r else 'flake8 passed')
    return r


def perform_isort(args: Optional[List[AnyStr]] = None):
    print('Running isort code checking...')
    r = subprocess.call(['isort', '--check-only', '--diff'] + (args or ['.']))
    if r:
        print('isort failed: Some modules have incorrectly ordered imports. Fix by running `isort .`')
    else:
        print('isort passed')
    return r


def perform_gitlint():
    print('Running git linting...')
    r = subprocess.call(['gitlint'])
    print('gitlint failed' if r else 'gitlint passed')
    return r


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run test suite')
    parser.add_argument(
        '--nolint', action='store_true',
        help='no lint, just run unit test.',
    )
    parser.add_argument(
        '--onlylint', action='store_true',
        help='only lint, do not run unit test.',
    )

    options, extras = parser.parse_known_args()

    if options.nolint and options.onlylint:
        print('Aborting: --nolint and --onlylint are conflict.')
        sys.exit(1)

    run_test = False if options.onlylint else True
    run_lint = False if options.nolint else True

    if run_lint:
        exit_on_failure(perform_flake8())
        exit_on_failure(perform_isort())

    if run_test:
        exit_on_failure(perform_test(extras))

    exit_on_failure(perform_gitlint())
