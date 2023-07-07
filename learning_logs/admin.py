from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic
from learning_logs.models import Entry


admin.site.register(Entry)
admin.site.register(Topic)
