# Generated by Django 4.1.3 on 2022-11-10 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.TextField(unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('cost', models.FloatField()),
                ('approved', models.BooleanField(default=False, help_text='Approve the album if its name is not explicit')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='artists.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('audio', models.FileField(help_text='Allowed type - .mp3, .wav', upload_to='songs/')),
                ('image', models.ImageField(default='images/def.jpg', upload_to='images/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album')),
            ],
        ),
    ]
