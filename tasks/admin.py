from django.contrib import admin
from tasks.models import Task, Category, Feedback


class FeedbackInline(admin.StackedInline):
    model = Feedback
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_from', 'price_to',
                    'visible', 'created', 'updated')
    list_editable = ('price_from', 'price_to', 'visible')
    list_filter = ('visible', 'created', 'updated')
    prepopulated_fields = {'slug': ('title', 'employer')}
    inlines = (FeedbackInline,)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'created')
    readonly_fields = ('created',)
