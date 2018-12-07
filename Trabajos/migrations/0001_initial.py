# Generated by Django 2.1.1 on 2018-11-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('career', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=150)),
                ('link', models.URLField(blank=True, null=True, verbose_name='Direccionar a otro sitio')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]