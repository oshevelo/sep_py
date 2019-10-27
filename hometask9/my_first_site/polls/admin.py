from django.contrib import admin

# Register your models here.

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)


# admin.site.register(Question)
admin.site.register(Choice)