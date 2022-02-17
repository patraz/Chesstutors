from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.urls import reverse
from userprofile.models import Userprofile


User = settings.AUTH_USER_MODEL

# Create your models here.

DAYS_OF_WEEK = (
    ('Poniedziałek', 'Poniedziałek'),
    ('Wtorek', 'Wtorek'),
    ('Środa', 'Środa'),
    ('Czwartek', 'Czwartek'),
    ('Piątek', 'Piątek'),
    ('Sobota', 'Sobota'),
    ('Niedziela', 'Niedziela'),
)

CURRENCY = (
    ('PLN', 'PLN'),
    ('USD', 'USD'),
    ('NOK', 'NOK'),
    ('RUB', 'RUB'),
    ('EUR', 'EUR')
)

RATING = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)



class Announcement(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=True, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY)

    def get_announcement_picture(self):
        u_prof = Userprofile.objects.get(user = self.user)
        return u_prof.profile_picture.url

    def get_id_str(self):
        return 'a'+str(self.id)

    def get_update_url(self):
        return reverse('announcements:update', kwargs={"id":self.id})

    def get_hx_av_url(self):
        return reverse('announcements:hx_av', kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse('announcements:delete', kwargs={"id":self.id})

    def get_absolute_url(self):
        return reverse('announcements:detail', kwargs={"id": self.id}) 
    
    def announcement_count(self):
        return self.objects.all().count()

class Avaliability(models.Model):
    announcement = models.ForeignKey(Announcement,on_delete = models.CASCADE, related_name='avs')
    day = models.CharField(max_length=12, choices=DAYS_OF_WEEK)
    av_from = models.TimeField(null=True, blank=True)
    av_to = models.TimeField(null=True, blank=True)

    def seven_max(self):
        return self.announcement.avs.count()
    
    def get_absolute_url(self):
        return self.announcement.get_absolute_url()

class Comment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    announcement = models.ForeignKey(Announcement,on_delete = models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATING)
    publish = models.DateTimeField(auto_now_add=True)

    def get_com_author(self):
        u_prof = Userprofile.objects.get(user = self.user)
        return u_prof.profile_picture.url
