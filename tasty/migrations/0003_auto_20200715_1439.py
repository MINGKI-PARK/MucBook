# Generated by Django 3.0.3 on 2020-07-15 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasty', '0002_auto_20200715_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='TastyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('score', models.PositiveIntegerField()),
                ('tasty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasty.Tasty')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Comment',
            new_name='TastyScore',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
