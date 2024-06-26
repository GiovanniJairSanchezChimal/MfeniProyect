# Generated by Django 4.2.9 on 2024-02-08 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmento_image1', models.URLField(max_length=1000)),
                ('segmento_image2', models.URLField(max_length=1000)),
                ('propuesta_image1', models.URLField(max_length=1000)),
                ('propuesta_image2', models.URLField(max_length=1000)),
                ('canales_image', models.URLField(max_length=1000)),
                ('relaciones_image', models.URLField(max_length=1000)),
                ('recursos_image', models.URLField(max_length=1000)),
                ('actividades_image', models.URLField(max_length=1000)),
                ('socios_image1', models.URLField(max_length=1000)),
                ('socios_image2', models.URLField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'GeneratedImage',
                'verbose_name_plural': 'GeneratedImages',
                'db_table': 'GeneratedImages',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AnswersChatgpt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmento_gpt', models.TextField(max_length=1000, verbose_name='segmento_gpt')),
                ('propuesta_gpt', models.TextField(max_length=700, verbose_name='propuesta_gpt')),
                ('canales_gpt', models.TextField(max_length=700, verbose_name='canales_gpt')),
                ('relaciones_gpt', models.TextField(max_length=700, verbose_name='relaciones_gpt')),
                ('recursos_gpt', models.TextField(max_length=700, verbose_name='recursos_gpt')),
                ('actividades_gpt', models.TextField(max_length=700, verbose_name='actividades_gpt')),
                ('socios_gpt', models.TextField(max_length=700, verbose_name='socios_gpt')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Respuesta_Chatgpt',
                'verbose_name_plural': 'Respuestas_Chatgpt',
                'db_table': 'answer_chatgpt',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='answers_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_e_p', models.TextField(max_length=30, verbose_name='Nombre_empresa_proyecto')),
                ('segmento', models.TextField(max_length=1000, verbose_name='segmento')),
                ('propuesta', models.TextField(max_length=1000, verbose_name='propuesta')),
                ('canales', models.TextField(max_length=1000, verbose_name='canales')),
                ('relaciones', models.TextField(max_length=1000, verbose_name='relaciones')),
                ('recursos', models.TextField(max_length=1000, verbose_name='recursos')),
                ('actividades', models.TextField(max_length=1000, verbose_name='actividades')),
                ('socios', models.TextField(max_length=1000, verbose_name='socios')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AnswerChatgpt',
                'verbose_name_plural': 'AnswersChatgpt',
                'db_table': 'answers_user',
                'ordering': ['id'],
            },
        ),
    ]
