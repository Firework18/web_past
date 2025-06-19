from django.db import models


class Category(models.Model):
    descript = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.descript

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
