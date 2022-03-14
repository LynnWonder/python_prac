from mixer.backend.django import mixer
from django.utils import timezone
import pytest


# 我们使用 mixer 生成测试用的 model instance
# 根据 orm 模型的特点，那么这里就是生成一条数据
@pytest.mark.django_db
class TestModels:

    def test_question_has_choice(self):
        # tip 使用 datetime.now() 返回的是 naive datetime
        #  而由于默认使用 USE_TZ 为 true 即网站内存储和使用的是 UTC 时间
        question = mixer.blend('polls.Question', question_text="for test", pub_date=timezone.now())
        assert question.__str__() == 'for test'
