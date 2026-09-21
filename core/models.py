from django.db import models

class Project(models.Model) :

    class Status(models.TextChoices):
        TODO = "TODO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        DONE = "DONE", "Done"


    name = models.CharField(max_length=50)
    project_url = models.CharField(max_length=200, null=True)
    progress = models.CharField(max_length=15
    ,
    choices=Status.choices,
    default=Status.TODO,
    )
    descriptions = models.TextField()

    def __str__(self) :
        return self.name
