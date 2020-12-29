from django.db import models
from django.template.defaultfilters import truncatewords

# Create your models here.
class Blog(models.Model):
    
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return truncatewords(self.body,50)