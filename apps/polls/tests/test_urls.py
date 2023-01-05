from django.urls import resolve, reverse


class TestUrls:

    # 测试 url
    def test_detail_url(self):
        # 获取 name 是 detail 的 url
        path = reverse('polls:detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'polls:detail'
