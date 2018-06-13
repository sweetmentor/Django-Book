from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from .forms import UserLoginForm,UserRegistrationForm

# Create your views here.
