from django.contrib import admin
from .models import Questions, Feedback

# Register your models here.
admin.site.register(Questions)
admin.site.register(Feedback)


admin.site.site_header = "Online-Examination"
admin.site.site_title = "Online-Examination"