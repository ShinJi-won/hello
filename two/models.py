from django.db import models

class Food(models.Model):
    name=models.CharField(max_length=30)
    adr=models.CharField(max_length=100)
    pw=models.CharField(max_length=10,default=None,null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성시각
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    score=models.IntegerField()
    comment=models.CharField(max_length=50)

    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성시각
    updated_at = models.DateTimeField(auto_now=True)