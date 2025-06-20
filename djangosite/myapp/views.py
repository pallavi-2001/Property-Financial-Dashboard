from django.shortcuts import render# automatic rendering index.html file
from django.http import HttpResponse
import pandas as pd
import json

from myapp.models import Data

# Create your views here.

#Request from URL and returns reponse
def hello(request):

    #made a post request
    if (request.method=='POST'):
       show_table=True
       file=request.FILES['file']
       #always reading fresh data
       previous_data=Data.objects.all()
       previous_data.delete()

    #Uploaded a file
       #Reading entire csv file using pandas and sending to Dataframe
       df=pd.read_csv(file)
       #Converts the read data into the json formet
       json_records=df.reset_index().to_json(orient='records')
       #created a list 
       data=[]
       #Holding each row with key and value pairs
       data=json.loads(json_records)

    #data gets saved into the data base 
       for d in data:
            name=d['property_name']
            price=d['property_price']
            rent=d['property_rent']
            emi=d['emi']
            tax=d['tax']
            expense=d['other_exp']
            expense_monthly=emi+tax+expense
            income_monthly=rent - expense_monthly
            
            #data object created and assigned to dt
            dt=Data(name=name,price=price,rent=rent,emi=emi,tax=tax,expense=expense,expense_monthly=expense_monthly,income_monthly=income_monthly)
            #saving into the DB
            dt.save()
         

    #extracting data from data objects
       data_objects=Data.objects.all()     

    #packing data as context 
       context={'data_objects': data_objects,'success':True} 
    
    #passing this data into the indext.html
       return render(request,'myapp/index.html',context) 
    else:
      print('This is a GET method request')
        
    return render(request,'myapp/index.html')   