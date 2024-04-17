from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Blogs)
# admin.site.register(Distinguished)
from.models import *
# Register your models here.
class Show(admin.ModelAdmin):
    
    list_display=['name1','number','doctor','age','gender','data']
    list_display_links=['number','doctor','age','gender','data']
    
    search_fields=['number','doctor','age','gender','data']
    list_filter=['number','doctor','age','gender','data']

admin.site.register(LOGIN)
admin.site.register(Callus)
admin.site.register(ExpertDoctor)

admin.site.site_header='Hospital manage system'
admin.site.site_title='Hospital system'

admin.site.site_url='name'


