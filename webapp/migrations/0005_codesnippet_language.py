# Generated by Django 3.1.3 on 2021-02-03 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_codesnippetlabel'),
    ]

    operations = [
        migrations.AddField(
            model_name='codesnippet',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.language'),
        ),
    ]
