# Generated by Django 5.1 on 2024-09-02 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_question_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='ans',
        ),
    ]
