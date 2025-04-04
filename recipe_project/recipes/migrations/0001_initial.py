# Generated by Django 5.1.7 on 2025-03-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('instructions', models.TextField()),
                ('servings', models.PositiveIntegerField(default=1)),
                ('ingredients', models.JSONField(default=list)),
            ],
        ),
    ]
