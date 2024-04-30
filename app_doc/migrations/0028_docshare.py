# Generated by Django 2.2.12 on 2020-11-01 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0027_projecttoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True)),
                ('share_type', models.IntegerField(choices=[(0, 0), (1, 1)], default=0)),
                ('share_value', models.CharField(blank=True, max_length=10, null=True, verbose_name='分享码')),
                ('effective_time', models.IntegerField(blank=True, default=None, null=True)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_doc.Doc')),
            ],
            options={
                'verbose_name': '文档分享',
                'verbose_name_plural': '文档分享',
            },
        ),
    ]
