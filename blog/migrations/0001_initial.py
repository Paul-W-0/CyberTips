# Generated by Django 3.0.5 on 2020-10-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('post_body', models.CharField(max_length=340)),
                ('slug', models.DateTimeField(auto_now_add=True)),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('status_choices', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
        ),
    ]