from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=25, blank=False, unique=True)

    def __str__(self):
         return f"{self.tag}"

class Author(models.Model):
    fullname = models.CharField(max_length=50, blank=False)
    born_date = models.DateField(blank=True)
    born_location = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)

    # def __str__(self):
    #      return f"{self.fullname}, Born: {self.born_date} {self.born_location}"

    def __str__(self):
         return f"{self.fullname}"


class Quote(models.Model):
      quote  = models.CharField(max_length=500, unique=True, blank=False)
      author  = models.ForeignKey(Author, on_delete=models.CASCADE)
      tags = models.ManyToManyField(Tag)

      def __str__(self):
           return f"{self.quote}"

