from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

'''
create table "blog_post"(
    id integer not null primary key autoincrement,
    title varchar(120) not null,
    content text not null,
    published_at datetime not null,
    author_id integer NOT NULL
        REFERENCES auth_user(id)
        DEFERRABLE INITIALLY DEFERRED
);
'''

# Create your models here.
# 어플리케이션은 각 게시물을 blog 사용자가 작성하며 사용자는 0개 이상의 게시물을 작성할 수 있다.
# 일대다 관계
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        #db_table = 'posts' / 게시물에 대한 내림차순을 관리하는 속성을 지정
        ordering = ["-published_at"]

# 내장 모듈이 가진 모델 'django.contrib.auth.models.User'


