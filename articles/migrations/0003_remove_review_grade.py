# Generated by Django 3.2.13 on 2022-11-02 07:57


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_remove_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='grade',
        ),
    ]
