# Generated by Django 4.2.12 on 2024-06-05 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0122_parttesttemplate_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='parttesttemplate',
            name='choices',
            field=models.CharField(blank=True, help_text='Valid choices for this test (comma-separated)', max_length=5000, verbose_name='Choices'),
        ),
    ]
