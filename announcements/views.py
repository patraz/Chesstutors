from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect, Http404, HttpResponse

from .models import Announcement, Avaliability
from .forms import AnnouncementForm, AvailabilityForm, CommentForm
from userprofile.models import Userprofile
# Create your views here.

@login_required
def announcement_detail_view(request, id=None):
    user = get_object_or_404(Userprofile, user=request.user)
    obj = get_object_or_404(Announcement, id=id)
    author = get_object_or_404(Userprofile, user = obj.user)
    form = CommentForm(request.POST or None)
    context = {
        'obj':obj,
        'form':form,
        'user':user,
        'author':author
    }
    if form.is_valid():
        com = form.save(commit=False)
        com.user = request.user
        com.announcement = obj
        com.save()
        form = CommentForm()
        context['form'] = form
        return render(request, "form_comments.html", context)
    return render(request, "announcements/detail.html", context)

@login_required
def announcement_list_view(request):
    qs = reversed(Announcement.objects.all())
    context = {
        'object_list':qs,
    }
    return render(request, "announcements/list.html", context)

@login_required
def announcement_create_view(request,id=None):
    form = AnnouncementForm(request.POST or None)
    av_form = AvailabilityForm(request.POST or None)
    context = {
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            an = form.save(commit=False)
            an.user = request.user
            an.save()
            context['av_form'] = av_form
            context['message'] = 'zapisano'
            form = AnnouncementForm(request.POST or None, instance = an)
            return redirect(an.get_hx_av_url())
 
    
    return render(request, "announcements/create-update.html", context)

@login_required
def av_form(request, id=None):
    
    obj = get_object_or_404(Announcement, id=id, user=request.user)
    form = AnnouncementForm(request.POST or None, instance =obj)
    av_form = AvailabilityForm(request.POST or None)
    context = {
        'av_form':av_form,
        'form':form,
        'obj':obj,
        'btn': True
    }
    if not request.htmx:
            
        return redirect(obj.get_update_url())

        raise Http404
    if request.method == "PATCH":
        return redirect(obj) 
    if request.method == "PUT":
        return render(request, "announcements/partials/date.html", context) 
    if request.method == "POST":
        if av_form.is_valid():
            aval = av_form.save(commit=False)
            aval.announcement = obj
            aval.save()
            return render(request, "announcements/availability.html", {'obj':obj}) 
    return render(request, "announcements/partials/forms.html", context) 

def av_delete(request, id= None, av_id=None):
    obj = get_object_or_404(Announcement, id=id, user=request.user)
    av_obj = get_object_or_404(Avaliability,  id = av_id)
    form = AnnouncementForm(request.POST or None, instance =obj)
    context = {
        'av_form':av_form,
        'obj':obj,
        'form':form,
        'btn': True
    }
    if request.method == 'POST':
        av_obj.delete()
        return render(request, "announcements/availability.html", context) 
        

@login_required
def announcement_update_view(request, id=None):
    obj = get_object_or_404(Announcement, id=id, user=request.user)
    form = AnnouncementForm(request.POST or None, instance=obj)
    context = {
        'form':form,
        'obj':obj,
        'btn': True,
    }

    # if request.method == "PUT":
    #     print(request.POST['form'])
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         obj.save()
    #         context['message'] = 'zapisano'
        # return render(request, "announcements/create-update.html", context)
    if request.method == "POST":
        if form.is_valid():
            an = form.save(commit=False)
            an.save()
            # context['av_form'] = av_form
            context['message'] = 'zapisano'
            form = AnnouncementForm(request.POST or None, instance = an)
            return render(request, "announcements/create-update.html", context)
    # if request.method == "POST":
    #     if form.is_valid():
    #         an = form.save(commit=False)
    #         an.save()
    #         context['message'] = 'zapisano'
    #     return redirect(an.get_hx_av_url())
    return render(request, "announcements/create-update.html", context)

@login_required
def announcement_delete_view(request, id=None, parent_id=None):

    try:
        obj = Announcement.objects.get(id=id, user = request.user)
    except:
        obj = None
    if obj is None:
        raise Http404
    obj = get_object_or_404(Announcement, id=id, user = request.user)
    context = {
    }
    if request.method == 'POST':
        obj.delete()
        qs_qty = Announcement.objects.filter(user = request.user).count()
        context['qs_qty'] = qs_qty
        return  render(request, "hidden.html", context)
    
    return HttpResponse('')

