import json
from django.db import models
from channels import Group

# Create your models here.

class Current(models.Model):
    slide_name = models.CharField(max_length=200)
    page = models.IntegerField()

    def send_notification(self):
        notification = {
            "id": self.id,
            "slide_name": self.slide_name,
            "page": self.page,
        }
        Group("chat").send({
            "text": json.dumps(notification),
        })
    def save(self, *args, **kwargs):
        result = super(Current, self).save(*args, **kwargs)
        self.send_notification()
        return result


class Slides(models.Model):
    slide_text = models.CharField(max_length=200)
    page = models.IntegerField()
    img_source = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.slide_text +' '+ str(self.page)

    def send_notification(self):
        notification = {
            "id": self.id,
            "slide_name": self.slide_text,
            "votes": self.votes,
        }
        Group("chat").send({
            "text": json.dumps(notification),
        })
    def save(self, *args, **kwargs):
        result = super(Slides, self).save(*args, **kwargs)
        self.send_notification()
        return result
