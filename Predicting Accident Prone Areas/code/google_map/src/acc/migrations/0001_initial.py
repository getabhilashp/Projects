# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-02 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accident_Index', models.CharField(max_length=100)),
                ('Location_Easting_OSGR', models.CharField(max_length=100)),
                ('Location_Northing_OSGR', models.CharField(max_length=100)),
                ('Longitude', models.CharField(max_length=100)),
                ('Latitude', models.CharField(max_length=100)),
                ('Police_Force', models.CharField(max_length=100)),
                ('Accident_Severity', models.CharField(max_length=100)),
                ('Number_of_Vehicles', models.CharField(max_length=100)),
                ('Number_of_Casualties', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
                ('Day_of_Week', models.CharField(max_length=100)),
                ('Time', models.CharField(max_length=100)),
                ('Local_Authority_District', models.CharField(max_length=100)),
                ('Local_Authority_Highway', models.CharField(max_length=100)),
                ('first_Road_Class', models.CharField(max_length=100)),
                ('first_Road_Number', models.CharField(max_length=100)),
                ('Road_Type', models.CharField(max_length=100)),
                ('Speed_limit', models.CharField(max_length=100)),
                ('Junction_Detail', models.CharField(max_length=100)),
                ('Junction_Control', models.CharField(max_length=100)),
                ('second_Road_Class', models.CharField(max_length=100)),
                ('second_Road_Number', models.CharField(max_length=100)),
                ('Pedestrian_Crossing_Human_Control', models.CharField(max_length=100)),
                ('Pedestrian_Crossing_Physical_Facilities', models.CharField(max_length=100)),
                ('Light_Conditions', models.CharField(max_length=100)),
                ('Weather_Conditions', models.CharField(max_length=100)),
                ('Road_Surface_Conditions', models.CharField(max_length=100)),
                ('Special_Conditions_at_Site', models.CharField(max_length=100)),
                ('Carriageway_Hazards', models.CharField(max_length=100)),
                ('Urban_or_Rural_Area', models.CharField(max_length=100)),
                ('Did_Police_Officer_Attend_Scene_of_Accident', models.CharField(max_length=100)),
                ('LSOA_of_Accident_Location', models.CharField(max_length=100)),
            ],
        ),
    ]
