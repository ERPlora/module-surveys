from django.contrib import admin

from .models import Survey, SurveyQuestion

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'start_date', 'end_date', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ['survey', 'text', 'question_type', 'is_required', 'order', 'created_at']
    search_fields = ['text', 'question_type']
    readonly_fields = ['created_at', 'updated_at']

