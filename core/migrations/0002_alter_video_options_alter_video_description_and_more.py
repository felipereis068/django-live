# Generated by Django 5.1.2 on 2024-11-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Vídeo', 'verbose_name_plural': 'Vídeos'},
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='video',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Esta publicado?'),
        ),
        migrations.AlterField(
            model_name='video',
            name='num_likes',
            field=models.IntegerField(default=0, verbose_name=' Está publicado'),
        ),
        migrations.AlterField(
            model_name='video',
            name='num_views',
            field=models.IntegerField(default=0, verbose_name='Numero de visualizações'),
        ),
        migrations.AlterField(
            model_name='video',
            name='published_at',
            field=models.DateTimeField(verbose_name='Publicado em'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnails/', verbose_name='Miniatura'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/', verbose_name='Vídeo'),
        ),
    ]