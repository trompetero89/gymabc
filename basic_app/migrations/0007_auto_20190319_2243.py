# Generated by Django 2.1.7 on 2019-03-20 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20190319_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='PaymentsId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payments',
            name='amount',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='payments',
            name='id_afiliado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.UserProfileInfo'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='months',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(),
        ),
    ]