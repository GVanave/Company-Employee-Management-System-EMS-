# Generated by Django 4.1.6 on 2023-02-05 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Full_Name", models.CharField(max_length=20)),
                ("Employee_Id", models.PositiveIntegerField()),
                ("Hourly_Rate", models.PositiveIntegerField()),
                ("Team_Lead", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Teams",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Add_Team", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Work_Arrangement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_full_time", models.BooleanField(default=False)),
                ("is_part_time", models.BooleanField(default=True)),
                ("WorkPercentage", models.FloatField(default=40)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="App_Management.employees",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="employees",
            name="Part_of_Team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="App_Management.teams"
            ),
        ),
    ]