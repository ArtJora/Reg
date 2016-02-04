# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from context.models import Context, Context_dancer
from dancers.models import Dancer
from django.core.context_processors import csrf
from django.contrib import auth
from context.forms import ContextDancerForm, ContextContentForm, ContextDuetForm



def contexts(request):
    args = {}
    args.update(csrf(request))
    args['form_add_context'] = ContextContentForm()
    args['contexts'] = Context.objects.all().order_by('context_date')
    args['user'] = auth.get_user(request)
    return render_to_response('turnirs.html', args)


def context_dancers(request, context_id=1):
    args = {}
    args.update(csrf(request))
    args['form'] = ContextDancerForm()
    args['form2'] = ContextDuetForm()
    if auth.get_user(request).is_active:
        args['context_dancers'] = Context_dancer.objects.filter(context_dancer_treaner = auth.get_user(request),context_name=context_id)
        args['user'] = auth.get_user(request)
        args['contexta'] = context_id
        args['context_name'] = Context.objects.get(id=context_id)
        args['club'] = auth.get_user(request).clubname
        args['treaner'] = auth.get_user(request).name
    if request.POST:
        newuser_form = ContextDancerForm(request.POST)
        if newuser_form.is_valid():
            dancer = newuser_form.save(commit=False)
            # k=newuser_form.cleaned_data['context_dancer_name']
            # j=len(k)
            # if j > 3:
            #     k = 1
            k=0
            if len(newuser_form.cleaned_data['context_dancer_name']) > 3:
                k+=1

                message = newuser_form.cleaned_data['context_dancer_name']
            if len(newuser_form.cleaned_data['context_dancer_name2']) > 3:
                k+=1
                x = '------'
                dancer.context_dance_league = x
                message = message+'\n'+newuser_form.cleaned_data['context_dancer_name2']
            if len(newuser_form.cleaned_data['context_dancer_name3']) > 3:
                k+=1
                x = '------'
                dancer.context_dance_league = x
                message = message+'\n'+newuser_form.cleaned_data['context_dancer_name3']
            if len(newuser_form.cleaned_data['context_dancer_name4']) > 3:
                k+=1
                x = '------'
                dancer.context_dance_league = x
                message = message+'\n'+newuser_form.cleaned_data['context_dancer_name4']
            if len(newuser_form.cleaned_data['context_dancer_name5']) > 3:
                k+=1
                x = '------'
                dancer.context_dance_league = x
                message = message+'\n'+newuser_form.cleaned_data['context_dancer_name5']
            if len(newuser_form.cleaned_data['context_dancer_name6']) > 3:
                k+=1
                x = '------'
                dancer.context_dance_league = x
                message = message+'\n'+newuser_form.cleaned_data['context_dancer_name6']
            if len(newuser_form.cleaned_data['context_dancer_name7']) > 3:
                k+=1
                x = '------'
                dancer.context_dance_league = x
                message = message+'\n'+newuser_form.cleaned_data['context_dancer_name7']
            dancer.context_dancer_name = message
            dancer.context_dancer_treaner = auth.get_user(request)
            dancer.context_dancer_sum = k
            dancer.context_name = Context.objects.get(id=context_id)
            newuser_form.save()
            return redirect('/context/%s/' %context_id)
        else:
            args['form'] = newuser_form

    return render_to_response('contex_dancers.html', args)
def addsolo(request, context_id=1):
    args = {}
    args.update(csrf(request))
    args['form'] = ContextDancerForm()
    args['form2'] = ContextDuetForm()
    if auth.get_user(request).is_active:
        args['context_dancers'] = Context_dancer.objects.filter(context_dancer_treaner = auth.get_user(request),context_name=context_id)
        args['user'] = auth.get_user(request)
        args['contexta'] = context_id
        args['context_name'] = Context.objects.get(id=context_id)
        args['club'] = auth.get_user(request).clubname
        args['treaner'] = auth.get_user(request).name
    if request.POST:
        newuser_form = ContextDancerForm(request.POST)
        if newuser_form.is_valid():
            # k=newuser_form.cleaned_data['context_dancer_name']
            # j=len(k)
            if j > 3:
                k = 1

            message = newuser_form.cleaned_data['context_dancer_name']
            dancer = newuser_form.save(commit=False)
            dancer.context_dancer_name = message
            dancer.context_dancer_treaner = auth.get_user(request)
            dancer.context_dancer_sum = k
            dancer.context_name = Context.objects.get(id=context_id)
            newuser_form.save()
            return redirect('/context/%s/' %context_id)
        else:
            args['form'] = newuser_form

    return render_to_response('addsolo.html', args)
