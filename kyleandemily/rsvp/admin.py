from django.contrib import admin

from .models import Invitation, Person

class PersonInline(admin.TabularInline):
    model = Person
    extra = 0

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('name', 'responded', 'welcome_guests', 'wedding_guests', 'farewell_guests')
    readonly_fields = ('responded',)
    inlines = (PersonInline,)

admin.site.register(Invitation, InvitationAdmin)