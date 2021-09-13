from django.contrib import admin
from django.db import models
from django.db.models import TextField

from DIDInv.models import DIDInventory,UserRequestReg,DIDProvison,DIDNumbers,DIDAllocation
from import_export.admin import ImportExportModelAdmin
from .choice_filter import MultiSelectFieldListFilter

class DIDAllocationModel(admin.ModelAdmin):
    list_display = ['did_allocated']

class DIDNoModel(admin.ModelAdmin):
    list_display = ['did_no']

class DIDProvisonModel(admin.ModelAdmin):
    list_display = ['number_type','country','state','city','max_count','number_format']

class UserRequestRegModel(admin.ModelAdmin):
    list_display = ['select_region','company_name','project_name','project_comments','first_name','last_name',
                    'email','street_address1','street_address2','city','state','postal_code','country','deal_status','primary_contact']
    # formfield_overrides = {models.CharField: {'widget': TextField(attrs={'size': '80'})}}
admin.site.register(UserRequestReg,UserRequestRegModel)
admin.site.register(DIDProvison,DIDProvisonModel)
admin.site.register(DIDNumbers,DIDNoModel)
admin.site.register(DIDAllocation,DIDAllocationModel)

class DropdownFilter(MultiSelectFieldListFilter):
    # template = 'admin/dropdown_filter.html'
    template = 'admin/dropdown_filter.html'


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        return (
            ('TNs', ('TNs')),
        )


class TNFilter(InputFilter):
    parameter_name = 'TNs'
    title = 'Number'

    def queryset(self, request, queryset):
        if self.value() is not None:
            uid = self.value()
            return queryset.filter(
                Q(TNs=uid)
            )

class PageAdminC(ImportExportModelAdmin):
    indexCnt = 0

    list_filter = (('Project_Account', DropdownFilter), ('Carrier', DropdownFilter), ('Type_of_Order', DropdownFilter),
                   ('Type_of_Number', DropdownFilter), ('Country', DropdownFilter), TNFilter)

    list_display = ['Project_Account', 'TNs', 'Status', 'Carrier', 'Business_Name', 'Region', 'Country', 'Data_Center',
                    'Site_Address', 'Customer_Inventory_Assignment', 'Type_of_Order', 'Type_of_Number',
                    'Order_Received_Date', 'Order_Completion_date', 'Ops_Handover_date', 'Termination_Request_Date',
                    'Termination_Closed_Date', 'TN_Quantity', 'Branch_Site_ID', 'Cost_per_DID', 'Quote_Number',
                    'Call_Forward', 'Audio_Code_Ticket', 'Comments']

    list_display_links = ['TNs']
    search_fields = ['Project_Account', 'Business_Name', 'Country', 'Site_Address', 'Type_of_Order', 'Type_of_Number',
                     'TN_Quantity', 'Carrier', 'TNs', 'ASIMS_Ticket_Number', 'Order_Completion_date']


class InventoryAdminC(PageAdminC):
    change_list_template = "admin/billing_import_b.html"

    class Meta:
        model = DIDInventory

admin.site.register(DIDInventory, InventoryAdminC)
