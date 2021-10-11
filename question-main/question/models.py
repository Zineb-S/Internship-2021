from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):

    titre = models.CharField(max_length=255, verbose_name="titre de la question")
    date_de_publication = models.DateTimeField(verbose_name="date de publication", null=False)
    user = models.ForeignKey(User, verbose_name="celui qui a pose la question", null=True, related_name="questionuser",
                             on_delete=models.PROTECT)

    def __str__(self):
        return self.titre

