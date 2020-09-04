from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    # text = models.TextField(max_length=5000)

    def __str__(self):
        return f'Username = {self.username}, Password = {self.password}, notes={self.note_set.all()}'

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(max_length=5000)
    # def __str__(self):
    #     return self.note