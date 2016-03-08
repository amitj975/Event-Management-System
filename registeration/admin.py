from django.contrib import admin
from registeration.models import *
#from events.models import *

class EventAdmin(admin.ModelAdmin):
	list_display = ('name','event_coordi','contact_id_coordinator','participants_list',)
	list_filter = ('name','event_coordi','Actual_time')

class EventAdmin(admin.ModelAdmin):
	exclude=('Actual_time','participants_list')


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('Name','Email','phone')
	list_filter = ('user',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Event,EventAdmin)
