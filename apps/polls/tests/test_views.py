# 简单写一个和用户无关的视图测试
# 更多的内容可以参考 https://docs.djangoproject.com/zh-hans/4.0/intro/tutorial05/#test-a-view
import pytest
from django.test import Client
from django.urls import reverse
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestViews:

    def test_polls_detail(self):
        client = Client()
        mixer.blend('polls.Question')
        path = reverse('polls:detail', kwargs={'pk': 1})
        response = client.get(path)
        assert response.status_code == 200
