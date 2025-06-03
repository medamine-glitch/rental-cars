from django.contrib import admin
from django.utils.html import format_html
from .models import Brand, Car, CarImage, Review, Testimonial, Partner, TeamMember, ContactMessage

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo')
    search_fields = ('name',)

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" height="50"/>', obj.logo.url)
        return '-'
    display_logo.short_description = 'Logo'

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'price_per_day', 'transmission', 'is_available', 'is_featured', 'rating')
    list_filter = ('brand', 'transmission', 'fuel_type', 'is_available', 'is_featured')
    search_fields = ('name', 'brand__name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CarImageInline]
    list_editable = ('is_available', 'is_featured', 'price_per_day')
    readonly_fields = ('rating', 'review_count')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'brand', 'year', 'price_per_day', 'description')
        }),
        ('Specifications', {
            'fields': ('transmission', 'fuel_type', 'seats', 'doors', 'engine', 'air_conditioning', 'mileage', 'color')
        }),
        ('Status', {
            'fields': ('is_available', 'is_featured', 'location')
        }),
        ('Media', {
            'fields': ('main_image',)
        }),
        ('Statistics', {
            'fields': ('rating', 'review_count'),
            'classes': ('collapse',)
        })
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'name', 'email', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('car__name', 'name', 'email', 'comment')
    readonly_fields = ('created_at',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'is_active', 'created_at')
    list_filter = ('rating', 'is_active', 'created_at')
    search_fields = ('name', 'comment')
    list_editable = ('is_active',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo', 'website', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    list_editable = ('is_active',)

    def display_logo(self, obj):
        return format_html('<img src="{}" height="50"/>', obj.logo.url)
    display_logo.short_description = 'Logo'

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'display_photo', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name', 'position', 'bio')
    list_editable = ('is_active', 'order')

    def display_photo(self, obj):
        return format_html('<img src="{}" height="50"/>', obj.photo.url)
    display_photo.short_description = 'Photo'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    actions = ['mark_as_read']
