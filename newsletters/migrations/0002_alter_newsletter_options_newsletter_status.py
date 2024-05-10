# Generated by Django 5.0.6 on 2024-05-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]