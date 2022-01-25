from django.db import models

# class 클래스이름(상위클래스)
class Address(models.Model):
    #필드명 = 자료형
    idx=models.AutoField(primary_key=True) #자동증가 일련번호
    name=models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)