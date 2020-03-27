from django.http import HttpResponseRedirect
from django.shortcuts import render
import xlrd
import pandas as pd
from .forms import PinForm


file_location = "/home/mohit/Desktop/CoronaPin/Corona/Bengaluru.xls"
df = pd.read_excel(file_location)
df.dropna(inplace = True)


def get_pin(request):
    form = PinForm()

    return render(request, 'pin.html', {'form': form})


def post_pin(request):
    if request.method == "POST":

        form = PinForm(request.POST)
        if form.is_valid():
             pin = form.cleaned_data['your_pin']

        else:
            form = PinForm()    
    
    pin_list = df["PIN"].tolist() 
    count = pin_list.count(pin)
    if pin in pin_list:
        #count = pin_list.count(pin)
        status = "Number of people quanranitned in your area"
    else:
        status = "Invalid PIN"        
    return render(request, 'result.html',{'pin':count,'status':status})        
