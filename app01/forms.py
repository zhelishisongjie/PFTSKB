from django import forms
from .models import PftdDecisionIndicator

def get_surgery_type():
    surgery_type_choice = PftdDecisionIndicator.objects.raw(
        "SELECT id,surgery_type FROM `pftd_decision_indicator` GROUP BY surgery_type")
    surgery_type_array = ['']
    for i in surgery_type_choice:
        if i.surgery_type == 'NA':
            continue
        if ";" in i.surgery_type:
            temp = i.surgery_type.split(";")
            for j in temp:
                surgery_type_array.append(j.strip().title())
        elif "；" in i.surgery_type:
            temp = i.surgery_type.split("；")
            for j in temp:
                surgery_type_array.append(j.strip().title())
        else:
            surgery_type_array.append(i.surgery_type.strip().title())

    surgery_type_array1 = list(set(surgery_type_array))
    surgery_type_array1 = [item for item in surgery_type_array1 if item]
    surgery_type_array1.insert(0,'')
    return surgery_type_array1

def get_classification():
    class_choice = PftdDecisionIndicator.objects.raw(
        "SELECT id,Classification_of_fluid_therapy_Parameters as class FROM `pftd_decision_indicator` GROUP BY Classification_of_fluid_therapy_Parameters")
    class_choice_array = ['']
    for i in class_choice:
        if ";" in i.classification_of_fluid_therapy_parameters:
            temp = i.classification_of_fluid_therapy_parameters.split(";")
            class_choice_array += temp
        elif "；" in i.classification_of_fluid_therapy_parameters:
            temp = i.classification_of_fluid_therapy_parameters.split("；")
            class_choice_array += temp
        else:
            class_choice_array.append(i.classification_of_fluid_therapy_parameters)
    class_choice_array1 = list(set(class_choice_array))
    return class_choice_array1


class PFTD_Form(forms.Form):
    classification_choices = (
        ('', 'All'),
        ("Hemodynamic parameters", "Hemodynamic parameters"),
        ("Physiological factors", "Physiological factors"),
        ("Laboratory tests", "Laboratory tests"),
        ("volume loss factors", "volume loss factors"),
        ("Vital signs", "Vital signs"),
        ("Intake factors", "Intake factors"),
        ("clinical signs", "clinical signs"),
        ("Insensible losses", "Insensible losses"),
        ("Physical examinations", "Physical examinations"),
        ("Complications", "Complications"),
        ("Treatment information", "Treatment information"),
        ("Other factors", "Other factors"),

    )
    classification = forms.ChoiceField(label="Classification of parameter",
                                       widget=forms.Select(attrs={"class": "form-control", "style": "font-size: 14px",}),
                                       choices=classification_choices, required=False)

    application_choices = (
        ('', 'All'),
        ('Fluid volume estimation', 'Fluid volume estimation'),
        ("Fluid type estimation", "Fluid type estimation"),
        ("Fluid Therapy Rate Assessment", "Fluid Therapy Rate Assessment"),
        ("Transfusion Assessment", "Transfusion Assessment"),
        ("Use of vasoactive agents Assessment", "Use of vasoactive agents Assessment"),

    )
    application = forms.ChoiceField(label="Parameter Application",
                                    widget=forms.Select(attrs={"class": "form-control", "style": "font-size: 14px",}),
                                    choices=application_choices, required=False)

    age_choices = (
        ('', 'All'),
        ('Children', 'Children'),
        ("Youths", "Youths"),
        ("Adults", "Adults"),
        ("Elderly", "Elderly"),

    )
    age = forms.ChoiceField(label="Population",
                            widget=forms.Select(attrs={"class": "form-control", "style": "font-size: 14px",}),
                            choices=age_choices, required=False)

    bmi_choices = (
        ("", "All"),
        ("Underweight", "Underweight"),
        ("Normal", "Normal"),
        ("Overweight", "Overweight"),
        ("Obesity", "Obesity"),
    )

    bmi = forms.ChoiceField(label="BMI", widget=forms.Select(attrs={"class": "form-control", "style": "font-size: 14px"})
                                    , choices=bmi_choices,
                                    required=False)
    surgery_type_array = ['Cardiac surgery','Abdominal surgery','Thoracic surgery','Urological surgery',
                          'Vascular Surgery','Neurosurgery','Head and neck surgery','Orthopedic surgery',
                          'Gynecological surgery','Obstetric surgery','Pediatric surgery','Bariatric surgery','Critically ill surgery','Other surgeries']
    surgery_type_choices = (
        ('', 'All'),
        ('Cardiac surgery', 'Cardiac surgery'),
        ('Abdominal surgery', 'Abdominal surgery'),
        ('Thoracic surgery', 'Thoracic surgery'),
        ('Urological surgery',
         'Urological surgery'),
        ('Vascular Surgery', 'Vascular Surgery'),
        ('Neurosurgery', 'Neurosurgery'),
        ('Head and neck surgery', 'Head and neck surgery'),
        ('Orthopedic surgery', 'Orthopedic surgery'),
        ('Gynecological surgery', 'Gynecological surgery'),
        ('Obstetric surgery', 'Obstetric surgery'),
        ('Pediatric surgery', 'Pediatric surgery'),
        ('Bariatric surgery', 'Bariatric surgery'),
        ('Critically ill surgery', 'Critically ill surgery'),
        ('Other surgeries', 'Other surgeries'),
    )
    surgery_type = forms.ChoiceField(label="Surgical type",
                                     widget=forms.Select(attrs={"class": "form-control", "style": "font-size: 14px",}),
                                     choices=surgery_type_choices, required=False)

    asa_choices = (
        ("", "All"),
        ("I", "Ⅰ"),
        ("II", "Ⅱ"),
        ("III", "Ⅲ"),
        ("IV", "Ⅳ"),
        ("V", "Ⅴ"),
    )
    asa = forms.ChoiceField(label="ASA physical status", widget=forms.Select(attrs={"class": "form-control", "style": "font-size: 14px",}),
                                    choices=asa_choices, required=False)

    period_of_FT_chioces = (
        ("", "All"),
        ("preoperative", "preoperative"),
        ("intraoperative", "intraoperative"),
        ("postoperative", "postoperative"),

    )
    period_of_FT = forms.ChoiceField(label="Period of fluid therapy", widget=forms.Select(attrs={"class": "form-control", "style": "font-size: 14px",}),
                                             choices=period_of_FT_chioces, required=False)

    surgery_app = forms.ChoiceField(label="Surgical approach", widget=forms.Select(attrs={"class": "form-control", "style": "font-size: 14px",}), choices=(
        ('', 'All'),('Endoscopic surgery', 'Endoscopic surgery'),
        ('Open surgery', 'Open surgery'), ('Laparoscopic surgery', 'Laparoscopic surgery')), required=False)

    def __init__(self, *args, **kwargs):
        super(PFTD_Form, self).__init__(*args, **kwargs)
        # surgery_type_choices = get_surgery_type()
        # # classification_choices = get_classification()
        # # 将surgery_type_choices转换成适合用作choices的格式
        #
        # surgery_type_formatted_choices = [(item, item) for item in surgery_type_choices]
        # classification_formatted_choices = [(item, item) for item in classification_choices]
        # self.fields['surgery_type'].choices = surgery_type_formatted_choices
        # self.fields['classification'].choices = classification_formatted_choices

