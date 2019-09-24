# Generated by Django 2.2.5 on 2019-09-23 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniprogram_api', '0002_payorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payorder',
            name='appId',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='body',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='deviceInfo',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='errCode',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='errCodeDesc',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='mchId',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='nonceStr',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='notifyUrl',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='prepayId',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='resultCode',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='returnCode',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='returnMsg',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='sign',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='signType',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='spBillCreateIp',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='timeExpire',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='timeStart',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='totalFee',
        ),
        migrations.RemoveField(
            model_name='payorder',
            name='tradeType',
        ),
    ]
