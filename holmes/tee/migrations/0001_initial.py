# Generated by Django 2.2 on 2020-03-02 21:30

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
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('photo', models.ImageField(blank=True, upload_to='employer/%Y/%m/%d')),
                ('education', models.CharField(blank=True, choices=[('', ''), ('SSCE', 'SSCE'), ('Vocational School', 'Vocational School'), ('NCE', 'NCE'), ('OND', 'OND'), ('HND', 'HND'), ("Bachelor's Degree", "Bachelor's Degree"), ("Master's Degree", "Master's Degree"), ('MBA', 'MBA'), ('PhD', 'PhD')], max_length=25)),
                ('subjects', models.CharField(choices=[('English', 'English'), ('Mathematics', 'Mathematics'), ('Basic Science', 'Basic Science'), ('Basic Tech.', 'Basic Tech.'), ('Lit.In.Eng', 'Lit.In.Eng'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Government', 'Government'), ('Civic Edu.', 'Civic Edu.'), ('Marketing', 'Marketing'), ('C.R.S', 'C.R.S'), ('R.N.V', 'R.N.V'), ('Economics', 'Economics'), ('Agric. Sc.', 'Agric. Sc.'), ('Accounting', 'Accounting'), ('Computer Edu.', 'Computer Edu.'), ('Data.processing.', 'Data.processing.'), ('Others.', 'Others.')], max_length=30)),
                ('position', models.CharField(choices=[('Activity', 'Activity'), ('Nursey', 'Nursery'), ('Primary', 'Primary'), ('Junior Secondary', 'Junior Secondary'), ('Senior Secondary', 'Senior Secondary')], max_length=30)),
                ('resume', models.FileField(upload_to='documents')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]