# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from . models import Episode
from django.shortcuts import render

# Create your views here.

def test(request):
    return HttpResponse("This is a test! Is it working?")


def WhichEpisode(request, EpisodeId):
    return HttpResponse("%s"%(Episode.objects.get(pk=EpisodeId)))