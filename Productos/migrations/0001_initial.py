# Generated by Django 3.0.8 on 2020-08-12 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Ciudad',
            },
        ),
        migrations.CreateModel(
            name='Clasif_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion_producto', models.CharField(blank=True, max_length=90, null=True)),
            ],
            options={
                'verbose_name_plural': '3. Clasificaciòn de Producto',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('image_a', models.FileField(blank=True, help_text='100x100', null=True, upload_to='products/')),
                ('image_b', models.FileField(blank=True, help_text='100x100', null=True, upload_to='products/')),
                ('foto_slider', models.FileField(blank=True, null=True, upload_to='producto/')),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('caracteristicas', models.TextField(blank=True, max_length=500, null=True)),
                ('tamanos', models.CharField(blank=True, max_length=500, null=True)),
                ('material', models.CharField(blank=True, max_length=500, null=True)),
                ('textura', models.CharField(blank=True, max_length=30, null=True)),
                ('gramaje', models.CharField(blank=True, max_length=30, null=True)),
                ('nuevo', models.BooleanField(default=False)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('disponivilidad', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('clasif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Clasif_producto')),
            ],
            options={
                'verbose_name_plural': '4. Producto',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='proveedor/')),
                ('detalle', models.CharField(blank=True, max_length=300, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Ciudad')),
            ],
            options={
                'verbose_name_plural': '2. Proveedor',
            },
        ),
        migrations.CreateModel(
            name='Producto_Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('slider', models.FileField(blank=True, help_text='1884x529', null=True, upload_to='slider')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Product')),
            ],
            options={
                'verbose_name_plural': '1. Slider',
            },
        ),
        migrations.CreateModel(
            name='Producto_Personalizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='producto')),
                ('titulo', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Product')),
            ],
            options={
                'verbose_name_plural': '6. Producto Personalizacion',
            },
        ),
        migrations.CreateModel(
            name='Producto_Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField(default=0)),
                ('galeria_articulo', models.FileField(blank=True, help_text='imagen producto 800x800', null=True, upload_to='media')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Product')),
            ],
            options={
                'verbose_name_plural': '5. Producto Imagenes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Proveedor'),
        ),
    ]
