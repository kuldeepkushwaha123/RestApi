# Generated by Django 3.2.8 on 2022-01-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='zip',
            field=models.IntegerField(max_length=100),
        ),
    ]