# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required

from datetime import *
from sistema.models import *
from sistema.forms import *


def home(request):
    return render(request, 'home.html', locals())
