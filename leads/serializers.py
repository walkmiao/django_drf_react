#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 22:04
# @Author  : lch
# @File    : serializers.py
from rest_framework import serializers
from leads.models import Leads


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ('id', 'name', 'email', 'message')

