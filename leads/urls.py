#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 22:07
# @Author  : lch
# @File    : urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view()),
]