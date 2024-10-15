from django.test import TestCase
from pybo.models import Question
from django.utils import timezone
# Create your tests here.

for i in range(300):
    q = Question(subject="데스트 데이터입니다:[%03d]" % i , content="내용 무" , create_date=timezone.now())
    q.save()

    