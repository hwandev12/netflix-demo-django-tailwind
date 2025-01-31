from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=100)
    
    def __str__(self):
        return self.language
    
class Addlanguage(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)