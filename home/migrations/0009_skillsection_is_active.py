# Generated by Django 5.1.7 on 2025-03-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillsection',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Skill bölümünün aktif olup olmadığını belirler.'),
        ),
    ]
