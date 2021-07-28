# Generated by Django 3.2.5 on 2021-07-26 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название позиции')),
                ('active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('status', models.CharField(choices=[('ACTIVE', 'Активен'), ('VACATION', 'Отпуск'), ('FIRED', 'Уволен')], max_length=50, verbose_name='Статус')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.position', verbose_name='Позиция')),
            ],
        ),
    ]
