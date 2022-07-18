# Generated by Django 4.0.6 on 2022-07-16 23:48

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('rate', models.BigIntegerField()),
                ('min_order', models.BigIntegerField()),
                ('max_order', models.BigIntegerField()),
                ('description', ckeditor.fields.RichTextField(default='')),
                ('slug', models.SlugField(unique=True)),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]