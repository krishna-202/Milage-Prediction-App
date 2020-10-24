from django.shortcuts import render
import joblib
import pandas as pd
from .models import MilagePredictionModel

reloadModel=joblib.load("C:\\Users\Krishna P\\ML_Django\\Milage_Prediction_Django\\Milage_Prediction_Website\\Milage_Prediction_App\\models\RFModelforMPG.pkl")
# Create your views here.

def index(request):
    return render(request,'index.html')

def predict_milage(request):
    models=MilagePredictionModel()
    if request.method == "POST":

        temp=dict()
        temp['cylinders']=int(request.POST['cylinders'])
        models.cylinders=int(request.POST['cylinders'])
        temp['displacement']=int(request.POST['displacement'])
        models.displacement=int(request.POST['displacement'])
        temp['horsepower']=int(request.POST['horsepower'])
        models.horsepower=int(request.POST['horsepower'])
        temp['weight']=int(request.POST['weight'])
        models.weight=int(request.POST['weight'])
        temp['acceleration']=int(request.POST['acceleration'])
        models.acceleration=int(request.POST['acceleration'])
        temp['model year']=int(request.POST['model_year'])
        models.model_year=int(request.POST['model_year'])
        temp['origin']=int(request.POST['origin'])
        models.origin=int(request.POST['origin'])



        testData=pd.DataFrame({'x':temp}).transpose()
        scoreval=reloadModel.predict(testData)[0]

        models.predicted_value=int(scoreval)
        models.save()

        context={'score_val':scoreval}

        return render(request,'predicted_milage.html',context)
    return render(request,'predict_milage.html')
