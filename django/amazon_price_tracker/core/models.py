from django.db import models


class CreatedModified(models.Model):
    """
    Extends Models of two useful
    fields: created and modified
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
