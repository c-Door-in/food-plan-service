# Generated by Django 4.0.3 on 2022-03-17 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0004_alter_subscribe_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_dishes',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favourite', to='tgbot.dish', verbose_name='Любимые блюда'),
        ),
        migrations.AddField(
            model_name='user',
            name='unloved_dishes',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unloved', to='tgbot.dish', verbose_name='Нелюбимые блюда'),
        ),
    ]