# Generated by Django 2.1.4 on 2018-12-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendmail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(default='subject', max_length=20)),
                ('mailfrom', models.CharField(default='', max_length=30)),
                ('mailto', models.CharField(default='', max_length=30)),
                ('mailtext', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.DeleteModel(
            name='Sendmail',
        ),
    ]
