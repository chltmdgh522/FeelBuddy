from django.contrib import admin

import feedback
from feedback.models import Community, Comment, Like

# Register your models here.
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Like)
