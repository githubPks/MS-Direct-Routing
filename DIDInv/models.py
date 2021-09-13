from django.core.validators import RegexValidator
from django.db import models

INVENTORY_CHOICES = (
    ("Assigned", "Assigned"),
    ("Reserved", "Reserved"),
)

class DIDInventory(models.Model):
    id = models.IntegerField(primary_key=True)
    Project_Account = models.CharField(max_length=300)  # M
    Business_Name = models.CharField(max_length=300)  # M
    Region = models.CharField(max_length=300, blank=True)
    Country = models.CharField(max_length=300)  # M
    Branch_Site_ID = models.CharField(max_length=300, blank=True, null=True)
    Site_Address = models.CharField(max_length=300)  # M
    Type_of_Order = models.CharField(max_length=300, blank=True, null=True)
    Type_of_Number = models.CharField(
        max_length=300,
        null=True,
        verbose_name="Type of Number(TN/TFN)")  # M
    TN_Quantity = models.CharField(max_length=300, blank=True, null=True)
    Carrier = models.CharField(max_length=300)  # M
    Data_Center = models.CharField(max_length=300, blank=True, null=True)
    TNs = models.CharField(
        verbose_name="Number(TN/TFN)",
        max_length=300,  # M
        unique=True)
    Call_Forward = models.CharField(
        blank=True,
        verbose_name="TN/TFN Call Forward#(if any)",
        max_length=300,
        null=True
    )
    Order_Received_Date = models.CharField(blank=True, max_length=300, null=True)
    Quote_Number = models.CharField(max_length=300, blank=True, null=True)
    Cost_per_DID = models.CharField(max_length=150, blank=True, null=True)
    ASIMS_Ticket_Number = models.CharField(max_length=300, blank=True, null=True)
    Audio_Code_Ticket = models.CharField(max_length=300, blank=True, null=True)
    Order_Completion_date = models.CharField(max_length=300, blank=True, null=True)
    Ops_Handover_date = models.CharField(max_length=300, blank=True, null=True)
    Customer_Inventory_Assignment = models.CharField(
        max_length=300,
        choices=INVENTORY_CHOICES,
        verbose_name="Customer Inventory Assignment(Assigned/Reserved)",
        blank=True,
        null=True)
    Status = models.CharField(max_length=300, blank=True,
                              null=True)  # verbose name - is this the same as active/terminated status
    Termination_Request_Date = models.CharField(max_length=300, blank=True, null=True)
    Termination_Closed_Date = models.CharField(max_length=300, blank=True, null=True)
    Comments = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural = "DID Inventory"

    def str(self):
        return '%s' % self.TNs

    def save(self, *args, **kwargs):
        for field_name in ['Project_Account', 'Country', 'Region', 'Carrier', 'Data_Center', 'Quote_Number',
                           'Audio_Code_Ticket', 'ASIMS_Ticket_Number']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())

        #        for field_name in ['Order_Received_Date', 'Order_Completion_date', 'Ops_Handover_date', 'Termination_Request_Date', 'Termination_Closed_Date']:
        #            val = getattr(self, field_name, False)
        #            if val:
        #                val =  parser.parse(val, dayfirst=True)
        #                val = val.strftime("%d-%b-%Y")
        #                setattr(self, field_name, val)

        #         for field_name in ['Cost_per_DID']:
        #             val = getattr(self, field_name, False)
        #             if val:
        #                 val = '$' + str(val)
        #                 setattr(self, field_name, val)

        super(DIDInventory, self).save(*args, **kwargs)



region =(
    ("sel","Open this menu to select your Region"),
    # ("region1","AMRS"),
    # ("region2","APAC"),
    # ("region3","EMEA"),
    # ("region4","LATAM"),
    ("AMRS","AMRS"),
    ("APAC","APAC"),
    ("EMEA","EMEA"),
    ("LATAM","LATAM"),
)
deal = (
    ("option","open this select menu"),
    ("op1","Lead"),
    ("op2","Opportunity"),
    ("op3","In Contract"),
    ("op4","Won"),
    ("op5","Lost"),
    ("op6","On Hold"),
    ("op7","Cancelled")
)

class UserRequestReg(models.Model):
    select_region = models.CharField(max_length=64,choices=region)
    company_name = models.CharField(max_length=64,blank=True)
    project_name = models.CharField(max_length=64,blank=True)
    project_comments = models.CharField(max_length=64,blank=True)
    first_name = models.CharField(max_length=64,blank=True)
    last_name = models.CharField(max_length=64,blank=True)
    email = models.EmailField(blank=True)
    street_address1 = models.CharField(max_length=256,blank=True)
    street_address2 = models.CharField(max_length=256,blank=True)
    city = models.CharField(max_length=64,blank=True)
    state = models.CharField(max_length=64,blank=True)
    postal_code = models.IntegerField(blank=True)
    country = models.CharField(max_length=64,blank=True)
    deal_status = models.CharField(max_length=64,choices=deal)
    primary_contact = models.IntegerField(blank=True,)

    def __str__(self):
        return self.last_name

no_type = (
    ('option','open this select menu'),
    ('type1','DID'),
    ('type2','toll')
)

country = (
    ('country1','USA'),
    ('country2','UK')
)
state = (
    ('state1','NJ'),
    ('state2','NY')
)
city = (

    ('city1','NJ'),
    ('city2','NY')
)


class DIDProvison(models.Model):
    number_type = models.CharField(max_length=64,choices=no_type)
    country = models.CharField(max_length=64,choices=country)
    state = models.CharField(max_length=64,choices=state)
    city = models.CharField(max_length=64,choices=city)
    max_count = models.IntegerField()
    number_format = models.IntegerField()

    def __str__(self):
        return self.number_type


class DIDNumbers(models.Model):
    did_no = models.IntegerField()

    def __str__(self):
        return str(self.did_no)

class DIDAllocation(models.Model):
    did_allocated = models.CharField(max_length=255 ,validators=[RegexValidator(r'^\d\d\d-\d\d\d-\d\d\d\d$')])

    def __str__(self):
        return str(self.did_allocated)