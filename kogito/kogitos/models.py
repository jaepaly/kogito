from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )
    introduction = models.TextField(null=False, max_length=300)
    profile_image = models.ImageField(upload_to='uploads/%Y/%m/%d/')    #이미지필드= 이미지 검증 로직, 업로드 투= 파일이 업로드될 때 프로젝트 폴더 내의 어디에 저장할지 경로 지정
    nickname = models.CharField(null=False, max_length=10)
    job = models.CharField(null=False, max_length=100)