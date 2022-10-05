from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user 리턴이 문자열 get_user_model()은 객체를 줌 장고가 내부적으로 실행할때 유저 객체보다 models.py 가 먼저 실행된다
    # get_user_model은 생성이 안된다. (생성 순서의 타이밍이 안맞아서 나중에 객체로 바꿔준다)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article =models.ForeignKey(Article, on_delete=models.CASCADE)
    # 외래키 위에 모델(참조하는 모델 클래스)을 받아와준다, 외래 키가 참조하는 객체가 사라졌을 때 어떻게 처리할지를 정의
    # 보기 편한 곳에 작성하면됨 실제론는 필드의 마지막에 작성 
    # 참조하는 모델 클래스의 단수형으로 작성
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.content