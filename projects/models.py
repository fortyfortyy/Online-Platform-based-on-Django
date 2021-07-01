from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)    # Allow to create in database out this value and don't need to set description,
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)    # class Tag will be found even when its under the class Project
    vote_total = models.IntegerField(default=0, null=True, blank=True)     # Votes set up to 0 at the beginning
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)     # Whether vote was positive or negative
    created = models.DateTimeField(auto_now_add=True)    # When the project was added to db
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)  # When the project was added to db
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)  # When the project was added to db
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
