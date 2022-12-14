from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateField()
    likes = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.content
    