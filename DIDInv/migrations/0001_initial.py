# Generated by Django 3.2.5 on 2021-09-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DIDInventory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Project_Account', models.CharField(max_length=300)),
                ('Business_Name', models.CharField(max_length=300)),
                ('Region', models.CharField(blank=True, max_length=300)),
                ('Country', models.CharField(max_length=300)),
                ('Branch_Site_ID', models.CharField(blank=True, max_length=300, null=True)),
                ('Site_Address', models.CharField(max_length=300)),
                ('Type_of_Order', models.CharField(blank=True, max_length=300, null=True)),
                ('Type_of_Number', models.CharField(max_length=300, null=True, verbose_name='Type of Number(TN/TFN)')),
                ('TN_Quantity', models.CharField(blank=True, max_length=300, null=True)),
                ('Carrier', models.CharField(max_length=300)),
                ('Data_Center', models.CharField(blank=True, max_length=300, null=True)),
                ('TNs', models.CharField(max_length=300, unique=True, verbose_name='Number(TN/TFN)')),
                ('Call_Forward', models.CharField(blank=True, max_length=300, null=True, verbose_name='TN/TFN Call Forward#(if any)')),
                ('Order_Received_Date', models.CharField(blank=True, max_length=300, null=True)),
                ('Quote_Number', models.CharField(blank=True, max_length=300, null=True)),
                ('Cost_per_DID', models.CharField(blank=True, max_length=150, null=True)),
                ('ASIMS_Ticket_Number', models.CharField(blank=True, max_length=300, null=True)),
                ('Audio_Code_Ticket', models.CharField(blank=True, max_length=300, null=True)),
                ('Order_Completion_date', models.CharField(blank=True, max_length=300, null=True)),
                ('Ops_Handover_date', models.CharField(blank=True, max_length=300, null=True)),
                ('Customer_Inventory_Assignment', models.CharField(blank=True, choices=[('Assigned', 'Assigned'), ('Reserved', 'Reserved')], max_length=300, null=True, verbose_name='Customer Inventory Assignment(Assigned/Reserved)')),
                ('Status', models.CharField(blank=True, max_length=300, null=True)),
                ('Termination_Request_Date', models.CharField(blank=True, max_length=300, null=True)),
                ('Termination_Closed_Date', models.CharField(blank=True, max_length=300, null=True)),
                ('Comments', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name_plural': 'DID Inventory',
            },
        ),
    ]
