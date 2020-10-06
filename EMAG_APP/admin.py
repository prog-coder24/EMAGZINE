from .forms import *
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import Group
from django.contrib import admin


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('full_name', 'dept_name',)
    list_filter = ('full_name', 'dept_name',)
    fieldsets = (
        ('Personal Information', {
         'fields': ('email', 'full_name', 'dept_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)}
         ),
    )
    readonly_fields = ('email', 'full_name', 'dept_name')
    search_fields = ('email',)
    ordering = ('email',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'project_description')


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('achievement_title', 'achievement_field')


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_category',
                    'event_date')


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Event, EventAdmin)
admin.site.unregister(Group)
