from django.contrib import admin
from webapp.models import Tracker, Status, Type, Project

# class ProjectAdmin(admin.TabularInline):
#         model = Project
#         fields = ['project', 'depiction']
#
# class TrackerAdmin(admin.ModelAdmin):
#         list_display = ['pk', 'summary', 'description', 'status', 'type',
#                         'created_at']
#         list_filter = ['summary', 'status', 'type']
#         list_display_links = ['pk', 'summary', 'project', 'depiction']
#         search_fields = ['summary', 'description']
#         exclude = []
#         readonly_fields = ['created_at', 'updated_at']
#         inlines = [ProjectAdmin]

admin.site.register(Tracker)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)