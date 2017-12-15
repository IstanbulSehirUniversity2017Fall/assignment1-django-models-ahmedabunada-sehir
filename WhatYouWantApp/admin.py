# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Episode
from .models import Season

# Register your models here.
admin.site.register(Season)
admin.site.register(Episode)
