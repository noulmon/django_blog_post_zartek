from django.contrib import admin

from post.models import Post, PostImage


class PostImageInline(admin.StackedInline):
    model = PostImage
    extra = 1
    show_change_link = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]

    fieldsets = (
        (None, {'fields': ('title', 'description', 'tags', 'created_by',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'description', 'tags', 'created_by')}
         ),
    )

    list_display = ('title', 'created_by', 'created_at', 'num_vote_up', 'num_vote_down',)
