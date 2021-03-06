# Generated by Django 2.1.3 on 2018-11-10 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField(blank=True)),
                ('date', models.CharField(max_length=50)),
                ('main_headline', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('url', models.TextField(blank=True)),
                ('stemming', models.TextField(blank=True)),
                ('stopword', models.TextField(blank=True)),
                ('sum_all_word', models.TextField(blank=True)),
                ('count_term', models.TextField(blank=True)),
                ('kluster', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
