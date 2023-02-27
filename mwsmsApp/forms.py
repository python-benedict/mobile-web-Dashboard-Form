from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["fullname", "mobile_number", "eaten", "eaten_report", "slept", "slept_report", "active", "kid_fight", "fight_report", "health_problem", "health_problem_report", "toilet", "toilet_report", "class_participation", "class_participation_report", "kid_attitude","academic_performance","kid_interest","teacher_name","general_comment", ]
    labels = {'fullname': "Full Name", "mobile_number": "Mobile Number","eaten":"Did The Kid Eat", "eaten_report":"Report On What The Kid Eat","slept":"slept", "slept_report":"Report On How The Kid Slept","active":"active","kid_fight":"kid_fight","fight_report":"Did The Kid Fought","health_problem":"Any Health Issues?","health_problem_report":"Report On Kid Health Issues","toilet":"Did The Kid Went To Toilet","toilet_report":"Report On The Kid Toilet","class_participation":"Class Participation Report Of The Kid","kid_attitude":"How is the kid Attitude in School","academic_performance":"How is the kid's Academic Performance","kid_interest":"What is the interest","teacher_name":"Name Of Teacher Filling The Form","general_comment":"Any General Comment?"}