import csv
from email import header
from turtle import pd
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
import joblib
import os
from pathlib import Path
import numpy as np
import requests
import json
import pandas as pdd

#-----------------------------------------------------------------------

# Loading model at runtime
base_dir = Path(__file__).resolve(strict=True).parent.parent
model = os.path.join(base_dir, 'model.pkl')
joblib_model = joblib.load(model)

#-----------------------------------------------------------------------
#
def predict_new_view(request):
    V1=request.GET.get('V1')
    V2=request.GET.get('V2')
    V3=request.GET.get('V3')
    V4=request.GET.get('V4')
    V5=request.GET.get('V5')
    V6=request.GET.get('V6')
    V7=request.GET.get('V7')
    V8=request.GET.get('V8')
    V9=request.GET.get('V9')
    V10=request.GET.get('V10')
    V11=request.GET.get('V11')
    V12=request.GET.get('V12')
    V13=request.GET.get('V13')
    V14=request.GET.get('V14')
    V15=request.GET.get('V15')
    V16=request.GET.get('V16')
    V17=request.GET.get('V17')
    V18=request.GET.get('V18')
    V19=request.GET.get('V9')
    V20=request.GET.get('V20')
    V21=request.GET.get('V21')
    V22=request.GET.get('V22')
    V23=request.GET.get('V23')
    V24=request.GET.get('V24')
    V25=request.GET.get('V25')
    V26=request.GET.get('V26')
    V27=request.GET.get('V27')
    V28=request.GET.get('V28')
    V29=request.GET.get('V29')
    V30=request.GET.get('V30')
    valuess=[]
    print('322222222222222222222222222222222222222222222222222222222222222222222222222222222')
    valuess.extend((V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30))
    converted_list = [str(element) for element in valuess]
    joined_string = ",".join(converted_list)

    print(valuess)
    preds = ''
    data=valuess
    result=-1
    value="-0.35318941,  0.92823624, -1.29844323,  1.94810045, -4.50994689, 1.30580477, -0.01948593, -0.50923778, -2.64339762,  1.28354519, -2.5153557 , -4.50131481,  2.09307501, -5.41888894, -1.24701371, -3.82826818,  0.39905034, -6.36649951, -7.55096809, -4.90276667, 0.15289203,  0.25041544,  1.17803195,  1.36098858, -0.27201306, -0.3259479 ,  0.29070267,  0.84129459"
    if request.method == 'GET':
        test = np.fromstring(joined_string[1:-1], dtype=np.float, sep=',')
        test = test.reshape(1, -1)

        try:
   
            result = joblib_model.predict(test)
            if result == 0:
                preds = 'Not Fraud'
            elif result == 1:
                    preds= 'Fraud'
            else:
                preds = 'Not available'
        except ValueError:
            preds = 'Please, enter correct array data - 30 features'
        print("-------------------------------------------------------------------")
        print(preds)
        print('---------------------------------------------------------------------------')
        context = {'preds':preds, 'txt':data}
    name=[]
    rangee=[]
    value=[-0.35318941,  0.92823624, -1.29844323,  1.94810045, -4.50994689, 1.30580477, -0.01948593, -0.50923778, -2.64339762,  1.28354519, -2.5153557 , -4.50131481,  2.09307501, -5.41888894, -1.24701371, -3.82826818,  0.39905034, -6.36649951, -7.55096809, -4.90276667, 0.15289203,  0.25041544,  1.17803195,  1.36098858, -0.27201306, -0.3259479 ,  0.29070267,  0.84129459]
    for i in range(1,29):
        print(i)
        rangee.append(i)
        newval="V"+str(i)
        name.append(newval)
 
    return render(request, 'card/predict1.html',{  'value':valuess,'name':name,'preds':preds})

def new_home(request):
    name=[]
    rangee=[]
    value=[-0.35318941,  0.92823624, -1.29844323,  1.94810045, -4.50994689, 1.30580477, -0.01948593, -0.50923778, -2.64339762,  1.28354519, -2.5153557 , -4.50131481,  2.09307501, -5.41888894, -1.24701371, -3.82826818,  0.39905034, -6.36649951, -7.55096809, -4.90276667, 0.15289203,  0.25041544,  1.17803195,  1.36098858, -0.27201306, -0.3259479 ,  0.29070267,  0.84129459]
    for i in range(1,29):
        print(i)
        rangee.append(i)
        newval="V"+str(i)
        name.append(newval)
 
    return render(request, 'card/predict1.html',{  'value':value,'name':name})

# Views 
def home(request):
	txt = "-0.35318941,  0.92823624, -1.29844323,  1.94810045, -4.50994689, 1.30580477, -0.01948593, -0.50923778, -2.64339762,  1.28354519, -2.5153557 , -4.50131481,  2.09307501, -5.41888894, -1.24701371, -3.82826818,  0.39905034, -6.36649951, -7.55096809, -4.90276667, 0.15289203,  0.25041544,  1.17803195,  1.36098858, -0.27201306, -0.3259479 ,  0.29070267,  0.84129459,  0.64309425,  0.20115575"
	context = {'preds':'', 'txt':txt}
	return render(request, 'card/home.html', context)


def predict_view(request):
	result = -1
	preds = ''
	data = request.GET.get('data')
	if request.method == 'GET':
		try:
			test = np.fromstring(data[1:-1], dtype=np.float, sep=',')
			test = test.reshape(1, -1)
			result = joblib_model.predict(test)
			if result == 0:
				preds = 'Not Fraud'
			elif result == 1:
				preds= 'Fraud'
			else:
				preds = 'Not available'
		except ValueError:
			preds = 'Please, enter correct array data - 30 features'
	context = {'preds':preds, 'txt':data}
	return render(request, 'cardfraud/base.html', context)


def upload_data(request):
        result=-1
        if request.method == 'POST':
                actual_file = request.FILES['actual_file_name']
                print(actual_file)
                df=pdd.read_csv(actual_file)
                result = joblib_model.predict(df)
                value_result=[]
                for i in result:
                    if i == 0:
                        preds = 'Not Fraud'
                    elif i == 1:
                        preds= 'Fraud'
                    else:
                        preds = 'Not available'
                    value_result.append(preds)             
                print(result)   
                df['result']=value_result
                json_records = df.reset_index().to_json(orient ='records')
                data = []
                data = json.loads(json_records)
                #response=HttpResponse(content_type='text\csv')
                #write=csv.writer(response)
                i=0
                for col in df.columns:
                 i+=1
                print("====================",i)
                csv_data = df.to_csv(encoding='utf-8', index=True)
                #return HttpResponse(csv_data)
                #write.writerow(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30','result'])
                #return render(request, 'cardfraud/upload_data.html',{'df':data})
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=filename.csv'

                df.to_csv(path_or_buf=response,index=False)
                return response

        data=0
        return render(request, 'card/upload_data.html',{'df':data})

