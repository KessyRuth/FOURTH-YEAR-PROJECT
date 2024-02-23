from django.db import models

# Create your models here.
# predictor/models.py
import joblib

class KidneyPredictor(models.Model):
    age = models.IntegerField(default=0)
    blood_pressure = models.FloatField(default=0)
    albumin = models.FloatField(default=0)
    sugar= models.FloatField(default=0)
    red_blood_cells= models.FloatField(default=0)
    pus_cell = models.FloatField(default=0)
    pus_cell_clumps = models.FloatField(default=0)
    bacteria = models.FloatField(default=0)
    blood_glucose_random  = models.FloatField(default=0)
    blood_urea = models.FloatField(default=0)
    serum_creatinine= models.FloatField(default=0)
    potassium = models.FloatField(default=0)
    white_blood_cell = models.FloatField(default=0)
    ypertension = models.FloatField(default=0)
    diabetes_mellitus  = models.FloatField(default=0)
    coronary_artery_disease = models.FloatField(default=0)
    pedal_edema = models.FloatField(default=0)
    anemia = models.FloatField(default=0)


    @staticmethod
    def load_model():
        # Load your pre-trained model using joblib
        return joblib.load('/Users/DELL/kidney_disease_prediction/predictor/kidney/kidney.pkl')

    def predict_kidney_disease(self):
        model = self.load_model()

        # Prepare input features
        input_features = [[self.age,self.blood_pressure,self.albumin,self.sugar,self.red_blood_cells,self.pus_cell,self.bacteria,self.blood_glucose_random,self.blood_urea,self.serum_creatinine,self.potassium,self.white_blood_cells,self.hypertension,self.diabetes_mellitus,self.coronary_artery,self.pedal_edema,self.anemia]]

        # Make predictions using the loaded model
        prediction = model.predict(input_features)

        return "Positive" if prediction[0] == 1 else "Negative"
