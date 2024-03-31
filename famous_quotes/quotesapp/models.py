from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=50, blank=False, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
         return f"{self.tag}"

class Author(models.Model):
    fullname = models.CharField(max_length=50, blank=False)
    born_date = models.DateField(blank=True)
    born_location = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
         return f"{self.fullname}"


class Quote(models.Model):
      quote  = models.TextField(unique=True, blank=False)
      author  = models.ForeignKey(Author, on_delete=models.CASCADE)
      tags = models.ManyToManyField(Tag)
      created_at = models.DateField(auto_now_add=True)

      def __str__(self):
           return f"{self.quote}"

