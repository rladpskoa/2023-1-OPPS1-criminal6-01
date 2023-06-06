# Generated by Django 4.2.1 on 2023-06-06 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('c6_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='region1',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_intro',
        ),
        migrations.AddField(
            model_name='appuser',
            name='roomID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='c6_app.room'),
        ),
        migrations.AddField(
            model_name='appuser',
            name='userID',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='room',
            name='region',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='room',
            name='roomID',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='room',
            name='roomIntro',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='id',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='name',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='room',
            name='activity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateField(max_length=45),
        ),
        migrations.AlterField(
            model_name='room',
            name='difficulty',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='fear',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='genre',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatID', models.IntegerField()),
                ('content', models.TextField()),
                ('createAT', models.DateTimeField()),
                ('roomId', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='c6_app.room')),
                ('senderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c6_app.appuser')),
            ],
        ),
    ]
