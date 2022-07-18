from django.db import models

# Create your models here.


class Message(models.Model):
    user_name = models.CharField(max_length=32)
    user_ip = models.CharField(max_length=40)
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"Message<user={self.user!r}, content={self.content!r}, created_at={self.created_at!r}>"
