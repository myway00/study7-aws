from django.db import models

# Create your models here.

class blog(models.Model) : #model을 상속받는다는 거
    title=models.CharField(max_length=200) #Charfield는 제한이 있는 문자열
    writer = models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:30] #파이썬 슬래쉬 기능으로 100자까지 잘라주기