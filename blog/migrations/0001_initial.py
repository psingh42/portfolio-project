# Generated by Django 2.2.17 on 2020-12-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('body', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
