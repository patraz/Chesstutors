from django.shortcuts import render, get_object_or_404
from django.template import context
from announcements.models import Announcement
# Create your views here.
from userprofile.models import Userprofile

def frontpage(request):
    return render(request, "frontpage.html")

def profile_view(request):
    user = get_object_or_404(Userprofile, user=request.user)
    qs = reversed(Announcement.objects.filter(user = request.user))
    qs_qty = Announcement.objects.filter(user = request.user).count()
    context = {
        'user':user,
        'object_list': qs,
        'qs_qty':qs_qty,
    }
    return render(request, 'profile.html', context)