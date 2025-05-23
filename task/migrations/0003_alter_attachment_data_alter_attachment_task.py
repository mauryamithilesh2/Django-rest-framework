# Generated by Django 5.1.7 on 2025-04-23 13:27

import django.db.models.deletion
import task.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_attachment_tasklist_task_task_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='data',
            field=models.FileField(upload_to=task.models.GenerateAttachmentFilePath()),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='task.task'),
        ),
    ]
