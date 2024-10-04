from django.contrib import admin

# Register your models here.
from Blogs.models import *
from zatuarApp.snippers import Attr


class CategoriaAdmin(admin.ModelAdmin):
    list_display = Attr(Categoria)
    list_display_links = Attr(Categoria)
admin.site.register(Categoria, CategoriaAdmin)



class BlogsAdmin(admin.ModelAdmin):
    list_display = Attr(Blogs)+["miniatura"]
    list_display_links = Attr(Blogs)
admin.site.register(Blogs,BlogsAdmin)






