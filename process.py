import os
# Unix/Linux 操作系统提供了一个 fork() 系统调用，
# 它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
#
# 子进程永远返回 0，而父进程返回子进程的 ID。
# 这样做的理由是，一个父进程可以 fork 出很多子进程，所以，父进程要记下每个子进程的 ID，而子进程只需要调用 getppid() 就可以拿到父进程的 ID。
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    # 子进程返回的内容
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    # 父进程返回的内容
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))