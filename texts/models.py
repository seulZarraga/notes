from django.db import models

class Note(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__ (self):
    	return "{}... ".format(self.text[:30])