from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class MatrixA(models.Model):
    N = models.PositiveIntegerField(verbose_name='N',  default=2, validators=[MinValueValidator(2), MaxValueValidator(10)])
    M = models.PositiveIntegerField(verbose_name='M', default=2, validators=[MinValueValidator(2), MaxValueValidator(10)])
    result = models.IntegerField(verbose_name='Результат', default=None, null=True)

    def __str__(self):
        return "Матрица А"

    class Meta:
        verbose_name = 'Матрица А'
        verbose_name_plural = 'Матрица А'


class MatrixB(models.Model):
    N = models.PositiveIntegerField(verbose_name='N', default=2, validators=[MinValueValidator(2), MaxValueValidator(10)])
    M = models.PositiveIntegerField(verbose_name='M', default=2, validators=[MinValueValidator(2), MaxValueValidator(10)])
    result = models.IntegerField(verbose_name='Результат', default=None, null=True)

    def __str__(self):
        return "Матрица В"

    class Meta:
        verbose_name = 'Матрица B'
        verbose_name_plural = 'Матрица B'
