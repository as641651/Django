from django.contrib import admin

# Register your models here.
from . import models

#to reorder the fields in the detail view of Movie object in admin interface
# The name of this class should be name of model followed by 'Admin'
class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year','title']

    #Displays a search box and helps searching my movie title or length
    search_fields = ['title','length']

    #Adding filters
    # Not all fields can be appropriate for filters
    #used for only categorical fields
    list_filter = ['release_year']

    #Displays additional fields in the list view page of the model
    list_display = ['title','release_year','length']

    #List of fields that are allowed to be editable in list view of the model
    #NOTE : This set should be a subset of list_display
    list_editable = ['length']

#Register this class along with your original model
admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer)
