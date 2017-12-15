# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Season(models.Model):
    Title = models.CharField(max_length=30)
    Creator = models.CharField(max_length=15)
    Producor = models.CharField(max_length=15)
    def __str__(self):
        return self.Title + " by " + self.Creator

class Episode(models.Model):
    s = models.ForeignKey(Season,on_delete=models.CASCADE)
    Title = models.CharField(max_length=30)
    EpisodeNumber = models.CharField(max_length=2)
    Director = models.CharField(max_length=15)
    ProductionCompany = models.CharField(max_length=15)
    Length = models.CharField(max_length=6)
    def __str__(self):
        return str(self.s) + " Episode " + self.EpisodeNumber + ": " + self.Title + " (" + self.Length + "), Directed by: " + self.ProductionCompany + " Produced by: " + self.ProductionCompany
