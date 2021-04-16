from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Blog Default from Model")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    #form submiting URL to redirect in adding new post in frontend
    # and redirect to 'article-detail'
    def get_absolute_url(self):
        # go to article-detail page with id as arg for assign as pk value
        return reverse('article-detail', args=(str(self.id)))
        #go to home after form submitted
        #return reverse('home')
