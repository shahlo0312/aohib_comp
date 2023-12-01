from .manager_base import BaseModel
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from hitcount.models import HitCountMixin
# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    # def get_hit_count(self):
    #     return HitCount.objects.filter(post=self).count()
    

class Tags(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
            return self.name


class News(BaseModel):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='news/')
    view_count = models.BigIntegerField(default=0, null=True, blank=True)
    body = models.TextField()
    slug = models.SlugField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="news_user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news_category")
    tags = models.ManyToManyField(Tags, related_name='news_tag')

    
   
    

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)

        super(News, self).save()

    def __str__(self) -> str:
        return self.title



# class HitCount():

#     ip_address = models.GenericIPAddressField()
#     post = models.ForeignKey("Category", on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.ip_address} => {self.post.name}'




