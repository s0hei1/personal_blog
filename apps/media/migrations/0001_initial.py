# Generated by Django 4.2.6 on 2023-10-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=288, null=True)),
                ('image', models.ImageField(height_field='height', upload_to='images/', width_field='width')),
                ('file_size', models.PositiveBigIntegerField(blank=True, editable=False, null=True)),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
            ],
        ),
    ]
