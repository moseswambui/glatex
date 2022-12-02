from django.db import models
from accounts.models import Account
class Type(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Blog(models.Model):
    author=models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    blog = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.TextField( null=True, blank=True)  

class Reply(models.Model):
    pass
