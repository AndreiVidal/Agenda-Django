from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'created_at',
        'show',
    )

    list_display_links = ('id','first_name')

    search_fields = ('first_name', 'last_name', 'email')
    search_help_text = 'Search by first name, last name, or email.'
    ordering = ('-id',)

    list_per_page = 10
    list_max_show_all = 200

    list_editable = ('phone_number', 'email','show')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)