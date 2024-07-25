from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("model", models.CharField(max_length=200)),
                ("brand", models.CharField(blank=True, max_length=200, null=True)),
                ("factory_year", models.IntegerField(blank=True, null=True)),
                ("model_year", models.IntegerField(blank=True, null=True)),
                ("value", models.FloatField()),
            ],
        ),
    ]
