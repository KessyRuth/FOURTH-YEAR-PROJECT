from django.shortcuts import render

# Create your views here.
# predictor/views.py
from .models import KidneyPredictor

def predict_kidney_disease(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        blood_pressure = request.POST.get('blood_pressure')
        albumin = request.POST.get('albumin')
        sugar = request.POST.get('sugar')
        red_blood_cells = request.POST.get('red_blood_cells')
        pus_cell = request.POST.get('pus_cell')
        pus_cell_clumps = request.POST.get('pus_cell_clumps')
        bacteria = request.POST.get('bacteria')
        blood_glucose_random = request.POST.get('blood_glucose')
        blood_urea = request.POST.get('blood_urea')
        serum_creatinine = request.POST.get('serum_creatinine')
        potassium = request.POST.get('potassium')
        white_blood_cell= request.POST.get('white_blood_cell')
        ypertension = request.POST.get('ypertension')
        diabetes_mellitus = request.POST.get('diabetes_mellitus')
        coronary_artery_disease = request.POST.get('coronary_artery_disease')
        pedal_edema = request.POST.get('pedal_edema')
        anemia = request.POST.get('anemia')

        predictor_instance = KidneyPredictor(age=age, blood_pressure=blood_pressure, albumin=albumin, sugar=sugar,
                                             red_blood_cells=red_blood_cells, pus_cell=pus_cell,
                                             pus_cell_clumps=pus_cell_clumps, bacteria=bacteria,
                                             blood_glucose_random=blood_glucose_random, blood_urea=blood_urea,
                                             serum_creatinine=serum_creatinine, potassium=potassium,
                                             white_blood_cell=white_blood_cell, ypertension=ypertension,
                                             diabetes_mellitus=diabetes_mellitus,
                                             coronary_artery_disease=coronary_artery_disease, pedal_edema=pedal_edema,
                                             anemia=anemia)

        prediction = predictor_instance.predict_kidney_disease()
        return render(request, 'predictor/kidney_result.html', {'prediction': prediction})

    return render(request, 'predictor/kidney_form.html')
