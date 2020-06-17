from django.db import models
from users.models import Users
# Create your models here.


class Comments(models.Model):
    user_account = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True)
    # CharField에서는 null보다 black를 더 많이 쓴다.
    comment_text = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 최초 생성 시간이 기록
    updated_at = models.DateTimeField(auto_now=True)  # 마지막 수정 시간이 기

    class Meta:
        db_table = "comments"
