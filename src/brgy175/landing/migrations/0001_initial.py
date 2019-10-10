# Generated by Django 2.2.5 on 2019-10-10 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('residents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=50)),
                ('father_address', models.CharField(max_length=100)),
                ('father_age', models.IntegerField()),
                ('father_occupation', models.CharField(max_length=30)),
                ('father_mobile', models.CharField(max_length=11)),
                ('father_precint', models.CharField(max_length=30)),
                ('father_salary', models.IntegerField()),
                ('mother_name', models.CharField(max_length=50)),
                ('mother_address', models.CharField(max_length=100)),
                ('mother_age', models.IntegerField()),
                ('mother_occupation', models.CharField(max_length=30)),
                ('mother_mobile', models.CharField(max_length=11)),
                ('mother_precint', models.CharField(max_length=30)),
                ('mother_salary', models.IntegerField()),
                ('resident_scholarship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='residents.Resident')),
            ],
        ),
        migrations.CreateModel(
            name='IndigencyForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccswd', models.BooleanField(default=False)),
                ('dswd_medical', models.BooleanField(default=False)),
                ('in_birth_certificate', models.BooleanField(default=False)),
                ('solo_parent', models.BooleanField(default=False)),
                ('philhealth', models.BooleanField(default=False)),
                ('burial_assistance', models.BooleanField(default=False)),
                ('medical_assistance', models.BooleanField(default=False)),
                ('financial_assistance', models.BooleanField(default=False)),
                ('educational_assistance', models.BooleanField(default=False)),
                ('dswd_financial', models.BooleanField(default=False)),
                ('resident_indigency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='residents.Resident')),
            ],
        ),
        migrations.CreateModel(
            name='IDForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_person', models.CharField(max_length=50)),
                ('con_person_address', models.CharField(max_length=100)),
                ('con_person_relationsip', models.CharField(max_length=20)),
                ('con_person_mobile', models.CharField(max_length=11)),
                ('resident_idform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='residents.Resident')),
            ],
        ),
        migrations.CreateModel(
            name='ClearanceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bail_bond', models.BooleanField(default=False)),
                ('bank', models.BooleanField(default=False)),
                ('cl_birth_certificate', models.BooleanField(default=False)),
                ('mayors_permit', models.BooleanField(default=False)),
                ('meralco', models.BooleanField(default=False)),
                ('personal_id', models.BooleanField(default=False)),
                ('sss', models.BooleanField(default=False)),
                ('excavation_permit', models.BooleanField(default=False)),
                ('travel', models.BooleanField(default=False)),
                ('loan', models.BooleanField(default=False)),
                ('indigency', models.BooleanField(default=False)),
                ('building_permit', models.BooleanField(default=False)),
                ('senior_citizen', models.BooleanField(default=False)),
                ('local_employment', models.BooleanField(default=False)),
                ('maynilad', models.BooleanField(default=False)),
                ('barangay_id', models.BooleanField(default=False)),
                ('tricycle_franchise', models.BooleanField(default=False)),
                ('lipat_bahay', models.BooleanField(default=False)),
                ('pnp', models.BooleanField(default=False)),
                ('postal_id', models.BooleanField(default=False)),
                ('business_license', models.BooleanField(default=False)),
                ('motor_loan', models.BooleanField(default=False)),
                ('bir', models.BooleanField(default=False)),
                ('nha', models.BooleanField(default=False)),
                ('resident_clearance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='residents.Resident')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPermit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barangay_permit', models.BooleanField(default=False)),
                ('city_permit', models.BooleanField(default=False)),
                ('business_address', models.CharField(max_length=100)),
                ('business_name', models.CharField(max_length=50)),
                ('resident_business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='residents.Resident')),
            ],
        ),
        migrations.CreateModel(
            name='BurialForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('burial_name', models.CharField(max_length=50)),
                ('burial_address', models.CharField(max_length=100)),
                ('burial_relation', models.CharField(max_length=20)),
                ('burial_birth', models.DateField()),
                ('burial_death', models.DateField()),
                ('burial_interment_place', models.CharField(max_length=50)),
                ('burial_interment_date', models.DateField()),
                ('resident_burial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='residents.Resident')),
            ],
        ),
    ]
