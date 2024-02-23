# What is a QuerySet?Write program to create a new Post object in
# database:
"""
- QuerySet is a collection of database query result. it is used to retrieve,filter and manipulate data using django.

- Example-
    from django.db import models

    class Post(models.Model):
        title = models.CharField(max_length=255)
        content = models.CharField(max_length=255)
        date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
"""
