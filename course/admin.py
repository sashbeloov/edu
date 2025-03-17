from django.contrib import admin
from .models import Course, Tag, Prerequisite, Learning, Video

class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.TabularInline):
    model = Video
class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, PrerequisiteAdmin, LearningAdmin, VideoAdmin]

admin.site.register(Course , CourseAdmin)
admin.site.register(Video)
