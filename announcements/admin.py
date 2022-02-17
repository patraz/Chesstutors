from django.contrib import admin

from announcements.models import Announcement, Avaliability, Comment

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class AvailabilityInline(admin.StackedInline):
    model = Avaliability
    extra = 0
    # readonly_fields = ['quantity_as_float', 'as_mks', "as_imperial"]
    # fields = ['name', 'quantity','quantity_as_float', 'unit', 'directions']

class AnnouncementAdmin(admin.ModelAdmin):
    inlines = [AvailabilityInline, CommentInline]    
    list_display = ['id', 'user', 'title',]
    search_fields = ['title','content']


admin.site.register(Announcement, AnnouncementAdmin)


