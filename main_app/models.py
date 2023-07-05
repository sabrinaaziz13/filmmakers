from django.db import models

class Director(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_director = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Director: " + self.name

    class Meta:
        ordering = ['name']

class Movie(models.Model):

    title = models.CharField(max_length=150)
    img = models.CharField(max_length=250)
    year = models.CharField(max_length=4)
    synopsis = models.TextField(max_length=500)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.title
    
    def get_year(self):
        return self.year
