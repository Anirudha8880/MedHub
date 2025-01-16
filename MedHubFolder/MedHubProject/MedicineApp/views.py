from glob import magic_check

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MedicineForm
from .models import Medicine





# Create your views here.
def home_view(request):
    template_name='MedicineApp/homepage.html'
    context={}
    return render(request, template_name, context)

def add_medicine_view(request):
    form = MedicineForm()
    template_name = 'MedicineApp/add_medicine.html'
    context = {'form': form}
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, template_name, context)

def show_medicine_view(request):
    med = Medicine.objects.all()
    template_name='MedicineApp/show_medicine.html'
    context={'med':med}
    return render(request, template_name, context)

def update_medicine_view(request,i):
    med_obj = Medicine.objects.get(id=i)
    form = MedicineForm(instance=med_obj)
    if request.method=="POST":
        form = MedicineForm(request.POST,instance=med_obj)
        if form.is_valid():
            form.save()
            return redirect('/medhub/show-medicine/')
    template_name = 'MedicineApp/add_medicine.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete_medicine_view(request,i):
    med_obj = Medicine.objects.get(id=i)
    med_obj.delete()
    return redirect('/medhub/show-medicine/')

def search_medicine_view(request):
    x=""
    med = None
    if request.method == "POST":
        med_name = request.POST.get('medicine_name')
        try:
            med = Medicine.objects.get(medicine_name=med_name)
        except Medicine.DoesNotExist:
            x = "Invalid Med!!!!"
            print(x)
    template_name='MedicineApp/search_medicine.html'
    context={ 'med': med ,"msg":x}
    return render(request, template_name, context)