def addduet(request, context_id=1):
    args = {}
    args.update(csrf(request))
    args['form'] = ContextDancerForm()
    args['form2'] = ContextDuetForm()
    if auth.get_user(request).is_active:
        args['context_dancers'] = Context_dancer.objects.filter(context_dancer_treaner = auth.get_user(request),context_name=context_id)
        args['user'] = auth.get_user(request)
        args['contexta'] = context_id
        args['context_name'] = Context.objects.get(id=context_id)
        args['club'] = auth.get_user(request).clubname
        args['treaner'] = auth.get_user(request).name

    return render_to_response('addduet.html', args)
def addgruppa(request, context_id=1):
    args = {}
    args.update(csrf(request))
    args['form2'] = ContextDancerForm()
    if auth.get_user(request).is_active:
        args['context_dancers'] = Context_dancer.objects.filter(context_dancer_treaner = auth.get_user(request),context_name=context_id)
        args['user'] = auth.get_user(request)
        args['contexta'] = context_id
        args['context_name'] = Context.objects.get(id=context_id)
        args['club'] = auth.get_user(request).clubname
        args['treaner'] = auth.get_user(request).name

    return render_to_response('addgruppa.html', args)

def delete_dancers(request, dancer_id=1, context_id=1):
    args = {}
    args.update(csrf(request))
    args['form'] = ContextDancerForm()
    Context_dancer.objects.filter(id=dancer_id).delete()
    args['user'] = auth.get_user(request)
    return redirect('/context/%s/' %context_id)


def search_dancer(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    args = {}
    args.update(csrf(request))
    args['hello'] = 'Hello world'
    args['dancers'] = Dancer.objects.filter(dancer_name__istartswith=search_text,dancer_trainer=auth.get_user(request))
    return render_to_response('3.html', args)

def search_dance_program(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    args = {}
    args.update(csrf(request))
    args['dancers'] = Context.objects.filter(id=search_text)
    return render_to_response('4.html', args)

def search_age_category(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    args = {}
    args.update(csrf(request))
    args['dancers'] = Context.objects.filter(id=search_text)
    return render_to_response('5.html', args)

def search_dance_league(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    args = {}
    args.update(csrf(request))
    args['dancers'] = Context.objects.filter(id=search_text)
    return render_to_response('6.html', args)

def addcontext(request):
    args = {}
    args.update(csrf(request))
    args['form_add_context'] = ContextContentForm()
    if auth.get_user(request).is_active:
        args['contexts'] = Context.objects.all()
        args['user'] = auth.get_user(request)
    if request.POST:
        newuser_form = ContextContentForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            return redirect('/context/')
        else:
            args['form'] = newuser_form
    return render_to_response('addcontext.html', args)

def add_duet(request, context_id=1):
    args = {}
    args.update(csrf(request))
    args['form'] = ContextDancerForm()
    args['form2'] = ContextDuetForm()
    if auth.get_user(request).is_active:
        args['context_dancers'] = Context_dancer.objects.filter(context_dancer_treaner = auth.get_user(request),context_name=context_id)
        args['user'] = auth.get_user(request)
        args['contexta'] = context_id
        args['context_name'] = Context.objects.get(id=context_id)
        args['club'] = auth.get_user(request).clubname
        args['treaner'] = auth.get_user(request).name
    if request.POST:
        newuser_form = ContextDuetForm(request.POST)
        if newuser_form.is_valid():
            k=newuser_form.cleaned_data['context_dancer_name']
            j=len(k)
            if j > 3:
                k = 1
            else:
                k = 0
            q=newuser_form.cleaned_data['context_dancer_name2']
            j=len(q)
            if j > 3:
                message = newuser_form.cleaned_data['context_dancer_name']+'\n'+newuser_form.cleaned_data['context_dancer_name2']
                k += 1

            dancer = newuser_form.save(commit=False)
            dancer.context_dancer_name = message
            dancer.context_dancer_treaner = auth.get_user(request)
            dancer.context_dancer_sum = k
            dancer.context_name = Context.objects.get(id=context_id)
            x = ' '
            dancer.context_dance_league = x
            newuser_form.save()
            return redirect('/context/%s/' %context_id)
        else:
            args['form2'] = newuser_form
    return render_to_response('contex_dancers.html', args)