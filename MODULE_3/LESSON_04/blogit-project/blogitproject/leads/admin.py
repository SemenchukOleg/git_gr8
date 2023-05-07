from django.contrib import admin
from leads.models import Lead
import csv
from django.http import HttpResponse
from datetime import datetime

# Register your models here.
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="report_{}.csv"'.format(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        
        return response
    
    export_as_csv.short_description = 'Export Selected'


class LeadAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions_on_top = False
    actions_on_bottom = True
    list_display = ('id', 'subject', 'name', 'email', 'short_message', 'created_at', 'updated_at', 'is_unswered',)
    list_display_links = ('id', 'subject',)
    search_fields = ('email', 'subject',)
    list_filter = ('is_unswered',)
    list_editable = ('is_unswered',)
    readonly_fields = ('name', 'subject', 'email', 'message',)
    actions = ['export_as_csv']

    def short_message(self, obj):
        return obj.message[:20] + '...'


admin.site.register(Lead, LeadAdmin)