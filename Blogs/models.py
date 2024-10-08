from django.db import models
from django.utils.safestring import mark_safe


class Categoria(models.Model):
    categoria=models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):

        return '%s' % (self.categoria)


    class Meta:
        verbose_name_plural = "1. Categorias"

class Blogs(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen=models.FileField(upload_to='blog/',help_text='imagen de 1280*500')
    fecha=models.DateField()
    titulo=models.CharField(max_length=200, null=True, blank=True)
    articulo=models.TextField(max_length=10000, null=True, blank=True)
    autor = models.CharField(max_length=200, null=True, blank=True)
    tipo_archivo=models.CharField(max_length=20, default='imagen', choices=(("imagen", "imagen"), ("video", "video")))
    tipo_imagen=models.FileField(upload_to='blog/', null=True,blank=True ,help_text='imagen de 1280*500')
    tipo_video_link=models.CharField(max_length=120, null=True,  blank=True)


    def __str__(self):

        return '%s ' % (self.categoria.categoria)

    def miniatura(self):
        return mark_safe("<img src='/media/%s' style='width: 200px'>" % self.imagen)

    class Meta:
        verbose_name_plural = "2. Blogs"


class Visitas_Blog(models.Model):
    blog=models.OneToOneField(Blogs, on_delete=models.CASCADE ,null=True,blank=True)
    visita=models.IntegerField(default=1)


    def visitar(self):
        return "<a target='blank' href='http://www.zatuar.com/blog/%s'>Ver en la Web</a>" % (self.blog.id)

    visitar.allow_tags = True
    visitar.short_description = "Ir"

    def save(self, *args, **kwargs):
        self.visita += 1
        super(Visitas_Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "4. Visitas al Blog"