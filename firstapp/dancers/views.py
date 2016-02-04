# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from dancers.models import Dancer
from extuser.models import ExtUser
from django.contrib import auth
from django.core.context_processors import csrf
from dancers.forms import DancerForm
# Create your views here.


def dancers(request):
    args = {}
    args.update(csrf(request))
    args['form'] = DancerForm()
    args['club'] = auth.get_user(request).clubname
    args['treaner'] = auth.get_user(request).name
    if auth.get_user(request).is_active:
        # args['dancers'] = Dancer.objects.filter(dancer_name__istartswith = 'мар')
        args['dancers'] = Dancer.objects.filter(dancer_trainer = auth.get_user(request))
        args['user'] = auth.get_user(request)
    if request.POST:
        newuser_form = DancerForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('dancers.html', args)

def adddancer(request):
    args = {}
    args.update(csrf(request))
    args['form'] = DancerForm()
    if auth.get_user(request).is_active:
        # args['dancers'] = Dancer.objects.filter(dancer_name__istartswith = 'мар')
        args['user'] = auth.get_user(request)
    return render_to_response('adddancer.html', args)
def savedancer(request):
    args = {}
    args.update(csrf(request))
    args['form'] = DancerForm()
    args['club'] = auth.get_user(request).clubname
    args['treaner'] = auth.get_user(request).name
    if request.POST and ("pause" not in request.session):
        form = DancerForm(request.POST)
        if form.is_valid():
            dancer = form.save(commit=False)
            dancer.dancer_trainer = auth.get_user(request)
            form.save()
    return redirect('/dancers/', args)

def delete_dancer(request, dancer_id=1):
    args = {}
    args.update(csrf(request))
    Dancer.objects.filter(id=dancer_id).delete()
    args['user'] = auth.get_user(request)
    return redirect('/dancers/', args)




