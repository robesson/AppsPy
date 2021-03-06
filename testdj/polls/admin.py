from django.contrib import admin
from polls.models import Choice, Poll



class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 4


class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['question']}),
		('Date information', 	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

   

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)

