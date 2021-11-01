from os import replace
from django.shortcuts import render
import pandas as pd
import openpyxl
from .models import Material,Zpp
from sqlalchemy import create_engine



def index (request):
    return render(request,'Adherence/index.html')

# _______________________

def apploadZpp(request):
    if request.method == 'POST':
        
        excel_file = request.FILES['document']
        df = pd.read_excel(excel_file)

        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(Zpp._meta.db_table,if_exists='replace', con=engine, index=False)

    return render(request,'Adherence/importZpp.html')

# _______________________

def apploadmaterial(request):
    if request.method == 'POST':
        
        excel_file = request.FILES['document']
        df = pd.read_excel(excel_file)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(Material._meta.db_table,if_exists='replace', con=engine, index=False)

    
 
    return render(request,'Adherence/importmaterial.html')