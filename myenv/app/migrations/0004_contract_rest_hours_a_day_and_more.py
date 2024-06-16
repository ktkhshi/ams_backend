# Generated by Django 5.0 on 2024-06-16 19:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_contract_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='rest_hours_a_day',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4, verbose_name='所定休憩時間'),
        ),
        migrations.AddField(
            model_name='useronprojectday',
            name='rest_hours',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True, verbose_name='休憩時間'),
        ),
        migrations.AddField(
            model_name='useronprojectday',
            name='work_ended_at',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='終了時刻'),
        ),
        migrations.AddField(
            model_name='useronprojectday',
            name='work_started_at',
            field=models.TimeField(blank=True, default=None, null=True, verbose_name='開始時刻'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='work_hours_a_day',
            field=models.DecimalField(decimal_places=2, default=8.0, max_digits=4, verbose_name='所定勤務時間'),
        ),
        migrations.AlterField(
            model_name='useronproject',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='useronproject', to='app.client', verbose_name='クライアント'),
        ),
        migrations.AlterField(
            model_name='useronproject',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='useronproject', to='app.contract', verbose_name='契約'),
        ),
        migrations.AlterField(
            model_name='useronproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useronproject', to='app.project', verbose_name='プロジェクト'),
        ),
        migrations.AlterField(
            model_name='useronproject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useronproject', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='useronprojectday',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='days', to='app.useronprojectmonth', verbose_name='ユーザプロジェクト月'),
        ),
        migrations.AlterField(
            model_name='useronprojectindex',
            name='user_on_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='idx', to='app.useronproject', verbose_name='ユーザプロジェクト'),
        ),
        migrations.AlterField(
            model_name='useronprojectindex',
            name='user_on_project_month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='idx_month', to='app.useronprojectmonth', verbose_name='ユーザプロジェクト月'),
        ),
    ]
