
from django.contrib import admin
from .models import Case, Hearing, Document, Notification

admin.site.register(Case)
admin.site.register(Hearing)
admin.site.register(Document)
admin.site.register(Notification)
