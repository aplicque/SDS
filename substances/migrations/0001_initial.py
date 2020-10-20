# Generated by Django 3.1.1 on 2020-09-21 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemicals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('substance_id', models.IntegerField()),
                ('subid', models.CharField(max_length=50)),
                ('sys_id', models.CharField(blank=True, max_length=50, null=True)),
                ('report_id', models.IntegerField()),
                ('compnum', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=128)),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(max_length=255)),
                ('compnumcheck', models.IntegerField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'chemicals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Identifiers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substance_id', models.IntegerField()),
                ('type', models.CharField(max_length=12)),
                ('value', models.CharField(max_length=1024)),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'identifiers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Substances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subid', models.CharField(max_length=512)),
                ('casno', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('type', models.CharField(max_length=3)),
                ('formula', models.CharField(blank=True, max_length=1024, null=True)),
                ('formula_html', models.CharField(blank=True, max_length=1024, null=True)),
                ('pcformula', models.CharField(max_length=256)),
                ('molweight', models.FloatField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'substances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubstancesSystems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substance_id', models.IntegerField(blank=True, null=True)),
                ('system_id', models.IntegerField(blank=True, null=True)),
                ('sysid', models.CharField(blank=True, max_length=10, null=True)),
                ('subid', models.CharField(blank=True, max_length=10, null=True)),
                ('sysnmid', models.CharField(blank=True, max_length=10, null=True)),
                ('component_index', models.IntegerField(blank=True, null=True)),
                ('issolvent', models.IntegerField(blank=True, db_column='isSolvent', null=True)),
                ('comment', models.TextField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'substances_systems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Systems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sysnmid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=512)),
                ('volume', models.IntegerField()),
                ('publication_id', models.SmallIntegerField()),
                ('components', models.PositiveIntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=256, null=True)),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'systems',
                'managed': False,
            },
        ),
    ]