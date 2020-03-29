from django.http import HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
from .forms import PinForm


file_location = "/home/mohit/Desktop/CoronaPin/Corona/Bengaluru.xls"
#file_loc_test = 
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
    detail = df.loc[df['PIN'] == pin]
    date_list = detail['Date until Quarantined at home']
    house = detail['House No']
    street = detail['Street/ Village']
    tehsil = detail['Tehsil']
    full_detail = pd.concat([date_list, house,street,tehsil], axis=1)
    full_detail_list = full_detail.values.tolist()

    print(type(detail))
    print(full_detail)
    #print(street)
    print(type(full_detail))
    
    

    if pin in pin_list:
        #count = pin_list.count(pin)
        
        
        status = "Number of people quanranitned in your area"
    else:
        status = "Invalid PIN"        
    return render(request, 'result.html',{'pin':count,'status':status,'full_detail':full_detail_list})        
