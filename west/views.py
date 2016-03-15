# -*- coding: utf-8 -*-

from django.http import HttpResponse
from west.models import Character
from django.shortcuts import render

def first_page(request):
    return HttpResponse("<p>西餐</p>")

def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(str, staff_list)
    return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")

def templay(request):
    context = {}
    context['label'] = 'Hello World!'
    staff_list = Character.objects.all()
    staff_str = map(str, staff_list)
    context['labelname'] = ' '.join(staff_str)
    context['staffs'] = staff_list
    test_list = ['a',['bb','bc'],{'name':'cwj','age':15}]
    context['list'] = test_list
    test_dict = {'name':'juke','age':25}
    context['dict'] = test_dict
    return render(request, 'templay.html', context)

def inherit(request):
    context = {}
    return render(request,'inherit_base.html')

from django.template.context_processors import csrf

def form(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['staff']
        new_record = Character(name=ctx['rlt'])
        new_record.save()
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    return render(request,'form.html',ctx)

def investigate(request):
    rlt = request.GET['staff']
    return HttpResponse(rlt)

from django import forms

class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 5)

def investigates(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted  = form.cleaned_data['name']
            new_record = Character(name = submitted)
            new_record.save()

    form = CharacterForm()
    ctx ={}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form']  = form
    return render(request, "investigates.html", ctx)