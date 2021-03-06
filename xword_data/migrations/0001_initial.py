# Generated by Django 2.2.16 on 2020-09-09 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=50, unique=True, verbose_name='Entry Text')),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'db_table': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255, verbose_name='Title')),
                ('date', models.DateField(verbose_name='Publication Date')),
                ('byline', models.CharField(max_length=255, verbose_name='Byline')),
                ('publisher', models.CharField(max_length=12, verbose_name='Publisher')),
            ],
            options={
                'db_table': 'puzzles',
            },
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clue_text', models.CharField(max_length=512, verbose_name='Clue Text')),
                ('theme', models.BooleanField(default=False, verbose_name='Theme')),
                ('entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='xword_data.Entry')),
                ('puzzle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='xword_data.Puzzle')),
            ],
            options={
                'db_table': 'clues',
            },
        ),
    ]
