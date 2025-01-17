from django.db import models
from django.contrib.auth.models import User

from common.models import AbstractCreateUpdateModel, AbstractCreateModel


class Author(AbstractCreateUpdateModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Blog(AbstractCreateUpdateModel):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    
class Comments(AbstractCreateModel):
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    