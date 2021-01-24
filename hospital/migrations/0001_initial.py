# Generated by Django 2.0.4 on 2018-04-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Diagnosis",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("birth_year", models.IntegerField()),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("INT", "Intern"),
                            ("RES", "Resident"),
                            ("ATT", "Attending"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "speciality",
                    models.CharField(
                        choices=[
                            ("GEN", "General"),
                            ("CAR", "Cardiothoracic"),
                            ("NEU", "Neurosurgery"),
                            ("PED", "Pediatric"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("survived", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Surgery",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_datetime", models.DateTimeField()),
                ("end_datetime", models.DateTimeField()),
                ("procedure", models.CharField(max_length=100)),
                ("doctors", models.ManyToManyField(to="hospital.Doctor")),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="hospital.Patient",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="diagnosis",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="hospital.Patient"
            ),
        ),
    ]
