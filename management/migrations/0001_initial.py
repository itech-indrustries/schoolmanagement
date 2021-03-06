# Generated by Django 3.0.4 on 2020-03-18 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_teacher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dormitories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dormitory', models.CharField(max_length=20)),
                ('dormdesc', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=30)),
                ('exam_desc', models.CharField(max_length=50)),
                ('exam_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('adm_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.BigIntegerField(default=1234567890)),
                ('date_join', models.DateField()),
                ('addhar_no', models.BigIntegerField()),
                ('fathers_name', models.CharField(max_length=50)),
                ('mothers_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHERS')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('addrress', models.CharField(max_length=50)),
                ('roll_no', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('dark-edition', 'dark-edition'), ('no-theme', 'no-theme')], default='no-theme', max_length=12)),
                ('exam_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Exam_list')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addhar_no', models.BigIntegerField(blank=True, null=True)),
                ('phone_no', models.BigIntegerField(blank=True, null=True)),
                ('fathers_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('addrress', models.CharField(blank=True, max_length=50, null=True)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('e_id', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(default=0)),
                ('full_marks', models.IntegerField(default=100)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Class')),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Exam_list')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Class_schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MON', 'MONDAY'), ('TUE', 'TUESDAY'), ('WED', 'WEDNESSDAY'), ('THU', 'THURSDAY'), ('FRI', 'FRIDAY'), ('SAT', 'SATURDAY')], max_length=3)),
                ('Period', models.IntegerField(choices=[(1, 'Period 1'), (2, 'Period 2'), (3, 'Period 3'), (4, 'Period 4'), (5, 'Period 5'), (6, 'Period 6'), (7, 'Period 7'), (8, 'Period 8')])),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Class')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='dormitory_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Dormitories'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('P', 'PRESENT'), ('A', 'ABSENT')], max_length=1)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Class')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student')),
            ],
        ),
    ]
