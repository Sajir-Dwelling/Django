from django.contrib import admin
from .models import Contact, MenuItem, Testimonial, GalleryImage

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']  # Remove 'price' from here
    list_editable = ['order']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'is_approved', 'created_at', 'order']
    list_filter = ['is_approved', 'rating', 'created_at']
    list_editable = ['is_approved', 'order']
    search_fields = ['name', 'message']

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['title', 'description']