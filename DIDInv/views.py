from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from DIDInv.forms import CreateUserForm,UserRequestForm,DIDProvisonForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from DIDInv.models import UserRequestReg,DIDProvison
from django.contrib.auth.decorators import login_required
from DIDInv.models import UserRequestReg,DIDProvison,DIDNumbers,DIDAllocation

def home(request):
    return render(request,'index.html')

def welcome(request):
    return render(request,'welcome.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            return redirect('registration-request')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')




def UserRequestRegistration(request):
    form = UserRequestForm
    if request.method == 'POST':
        form = UserRequestForm(request.POST)
        if form.is_valid():
            select_reg = form.cleaned_data['select_region']
            comp_name = form.cleaned_data['company_name']
            proj_name = form.cleaned_data['project_name']
            project_comm = form.cleaned_data['project_comments']
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            email =form.cleaned_data['email']
            street_add1 = form.cleaned_data['street_address1']
            street_add2 = form.cleaned_data['street_address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            postal_code = form.cleaned_data['postal_code']
            country = form.cleaned_data['country']
            deal_status = form.cleaned_data['deal_status']
            primary_contact = form.cleaned_data['primary_contact']
            instance = UserRequestReg(select_region=select_reg,company_name=comp_name,project_name=proj_name,
                                      project_comments=project_comm,first_name=f_name,last_name=l_name,email=email,
                                      street_address1=street_add1,street_address2=street_add2,city=city,state=state,
                                      postal_code=postal_code,country=country,deal_status=deal_status,primary_contact=primary_contact)
            instance.save()
            return redirect('did-prov')
        form = UserRequestForm()
    context = {'form':form}
    return render(request,'reg_request.html',context)


def didProvison(request):
    form = DIDProvisonForm
    if request.method == 'POST':
        form = DIDProvisonForm(request.POST)
        if form.is_valid():
            no_type = form.cleaned_data['number_type']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            max_count = form.cleaned_data['max_count']
            number_format = form.cleaned_data['number_format']
            instance= DIDProvison(number_type=no_type,country=country,state=state,city=city,max_count=max_count,
                                   number_format=number_format)
            instance.save()
            return redirect('final-view')
        form=DIDProvisonForm()
    context = {'form':form}
    return render(request,'did_provison.html',context)



def did_numbers(request):
    did_nos = DIDNumbers.objects.all()
    return render(request,'did_nos.html',{'did_nos':did_nos})
def didview(request):
    did_queryset = DIDProvison.objects.all()
    return render(request,'final_view.html',{'did_queryset':did_queryset})

def finalview(request):
    reg_queryset= UserRequestReg.objects.all()
    did_queryset = DIDProvison.objects.all()
    did_allocated_nos=DIDAllocation.objects.all()
    return render(request,'final.html',{'reg_queryset':reg_queryset,'did_queryset':did_queryset,'did_allocated':did_allocated_nos})
def did_allocationview(request):
    if request.method == 'POST':
        if request.POST.get('did_allocated'):
            savedata = DIDAllocation()
            savedata.did_allocated =request.POST.get('did_allocated')
            savedata.save()
            return render(request,'did_nos.html')
    else:
        return render(request,'did_nos.html')