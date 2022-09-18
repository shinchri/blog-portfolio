from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill,
    Tag
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'color')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name', 'has_been_viewed')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'date', 'is_active', 'is_featured')
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at', 'is_active')
    readonly_fields = ('slug',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score', 'is_key_skill')