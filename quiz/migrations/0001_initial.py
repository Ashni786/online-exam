# Generated by Django 3.0.5 on 2020-06-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('catagory', models.CharField(choices=[('ComputerScience', 'Computer Science'), ('Histroy', 'Histroy'), ('Science', 'Science'), ('ArtandLiterature', 'Art and Literature'), ('Geography', 'Geography'), ('Music', 'Music '), ('movies', 'Movies'), ('maths', 'Maths'), ('generalknowledge', 'GeneralKnowledge')], max_length=20)),
            ],
            options={
                'ordering': ('-catagory',),
            },
        ),
    ]
