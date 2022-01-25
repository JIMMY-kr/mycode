from django.db import models
from  datetime import datetime

class Memo(models.Model):
    idx = models.AutoField(primary_key=True) #일련번호
    writer = models.TextField(null=False)
    memo=models.TextField(null=False)
    #현재시각이 기본값으로 입력
    post_date = models.DateTimeField(default=datetime.now, blank=True)