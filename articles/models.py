from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add='True')
    thumbNail = models.ImageField(default="defaultImg.png", blank=True)
    

    def __str__(self):
        return self.title

    def article_body_view(self):
        if len(self.body)>160:
            return self.body[:160] + ' ...Read Full'
        else:
            return self.body
