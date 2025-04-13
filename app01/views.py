import json

import itertools as it
from django.db.models import Count
from django import forms
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.shortcuts import render, HttpResponse
from app01.serializer import *
from django.http import JsonResponse
# Create your views here.
from app01.models import *
from .forms import PFTD_Form
from django.utils.safestring import mark_safe


def home(request):
    if request.method == 'GET':
        # 获取分类下的条目数#
        data_st = PftdDecisionIndicator.objects.raw(
            "SELECT id, Application as app,COUNT(*) as nums FROM `pftd_decision_indicator` GROUP BY Application,id"
        )

        print(data_st)
        data_map = {}
        app_array = []
        for record in data_st:
            if ";" in record.app:
                split_temp = record.app.split(";")
                for item in split_temp:
                    if item.strip().title() not in app_array:

                        app_array.append(item.strip().title())
                        data_map[item.strip().title()] = int(record.nums)
                    else:
                        data_map[item.strip().title()] += int(record.nums)
            elif "；" in record.app:
                split_temp = record.app.split("；")
                for item in split_temp:
                    if item.strip().title() not in app_array:

                        app_array.append(item.strip().title())
                        data_map[item.strip().title()] = int(record.nums)
                    else:
                        data_map[item.strip().title()] += int(record.nums)
            elif "," in record.app:
                split_temp = record.app.split(",")
                for item in split_temp:
                    if item.strip().title() not in app_array:

                        app_array.append(item.strip().title())
                        data_map[item.strip().title()] = int(record.nums)
                    else:
                        data_map[item.strip().title()] += int(record.nums)
            else:
                app_array.append(record.app.strip().title())
                # 将分类作为键，数量作为值添加到字典中
                data_map[record.app.strip().title()] = record.nums

        cls = ['Treatment information', 'Physical examinations', 'Intake factors', 'Insensible losses', 'Complications',
               'Clinical signs', 'Other factors', 'Vital signs', 'Volume loss factors', 'Laboratory tests',
               'Physiological factors', 'Hemodynamic parameters']
        # cls = ['Physiological factors', 'volume loss factors', 'Vital signs', 'Hemodynamic parameters',
        #        'Laboratory tests', 'Other factors', 'clinical signs', 'Intake factors', 'Complications',
        #        'Insensible losses', 'Physical examinations', 'Treatment information']
        ft_array = []
        # ft_array = ['preoperative','intraoperative', 'postoperative' ]
        res = []
        cls_map = {}
        temp = 0
        for i in cls:
            cls_map[i] = temp
            temp += 1
        data_tt = PftdDecisionIndicator.objects.raw(
            "SELECT id, Classification_of_fluid_therapy_Parameters as clas,Period_of_fluid_therapy as ft,COUNT(*) as nums FROM `pftd_decision_indicator` GROUP BY Classification_of_fluid_therapy_Parameters,Period_of_fluid_therapy,id"
        )
        for i in data_tt:
            if ";" in i.ft:
                split_temp = i.ft.split(";")
                for item in split_temp:
                    if item not in ft_array:
                        dic_temp = {"name": item, "type": 'bar', "stack": 'total',
                                    #             "label": {
                                    #     "show": 'true',
                                    # },
                                    "emphasis": {
                                        "focus": 'series'
                                    }, "data": [0] * len(cls)}
                        ft_array.append(item)
                        dic_temp["data"][cls_map[i.clas.capitalize()]] = int(i.nums)
                        res.append(dic_temp)
                    else:
                        for j in res:
                            if j["name"] == item:
                                j["data"][cls_map[i.clas.capitalize()]] += int(i.nums)
            else:
                name = i.ft
                dic_temp = {"name": name, "type": 'bar', "stack": 'total',
                            #             "label": {
                            #     "show": 'true',
                            # },
                            "emphasis": {
                                "focus": 'series'
                            }, "data": [0] * len(cls)}

                if name not in ft_array:
                    ft_array.append(name)
                    dic_temp["data"][cls_map[i.clas.capitalize()]] = int(i.nums)
                    res.append(dic_temp)

                else:
                    for j in res:
                        if j["name"] == name:
                            j["data"][cls_map[i.clas.capitalize()]] += int(i.nums)

        # print(data_map)
        # print(res)
        return render(request, "home.html",
                      {"pie": json.dumps(data_map), "res": json.dumps(res)})
        # return render(request, "home.html")


def home_select(request, id):
    if id == 1:
        rows = []
        queryset = PftdDecisionIndicator.objects.raw(
            "SELECT * from pftd_decision_indicator where Application LIKE '%%Fluid volume estimation%%'")
        for obj in queryset:
            rows.append({'id': obj.id, 'Pid': obj.pid, 'parameters': obj.parameters,
                         'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                         'application': obj.application, 'surgery_type': obj.surgery_type,
                         'period_of_fluid_therapy': obj.period_of_fluid_therapy,
                         'group_name': obj.group_name,
                         'pmid': obj.pmid})
        data = {'total': len(queryset), 'rows': rows}
        return render(request, "details_application.html", {'data': json.dumps(data), 'id': 'Fluid volume estimation'})
    elif id == 2:
        rows = []
        queryset = PftdDecisionIndicator.objects.raw(
            "SELECT * from pftd_decision_indicator where Application LIKE '%%Fluid type estimation%%'")
        for obj in queryset:
            rows.append({'id': obj.id, 'Pid': obj.pid, 'parameters': obj.parameters,
                         'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                         'application': obj.application, 'surgery_type': obj.surgery_type,
                         'period_of_fluid_therapy': obj.period_of_fluid_therapy,
                         'group_name': obj.group_name,
                         'pmid': obj.pmid})
        data = {'total': len(queryset), 'rows': rows}
        return render(request, "details_application.html", {'data': json.dumps(data), 'id': 'Fluid volume estimation'})
    elif id == 3:
        rows = []
        queryset = PftdDecisionIndicator.objects.raw(
            "SELECT * from pftd_decision_indicator where Application LIKE '%%Fluid therapy rate assessment%%'")
        for obj in queryset:
            rows.append({'id': obj.id, 'Pid': obj.pid, 'parameters': obj.parameters,
                         'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                         'application': obj.application, 'surgery_type': obj.surgery_type,
                         'period_of_fluid_therapy': obj.period_of_fluid_therapy,
                         'group_name': obj.group_name,
                         'pmid': obj.pmid})
        data = {'total': len(queryset), 'rows': rows}
        return render(request, "details_application.html", {'data': json.dumps(data), 'id': 'Fluid volume estimation'})

    elif id == 4:
        rows = []
        queryset = PftdDecisionIndicator.objects.raw(
            "SELECT * from pftd_decision_indicator where Application LIKE '%%transfusion assessment%%'")
        for obj in queryset:
            rows.append({'id': obj.id, 'Pid': obj.pid, 'parameters': obj.parameters,
                         'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                         'application': obj.application, 'surgery_type': obj.surgery_type,
                         'period_of_fluid_therapy': obj.period_of_fluid_therapy,
                         'group_name': obj.group_name,
                         'pmid': obj.pmid})
        data = {'total': len(queryset), 'rows': rows}
        return render(request, "details_application.html", {'data': json.dumps(data), 'id': 'Fluid volume estimation'})
    else:
        rows = []
        queryset = PftdDecisionIndicator.objects.raw(
            "SELECT * from pftd_decision_indicator where Application LIKE '%%use of vasoactive agents assessment%%'")
        for obj in queryset:
            rows.append({'id': obj.id, 'Pid': obj.pid, 'parameters': obj.parameters,
                         'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                         'application': obj.application, 'surgery_type': obj.surgery_type,
                         'period_of_fluid_therapy': obj.period_of_fluid_therapy,
                         'group_name': obj.group_name,
                         'pmid': obj.pmid})
        data = {'total': len(queryset), 'rows': rows}
        return render(request, "details_application.html", {'data': json.dumps(data), 'id': 'Fluid volume estimation'})


def preview(request):

    return render(request, "research_preview.html")
def publication(request):

    return render(request, "research_publication.html")
def study(request):

    return render(request, "research_study.html")

def study_details(request,id):
    queryset = Pftd.objects.get(id=id)
    return render(request, "details_study_information.html", {'queryset': queryset})

def patient(request):
    return render(request, "baseline_patient.html")

def surgery(request):
    return render(request, "baseline_surgery.html")

def disease(request):
    return render(request, "baseline_disease.html")

def complication(request):
    return render(request, "outcome_complication.html")
def hospital(request):
    return render(request, "outcome_len_hos.html")
def icu(request):
    return render(request, "outcome_ICU.html")
def mortality(request):
    return render(request, "outcome_Mortality.html")

def outcome_details(request,id):
    queryset = Pftd.objects.get(id=id)
    return render(request, "details_outcomes.html", {'queryset': queryset})

def get_pftd_data(request,num):
    if request.method == 'GET':
        #preview information
        if num == 1:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,Title,Levels_of_Recommendation,Grades_of_Evidence  FROM `pftd` GROUP BY pmid,Title,group_name")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'pmid': obj.pmid, 'Title': obj.Title,
                             'Key_points': obj.Key_points,
                             'Grades_of_Evidence': obj.Grades_of_Evidence,
                             'Levels_of_Recommendation': obj.Levels_of_Recommendation})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 2:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,`Year`,Title,Journal,Reference FROM `pftd` GROUP BY pmid")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'pmid': obj.pmid, 'Title': obj.Title,
                             'Year': obj.Year,'Reference': obj.Reference,
                             'Journal': obj.Journal})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 3:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,group_name,Study_Design,Region,Sample_Size,Year FROM `pftd` GROUP BY pmid,group_name")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'Year': obj.Year, 'pmid': obj.pmid, 'group_name': obj.group_name,
                             'Study_Design': obj.Study_Design, 'Region': obj.Region,
                             'Sample_Size': obj.Sample_Size})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 4:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,Gender,Age,ASA_physical_status,BMI,Race,group_name FROM `pftd` GROUP BY pmid,ASA_physical_status")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'group_name': obj.group_name, 'pmid': obj.pmid, 'Gender': obj.Gender,
                             'Age': obj.Age, 'ASA_physical_status': obj.ASA_physical_status,
                             'BMI': obj.BMI,'Race': obj.Race})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 5:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,group_name,ASA_physical_status,Surgical_approach,surgery_type,surgical_site FROM `pftd` GROUP BY pmid,group_name,ASA_physical_status,surgical_site")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'pmid': obj.pmid, 'group_name': obj.group_name,
                             'ASA_physical_status': obj.ASA_physical_status, 'Surgical_approach': obj.Surgical_approach,
                             'surgery_type': obj.surgery_type,'surgical_site': obj.surgical_site})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 6:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,group_name,Disease,Comorbidity FROM `pftd` GROUP BY pmid,group_name,Disease,Comorbidity")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'pmid': obj.pmid, 'group_name': obj.group_name,
                             'Disease': obj.Disease, 'Comorbidity': obj.Comorbidity})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 7:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,group_name,Effect_comparison,Complications_name,Result1,Statictics1 FROM `pftd` GROUP BY pmid,group_name,Effect_comparison,Complications_name,Result1,Statictics1")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'pmid': obj.pmid, 'group_name': obj.group_name,
                             'Effect_comparison': obj.Effect_comparison, 'Complications_name': obj.Complications_name,'Result1': obj.Result1,'Statictics1': obj.Statictics1})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 8:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,group_name,Effect_comparison,Outcome_name1,Result2,Statictics2 FROM `pftd` GROUP BY pmid,group_name,Effect_comparison,Outcome_name1,Result2,Statictics2")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'pmid': obj.pmid, 'group_name': obj.group_name,
                             'Effect_comparison': obj.Effect_comparison, 'Outcome_name1': obj.Outcome_name1,
                             'Result2': obj.Result2, 'Statictics2': obj.Statictics2})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 9:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,group_name,Effect_comparison,Outcome_name2,Result3,Statictics3 FROM `pftd` GROUP BY pmid,group_name,Effect_comparison,Outcome_name2,Result3,Statictics3")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'pmid': obj.pmid, 'group_name': obj.group_name,
                             'Effect_comparison': obj.Effect_comparison, 'Outcome_name2': obj.Outcome_name2,
                             'Result3': obj.Result3, 'Statictics3': obj.Statictics3})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        if num == 10:
            queryset = Pftd.objects.raw(
                "SELECT id,pmid,group_name,Effect_comparison,Outcome_name3,Result4,Statictics4 FROM `pftd` GROUP BY pmid,group_name,Effect_comparison,Outcome_name3,Result4,Statictics4")
            # total = PftdDecisionIndicator.objects.count()
            # queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'pmid': obj.pmid, 'group_name': obj.group_name,
                             'Effect_comparison': obj.Effect_comparison, 'Outcome_name3': obj.Outcome_name3,
                             'Result4': obj.Result4, 'Statictics4': obj.Statictics4})

            data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')



def analysis(request):
    return render(request, "analysis/analysis_py.html")


def contact(request):
    return render(request, "Contact us.html")


def help(request):
    return render(request, "help.html")


'''
 Search.html
'''


def get_queryset_or_none(value, field_name):
    if value:
        return Q(**{field_name + "__icontains": value})
    return None


def getlist(request, id):
    if request.method == 'POST':
        if id == 2:
            data = json.loads(request.body)
            classification = data.get('classification').get("value") if isinstance(data.get('classification'),
                                                                                   dict) else None
            application = data.get('application').get("value") if isinstance(data.get('application'), dict) else None
            surgeryType = data.get('surgeryType').get("value") if isinstance(data.get('surgeryType'), dict) else None
            Period_ft = data.get('Period_ft').get("value") if isinstance(data.get('Period_ft'), dict) else None

            print(classification, application, surgeryType, Period_ft)
            if surgeryType == 'Other surgeries':
                surgeries = ["Non-cardiac surgery",
                             "post-endoscopic retrograde cholangiopancreatography(ERCP)", "urgent PCI", "Oncosurgery",
                             "NA",
                             "other surgery", "other surgeries"]
                # query = Q()
                # for surgery in surgeries:
                #     condition = get_queryset_or_none(surgery, 'surgery_type')
                #     if condition:
                #         query |= condition  # 使用OR操作符连接条件
                # print(query)
                queryset = Pftd.objects.filter(surgery_type__in=surgeries)
                rows = []
                for obj in queryset:
                    rows.append({'id': obj.id,
                                 #'IFTP': obj.IFTP,
                                 #'IFTP_subgroup': obj.IFTP_subgroup,
                                 'Period_of_fluid_therapy': obj.Period_of_fluid_therapy,
                                 'liquid_treatment': obj.liquid_treatment,
                                 'Fluid_name': obj.Fluid_name,
                                 'Fluid_type': obj.Fluid_type, 'surgery_type': obj.surgery_type,
                                 'Dose': obj.Dose, 'Rate': obj.Rate,
                                 'Duration': obj.Duration})

                data = {'total': queryset.count(), 'totalNotFiltered': queryset.count(), 'rows': rows}
                return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
            else:
                query = Q()
                for value, field_name in zip([classification, application, surgeryType, Period_ft],
                                             ['classification_of_fluid_therapy_parameters', 'application',
                                              'surgery_type',
                                              'Period_of_fluid_therapy']):
                    condition = get_queryset_or_none(value, field_name)
                    if condition:
                        query &= condition

                print(query)
                queryset = Pftd.objects.filter(query)
                # total = PftdDecisionIndicator.objects.filter(query).count()
                # queryset = PftdDecisionIndicator.objects.all().filter(
                #     classification_of_fluid_therapy_parameters=classification, application=application,
                #     surgery_type=surgeryType)
                rows = []
                for obj in queryset:
                    rows.append({'id': obj.id,
                                 #'IFTP': obj.IFTP,
                                 #'IFTP_subgroup': obj.IFTP_subgroup,
                                 'Period_of_fluid_therapy': obj.Period_of_fluid_therapy,
                                 'liquid_treatment': obj.liquid_treatment,
                                 'Fluid_name': obj.Fluid_name,
                                 'Fluid_type': obj.Fluid_type, 'surgery_type': obj.surgery_type,
                                 'Dose': obj.Dose, 'Rate': obj.Rate,
                                 'Duration': obj.Duration})

                data = {'total': queryset.count(), 'totalNotFiltered': queryset.count(), 'rows': rows}
                return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')

        else:
            data = json.loads(request.body)
            classification = data.get('classification').get("value") if isinstance(data.get('classification'),
                                                                                   dict) else None
            application = data.get('application').get("value") if isinstance(data.get('application'), dict) else None
            surgeryType = data.get('surgeryType').get("value") if isinstance(data.get('surgeryType'), dict) else None
            Period_ft = data.get('Period_ft').get("value") if isinstance(data.get('Period_ft'), dict) else None

            print(classification, application, surgeryType, Period_ft)
            if surgeryType == 'Other surgeries':
                surgeries = ["Non-cardiac surgery",
                             "post-endoscopic retrograde cholangiopancreatography(ERCP)", "urgent PCI", "Oncosurgery", "NA",
                             "other surgery", "other surgeries"]
                # query = Q()
                # for surgery in surgeries:
                #     condition = get_queryset_or_none(surgery, 'surgery_type')
                #     if condition:
                #         query |= condition  # 使用OR操作符连接条件
                # print(query)
                queryset = PftdDecisionIndicator.objects.filter(surgery_type__in=surgeries)
                rows = []
                for obj in queryset:
                    rows.append({'id': obj.id,
                                 #'IFTP': obj.IFTP,
                                 #'IFTP_subgroup': obj.IFTP_subgroup,
                                 'Pid': obj.pid, 'parameters': obj.parameters,
                                 'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                                 'application': obj.application, 'surgery_type': obj.surgery_type,
                                 'period_of_fluid_therapy': obj.period_of_fluid_therapy, 'group_name': obj.group_name,
                                 'pmid': obj.pmid})

                data = {'total': queryset.count(), 'totalNotFiltered': queryset.count(), 'rows': rows}
                return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
            else:
                query = Q()
                for value, field_name in zip([classification, application, surgeryType, Period_ft],
                                             ['classification_of_fluid_therapy_parameters', 'application', 'surgery_type',
                                              'period_of_fluid_therapy']):
                    condition = get_queryset_or_none(value, field_name)
                    if condition:
                        query &= condition

                print(query)
                queryset = PftdDecisionIndicator.objects.filter(query)
                # total = PftdDecisionIndicator.objects.filter(query).count()
                # queryset = PftdDecisionIndicator.objects.all().filter(
                #     classification_of_fluid_therapy_parameters=classification, application=application,
                #     surgery_type=surgeryType)
                rows = []
                for obj in queryset:
                    rows.append({'id': obj.id,
                                 #'IFTP': obj.IFTP,
                                 #'IFTP_subgroup': obj.IFTP_subgroup,
                                 'Pid': obj.pid, 'parameters': obj.parameters,
                                 'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                                 'application': obj.application, 'surgery_type': obj.surgery_type,
                                 'period_of_fluid_therapy': obj.period_of_fluid_therapy, 'group_name': obj.group_name,
                                 'pmid': obj.pmid})

                data = {'total': queryset.count(), 'totalNotFiltered': queryset.count(), 'rows': rows}
                return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')

        # list1 = data.split(";")
        # type1 = list1[1]
        # filter_data = list1[0]
        # if type1 == "1":
        #     total = PftdDecisionIndicator.objects.filter(classification_of_fluid_therapy_parameters=filter_data).count()
        #     queryset = PftdDecisionIndicator.objects.all().filter(
        #         classification_of_fluid_therapy_parameters=filter_data)
        #     rows = []
        #     for obj in queryset:
        #         rows.append({'id': obj.id, 'parameters': obj.parameters,
        #                      'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
        #                      'application': obj.application, 'surgery_type': obj.surgery_type,
        #                      'period_of_fluid_therapy': obj.period_of_fluid_therapy, 'group_name': obj.group_name,
        #                      'pmid': obj.pmid})
        #
        #     data = {'total': total, 'totalNotFiltered': total, 'rows': rows}
        #     return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        # elif type1 == "2":
        #     # filter_data1 = []
        #     # filter_data1.append("Use of vasoactive agents Assessment")
        #     # filter_data1.append(filter_data)
        #     # print(filter_data1)
        #     total = PftdDecisionIndicator.objects.filter(application__icontains=filter_data).count()
        #     queryset = PftdDecisionIndicator.objects.all().filter(
        #         application__icontains=filter_data)
        #     rows = []
        #     for obj in queryset:
        #         rows.append({'id': obj.id, 'parameters': obj.parameters,
        #                      'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
        #                      'application': obj.application, 'surgery_type': obj.surgery_type,
        #                      'period_of_fluid_therapy': obj.period_of_fluid_therapy, 'group_name': obj.group_name,
        #                      'pmid': obj.pmid})
        #
        #     data = {'total': total, 'totalNotFiltered': total, 'rows': rows}
        #     return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        # else:
        #     total = PftdDecisionIndicator.objects.filter(surgery_type=filter_data).count()
        #     queryset = PftdDecisionIndicator.objects.all().filter(
        #         surgery_type=filter_data)
        #     rows = []
        #     for obj in queryset:
        #         rows.append({'id': obj.id, 'parameters': obj.parameters,
        #                      'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
        #                      'application': obj.application, 'surgery_type': obj.surgery_type,
        #                      'period_of_fluid_therapy': obj.period_of_fluid_therapy, 'group_name': obj.group_name,
        #                      'pmid': obj.pmid})
        #
        #     data = {'total': total, 'totalNotFiltered': total, 'rows': rows}
        #     return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
    #     data = json.loads(request.body.decode())
    #     print(data)

    if request.method == 'GET':
        if id == 2:
            total = Pftd.objects.count()
            queryset = Pftd.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id,
                             'IFTP': obj.IFTP,
                             'IFTP_subgroup': obj.IFTP_subgroup,
                             'Period_of_fluid_therapy': obj.Period_of_fluid_therapy, 'liquid_treatment': obj.liquid_treatment,
                             'Fluid_name': obj.Fluid_name,
                             'Fluid_type': obj.Fluid_type, 'surgery_type': obj.surgery_type,
                             'Dose': obj.Dose, 'Rate': obj.Rate,
                             'Duration': obj.Duration})

            data = {'total': total, 'totalNotFiltered': total, 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        else:
            # page_size = int(request.GET['pageSize'])
            # page_number = int(request.GET['pageNumber'])

            # queryset = PftdDecisionIndicator.objects.order_by('id')[(page_number - 1) * page_size:page_number * page_size]
            total = PftdDecisionIndicator.objects.count()
            queryset = PftdDecisionIndicator.objects.all()
            rows = []
            for obj in queryset:
                rows.append({'id': obj.id, 'Pid': obj.pid, 'parameters': obj.parameters,
                             'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                             'application': obj.application, 'surgery_type': obj.surgery_type,
                             'period_of_fluid_therapy': obj.period_of_fluid_therapy, 'group_name': obj.group_name,
                             'pmid': obj.pmid})

            data = {'total': total, 'totalNotFiltered': total, 'rows': rows}

            return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')


def search(request,id):
    queryset = PftdDecisionIndicator.objects.all()

    queryset2 =Pftd.objects.all()
    surgery_type_choice = PftdDecisionIndicator.objects.raw(
        "SELECT id,surgery_type FROM `pftd_decision_indicator` GROUP BY surgery_type")
    # class_choice = PftdDecisionIndicator.objects.raw(
    #     "SELECT id,Classification_of_fluid_therapy_Parameters as class,count(*)as nums FROM `pftd_decision_indicator` GROUP BY Classification_of_fluid_therapy_Parameters ORDER BY nums DESC")
    # app_choice_query = PftdDecisionIndicator.objects.raw(
    #     "SELECT id,Application,count(*) as nums  FROM `pftd_decision_indicator` GROUP BY Application ORDER BY nums DESC")
    # period_ft = PftdDecisionIndicator.objects.raw(
    #     "SELECT id,Period_of_fluid_therapy as ft FROM `pftd_decision_indicator` GROUP BY Period_of_fluid_therapy")
    app_choice = ['Fluid volume estimation', 'Fluid type estimation', 'Fluid therapy rate assessment',
                  'Transfusion assessment', 'Use of vasoactive agents Assessment']
    class_choice_array = ['Hemodynamic parameters', 'Physiological factors', 'Laboratory tests', 'Volume loss factors',
                          'Vital signs', 'Intake factors', 'Clinical signs', 'Insensible losses',
                          'Physical examinations', 'Complications', 'Treatment information', 'Other factors']
    surgery_type_array = ['Cardiac surgery', 'Abdominal surgery', 'Thoracic surgery', 'Urological surgery',
                          'Vascular Surgery', 'Neurosurgery', 'Head and neck surgery', 'Orthopedic surgery',
                          'Gynecological surgery', 'Obstetric surgery', 'Pediatric surgery', 'Bariatric surgery',
                          'Critically ill surgery', 'Other surgeries']
    period_ft_array = ['Preoperative', 'Intraoperative', 'Postoperative']
    # for i in class_choice:
    #     if ";" in i.classification_of_fluid_therapy_parameters:
    #         temp = i.classification_of_fluid_therapy_parameters.split(";")
    #         class_choice_array += temp
    #     elif "；" in i.classification_of_fluid_therapy_parameters:
    #         temp = i.classification_of_fluid_therapy_parameters.split("；")
    #         class_choice_array += temp
    #     else:
    #         class_choice_array.append(i.classification_of_fluid_therapy_parameters)
    # class_choice_array1 = list(set(class_choice_array))

    # for i in app_choice_query:
    #     if ";" in i.application:
    #         temp = i.application.split(";")
    #         app_choice += temp
    #     elif "；" in i.application:
    #         temp = i.application.split("；")
    #         app_choice += temp
    #     elif ", " in i.application:
    #         temp = i.application.split(", ")
    #         app_choice += temp
    #     elif "," in i.application:
    #         temp = i.application.split(",")
    #         app_choice += temp
    #     else:
    #         app_choice.append(i.application)
    # app_choice1 = list(set(app_choice))

    # for i in surgery_type_choice:
    #     if i.surgery_type == 'NA':
    #         continue
    #     if ";" in i.surgery_type:
    #         temp = i.surgery_type.split(";")
    #         for j in temp:
    #             surgery_type_array.append(j.strip().title())
    #     elif "；" in i.surgery_type:
    #         temp = i.surgery_type.split("；")
    #         for j in temp:
    #             surgery_type_array.append(j.strip().title())
    #     else:
    #         surgery_type_array.append(i.surgery_type.strip().title())
    #
    # surgery_type_array1 = list(set(surgery_type_array))
    # surgery_type_array1 = [item for item in surgery_type_array1 if item]
    #
    # print(surgery_type_array1)

    # for i in period_ft:
    #     if ";" in i.ft:
    #         temp = i.ft.split(";")
    #         period_ft_array += temp
    #     elif "；" in i.ft:
    #         temp = i.ft.split("；")
    #         period_ft_array += temp
    #     else:
    #         period_ft_array.append(i.ft)
    # period_ft_array1 = list(set(period_ft_array))
    if id == 1:

        return render(request, "search1.html",
                  {"queryset": queryset, "st": surgery_type_array, "class": class_choice_array, "app": app_choice,
                   'period_ft': period_ft_array})
    else:
        return render(request, "search2.html",
                      {"queryset": queryset2, "st": surgery_type_array, "class": class_choice_array, "app": app_choice,
                       'period_ft': period_ft_array})

def getsearchdetails(request, id):
    queryset = PftdDecisionIndicator.objects.get(id=id)
    return render(request, "details_pftd.html", {'queryset': queryset})

def getdetails(request, id):
    #queryset = PftdDecisionIndicator.objects.get(id=id)
    queryset = Pftd.objects.get(id=id)
    return render(request, "details.html", {'queryset': queryset})




def getIFTPdetails(request, IFTP):
    queryset = Pftd.objects.filter(IFTP=IFTP)

    rows = []
    for obj in queryset:
        rows.append({'IFTP': obj.IFTP, 'IFTP_subgroup': obj.IFTP_subgroup,
                     'id': obj.id,
                     'application': obj.Application1, 'surgery_type': obj.surgery_type,
                     'period_of_fluid_therapy': obj.Period_of_fluid_therapy,
                     'pmid': obj.pmid, 'reference': obj.Reference})

    data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}
    return render(request, "details_IFTP.html", {'queryset': queryset, 'data': json.dumps(data)})

def getIFTPsubdetails(request, IFTP_subgroup):
    queryset = Pftd.objects.filter(IFTP_subgroup=IFTP_subgroup)

    rows = []
    for obj in queryset:
        rows.append({'IFTP': obj.IFTP, 'IFTP_subgroup': obj.IFTP_subgroup,
                     'id': obj.id,
                     'application': obj.Application1, 'surgery_type': obj.surgery_type,
                     'period_of_fluid_therapy': obj.Period_of_fluid_therapy,
                     'pmid': obj.pmid, 'reference': obj.Reference})

    data = {'total': len(queryset), 'totalNotFiltered': len(queryset), 'rows': rows}
    return render(request, "details_IFTP_subgroup.html", {'queryset': queryset, 'data': json.dumps(data)})


def getdetails_PID(request, id):
    queryset = PftdDecisionIndicator.objects.filter(pid=id).first()
    queryset2 = PftdDecisionIndicator.objects.raw(
        "select * from pftd_decision_indicator where PID = " + "'" + id + "'" + " GROUP BY pmid")
    # print(id)
    rows = []
    for obj in queryset2:
        rows.append({'id': obj.id,
                     'application': obj.application, 'surgery_type': obj.surgery_type,
                     'period_of_fluid_therapy': obj.period_of_fluid_therapy,
                     'pmid': obj.pmid, 'reference': obj.reference})

    data = {'total': len(queryset2), 'totalNotFiltered': len(queryset2), 'rows': rows}
    # print(data)
    return render(request, "details_PID.html", {'queryset': queryset, 'data': json.dumps(data)})


'''
 tool.html
'''


# def change_size(value):
#     if 1 <= value <= 10:
#         return 10
#     elif 10 < value <= 20:
#         return 15
#     elif 20 < value <= 40:
#         return 25
#     elif 40 < value <= 70:
#         return 35
#     elif 70 < value <= 100:
#         return 45
#     elif 100 < value <= 200:
#         return 55
#     elif 200 < value <= 300:
#         return 65
#     elif 300 < value <= 400:
#         return 75
#     else:
#         return 85
#
#
# def graph_PFTD(queryst, queryperiod_ft, query_para, links_st_pft, links_pft_para):
#     nodes = []
#     links = []
#     categories = ['surgery_type', 'Period_FT', 'parameter']
#     type_graph = []
#     for i in categories:
#         type_dic = {"name": i}
#         type_graph.append(type_dic)
#
#     '''
#     获取节点信息共3种节点
#     '''
#     st_array = []
#     for i in queryst:
#         if ";" in i.surgery_type:
#             temp = i.surgery_type.split(";")
#             for j in temp:
#                 if j.strip().title() not in st_array:
#                     st_array.append(j.strip().title())
#                     node_dic = {}
#                     node_dic["id"] = j.strip().title() + "-st"
#                     node_dic["name"] = j.strip().title()
#                     node_dic["value"] = i.value
#                     node_dic["category"] = "surgery_type"
#                     node_dic["symbolSize"] = change_size(i.value)
#                     nodes.append(node_dic)
#                 else:
#                     for k in nodes:
#                         if k["name"] == j.strip().title():
#                             k["value"] += int(i.value)
#                             k["symbolSize"] = change_size(k["value"])
#         else:
#             if i.surgery_type.strip().title() not in st_array:
#                 st_array.append(i.surgery_type.strip().title())
#                 node_dic = {}
#                 node_dic["id"] = i.surgery_type.strip().title() + "-st"
#                 node_dic["name"] = i.surgery_type.strip().title()
#                 node_dic["value"] = i.value
#                 node_dic["category"] = "surgery_type"
#                 node_dic["symbolSize"] = change_size(i.value)
#                 nodes.append(node_dic)
#             else:
#                 for k in nodes:
#                     if k["name"] == i.surgery_type.strip().title():
#                         k["value"] += int(i.value)
#                         k["symbolSize"] = change_size(k["value"])
#     period_array = []
#     for i in queryperiod_ft:
#         if ";" in i.period_of_fluid_therapy:
#             temp = i.period_of_fluid_therapy.split(";")
#             for j in temp:
#                 if j.strip().title() not in period_array:
#                     period_array.append(j.strip().title())
#                     node_dic = {}
#                     node_dic["id"] = j.strip().title() + "-pft"
#                     node_dic["name"] = j.strip().title()
#                     node_dic["value"] = i.value
#                     node_dic["category"] = "Period_FT"
#                     node_dic["symbolSize"] = change_size(i.value)
#                     nodes.append(node_dic)
#                 else:
#                     for k in nodes:
#                         if k["name"] == j.strip().title():
#                             k["value"] += int(i.value)
#                             k["symbolSize"] = change_size(k["value"])
#         else:
#             if i.period_of_fluid_therapy.strip().title() not in period_array:
#                 period_array.append(i.period_of_fluid_therapy.strip().title())
#                 node_dic = {}
#                 node_dic["id"] = i.period_of_fluid_therapy.strip().title() + "-pft"
#                 node_dic["name"] = i.period_of_fluid_therapy.strip().title()
#                 node_dic["value"] = i.value
#                 node_dic["category"] = "Period_FT"
#                 node_dic["symbolSize"] = change_size(i.value)
#                 nodes.append(node_dic)
#             else:
#                 for k in nodes:
#                     if k["name"] == i.period_of_fluid_therapy.strip().title():
#                         k["value"] += int(i.value)
#                         k["symbolSize"] = change_size(k["value"])
#     para_array = []
#     for i in query_para:
#         if i.parameters.strip().title() not in para_array:
#             para_array.append(i.parameters.strip().title())
#             node_dic = {}
#             node_dic["id"] = i.parameters.strip().title() + "-para"
#             node_dic["name"] = i.parameters.strip().title()
#             node_dic["value"] = i.value
#             node_dic["category"] = "parameter"
#             node_dic["symbolSize"] = change_size(i.value)
#             nodes.append(node_dic)
#         else:
#             for k in nodes:
#                 if k["name"] == i.parameters.strip().title():
#                     k["value"] += int(i.value)
#                     k["symbolSize"] = change_size(k["value"])
#
#     # 去重
#     node_ids = set()
#     for node in nodes:
#         node_id = node['id']
#         if node_id in node_ids:
#             print(f"Duplicate node id found: {node_id}")
#         node_ids.add(node_id)
#     # nodes = [dict(t) for t in set([tuple(d.items()) for d in nodes])]
#
#     '''
#     整理2种节点间关系
#     '''
#
#     # 'surgery_type - Period_FT'
#     for i in links_st_pft:
#         if (";" in i.surgery_type) and (";" not in i.period_of_fluid_therapy):
#             temp = i.surgery_type.split(";")
#             for j in temp:
#                 link_dic = {}
#                 link_dic["source"] = j.strip().title() + "-st"
#                 link_dic["target"] = i.period_of_fluid_therapy.strip().title() + "-pft"
#                 links.append(link_dic)
#         elif (";" in i.period_of_fluid_therapy) and (";" not in i.surgery_type):
#             temp = i.period_of_fluid_therapy.split(";")
#             for j in temp:
#                 link_dic = {}
#                 link_dic["source"] = i.surgery_type.strip().title() + "-st"
#                 link_dic["target"] = j.strip().title() + "-pft"
#                 links.append(link_dic)
#         elif (";" in i.period_of_fluid_therapy) and (';' in i.surgery_type):
#             temp = i.surgery_type.split(';')
#             temp2 = i.period_of_fluid_therapy.split(';')
#             for j in temp:
#                 for k in temp2:
#                     link_dic = {}
#                     link_dic["source"] = j.strip().title() + "-st"
#                     link_dic["target"] = k.strip().title() + "-pft"
#                     links.append(link_dic)
#         else:
#             link_dic = {}
#             link_dic["source"] = i.surgery_type.strip().title() + "-st"
#             link_dic["target"] = i.period_of_fluid_therapy.strip().title() + "-pft"
#             links.append(link_dic)
#
#     # 'Period_FT -parameter'
#     for i in links_pft_para:
#         if ";" in i.period_of_fluid_therapy:
#             temp = i.period_of_fluid_therapy.split(";")
#             for j in temp:
#                 link_dic = {}
#                 link_dic["source"] = j.strip().title() + "-pft"
#                 link_dic["target"] = i.parameters.strip().title() + "-para"
#                 links.append(link_dic)
#         else:
#             link_dic = {}
#             link_dic["source"] = i.period_of_fluid_therapy.strip().title() + "-pft"
#             link_dic["target"] = i.parameters.strip().title() + "-para"
#             links.append(link_dic)
#
#     unique_set = set(tuple(sorted(d.items())) for d in links)
#     unique_list = [dict(t) for t in unique_set]
#     # 去重操作
#     # link_pairs = set()
#     # for link in links:
#     #     link_pair = (link['source'], link['target'])
#     #     # if link_pair in link_pairs:
#     #     #     print(f"Duplicate links found: {link_pair}")
#     #     link_pairs.add(link_pair)
#     #
#     # print(links)
#
#     return nodes, unique_list, type_graph
#
#
# def create_node(name, value=None, children=None):
#     node = {'name': name}
#     if value is not None:
#         node['value'] = 1
#     if children is not None:
#         node['children'] = children
#     return node
#
#
# def build_forest(data):
#     trees = {}  # 使用字典来存储不同的树，key为surgery_type
#     for entry in data:
#         surgery_type = entry[0]  # 假设每个entry的第一个元素是surgery_type
#         if surgery_type not in trees:
#             trees[surgery_type] = create_node(surgery_type)  # 创建一个新树的根节点
#
#         current_node = trees[surgery_type]  # 从对应的树开始
#         for name in entry[1:]:  # 从第二个元素开始，因为第一个是surgery_type
#             found_child = None
#             if 'children' in current_node:
#                 for child in current_node['children']:
#                     if child['name'] == name:
#                         found_child = child
#                         break
#             if found_child is None:
#                 new_child = create_node(name)
#                 current_node.setdefault("children", []).append(new_child)
#                 current_node = new_child
#             else:
#                 current_node = found_child
#         current_node['value'] = 1
#     return list(trees.values())  # 将字典中所有树的根节点作为列表返回

def update_links1(links, source, target, value):
    # existing_link = next((link for link in links if link['source'] == source and link['target'] == target), None)
    # if existing_link:
    #
    #     # 如果存在，累加value
    #     existing_link['value'] += value
    # else:
    #     # 如果不存在，添加新的链接
    #     links.append({'source': source, 'target': target, 'value': value})
    for link in links:
        if link['source'] == source and link['target'] == target:
            link['value'] += value
            return
    else:
        links.append({'source': source, 'target': target, 'value': value})


def dfs(visited, graph, node, parent, recursion_stack):
    visited[node] = True
    recursion_stack[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            if dfs(visited, graph, neighbour, node, recursion_stack):
                return True
        elif recursion_stack[neighbour]:
            print(f"Found a cycle: {parent} -> {node} -> {neighbour}")
            return True
    recursion_stack[node] = False
    return False


def detect_cycles(links):
    graph = {}
    visited = {}
    recursion_stack = {}

    # Construct the graph
    for link in links:
        source = link['source']
        target = link['target']
        if source not in graph:
            graph[source] = []
        if target not in graph:
            graph[target] = []
        graph[source].append(target)

    # Initialize visited and recursion stack
    for node in graph.keys():
        visited[node] = False
        recursion_stack[node] = False

    # Call the recursive helper function to detect cycle in different DFS trees
    for node in graph.keys():
        if not visited[node]:
            if dfs(visited, graph, node, None, recursion_stack):
                return True

    return False


def clean_and_split1(value, field,filter_options=None):
    """清理字符串并按分号分割，返回标题格式的列表。"""
    # if not value:
    #     return []
    # return [item.strip().title() for item in value.split(';') if item.strip()]
    if not value:
        return []
    if field == 'parameters':
        items = [item.strip() for item in value.split(';') if item.strip()]
    else:
        items = [item.strip().title() for item in value.split(';') if item.strip()]
    if filter_options:
        # 将filter_options中的值也转换为标题格式以确保匹配
        # filter_options_set = set(filter_options)
        filter_options = [option.strip().title() for option in filter_options]
        items = [item for item in items if item in filter_options]
    return items


def process_entries1(search_res, field1, field2, links, category=None, options2=None):
    """处理条目并更新链接。"""
    # for entry in search_res:
    #     items1 = clean_and_split(getattr(entry, field1),options)
    #     items2 = clean_and_split(getattr(entry, field2),options)
    #
    #     if not items1:
    #         items1 = ['Unknown']  # 为缺失数据提供默认值
    #     if not items2:
    #         items2 = ['Unknown']
    #
    #     for item1 in items1:
    #         for item2 in items2:
    #             update_links(links, item1, item2, entry.value)
    if category==[]:
        category = None
    if options2 == []:
        options2 = None
    for entry in search_res:
        # filter_options1 = options2 if category == field1 else None
        # filter_options2 = options2 if category == field2 else None
        # if filter_options1 is None and filter_options2 is None:
        #     break
        items1 = clean_and_split1(getattr(entry, field1), field1,category)
        items2 = clean_and_split1(getattr(entry, field2), field2,options2)

        if not items1:
            items1 = ['Unknown']  # 为缺失数据提供默认值
        if not items2:
            items2 = ['Unknown']

        for item1 in items1:
            for item2 in items2:
                update_links1(links, item1, item2, entry.value)


def tool(request):
    if request.method == "POST":
        # print(request.POST)
        form = PFTD_Form(data=request.POST)
        if form.is_valid():
            age = form.cleaned_data.get("age")
            bmi = form.cleaned_data.get("bmi")
            # print(bmi)
            # print(bmi is None)
            classification = form.cleaned_data.get("classification")
            application = form.cleaned_data.get("application")
            surgery_app = form.cleaned_data.get("surgery_app")
            period_of_FT = form.cleaned_data.get("period_of_FT")
            surgery_type = form.cleaned_data.get("surgery_type")
            asa = form.cleaned_data.get("asa")

            if (len(classification) == 0) and (len(age) == 0) and (len(bmi) == 0) and (len(application) == 0) and (
                    len(surgery_app) == 0) and (len(period_of_FT) == 0) and (len(surgery_type) == 0) and (
                    len(asa) == 0):
                queryset1 = PftdDecisionIndicator.objects.all()
                # queryst = PftdDecisionIndicator.objects.raw(
                #     "SELECT id, surgery_type, COUNT(*) as value from pftd_decision_indicator GROUP BY surgery_type")
                # queryperiod_ft = PftdDecisionIndicator.objects.raw(
                #     "SELECT id, period_of_fluid_therapy, COUNT(*) as value from pftd_decision_indicator GROUP BY period_of_fluid_therapy")
                # query_para = PftdDecisionIndicator.objects.raw(
                #     "SELECT id, parameters, COUNT(*) as value from pftd_decision_indicator GROUP BY parameters")
                # links_st_pft = PftdDecisionIndicator.objects.raw(
                #     "SELECT id, surgery_type, Period_of_fluid_therapy from pftd_decision_indicator GROUP BY surgery_type, Period_of_fluid_therapy")
                # links_pft_para = PftdDecisionIndicator.objects.raw(
                #     "SELECT id, Period_of_fluid_therapy,Parameters from pftd_decision_indicator GROUP BY Period_of_fluid_therapy,Parameters")
                # nodes, links, type_graph = graph_PFTD(queryst, queryperiod_ft, query_para, links_st_pft, links_pft_para)
                rows = []
                for obj in queryset1:
                    rows.append({'id': obj.id, 'Pid': obj.pid, 'parameters': obj.parameters,
                                 'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                                 'application': obj.application, 'surgery_type': obj.surgery_type,
                                 'period_of_fluid_therapy': obj.period_of_fluid_therapy, 'group_name': obj.group_name,
                                 'pmid': obj.pmid})
                data1 = {'total': len(queryset1), 'rows': rows}

                data = []  # 存储节点数据
                links = []  # 存储关系数据
                first_level = PftdDecisionIndicator.objects.exclude(surgery_type='NA').values('surgery_type').distinct()
                for i in first_level:
                    if ";" in i["surgery_type"]:
                        temp = i["surgery_type"].split(";")
                        for j in temp:
                            data.append(j)
                    elif "；" in i["surgery_type"]:
                        temp = i["surgery_type"].split("；")
                        for j in temp:
                            data.append(j)
                    elif "," in i["surgery_type"]:
                        temp = i["surgery_type"].split(",")
                        for j in temp:
                            data.append(j)
                    elif ", " in i["surgery_type"]:
                        temp = i["surgery_type"].split(", ")
                        for j in temp:
                            data.append(j)
                    else:
                        data.append(i["surgery_type"])
                    # dic = {}
                    # dic['name'] = i.surgery_type
                    # data.append(dic)
                second_level = PftdDecisionIndicator.objects.exclude(period_of_fluid_therapy='NA').values(
                    'period_of_fluid_therapy').distinct()
                for i in second_level:
                    if ";" in i["period_of_fluid_therapy"]:
                        temp = i["period_of_fluid_therapy"].split(";")
                        for j in temp:
                            data.append(j)
                    else:
                        data.append(i["period_of_fluid_therapy"])
                third_level = PftdDecisionIndicator.objects.exclude(application='NA').values('application').distinct()
                for i in third_level:
                    if ";" in i["application"]:
                        temp = i["application"].split(";")
                        for j in temp:
                            data.append(j)
                    elif "；" in i["application"]:
                        temp = i["application"].split("；")
                        for j in temp:
                            data.append(j)
                    elif "," in i["application"]:
                        temp = i["application"].split(",")
                        for j in temp:
                            data.append(j)
                    elif ", " in i["application"]:
                        temp = i["application"].split(", ")
                        for j in temp:
                            data.append(j)
                    else:
                        data.append(i["application"])

                forth_level = PftdDecisionIndicator.objects.exclude(parameters='NA').values('parameters').distinct()
                for i in forth_level:
                    if ";" in i["parameters"]:
                        temp = i["parameters"].split(";")
                        for j in temp:
                            data.append(j)
                    else:
                        data.append(i["parameters"])
                data = [item.strip().title() for item in data if item.strip()]

                data = list(set(data))
                # 获取各level间的关系数据

                test1 = PftdDecisionIndicator.objects.raw(
                    "SELECT id, surgery_type,period_of_fluid_therapy,count(*) as value FROM pftd_decision_indicator GROUP BY surgery_type,Period_of_fluid_therapy HAVING surgery_type != 'NA'")
                for entry in test1:
                    surgery_types = [surgery.strip().title() for surgery in entry.surgery_type.split(';')]
                    therapies = [therapy.strip().title() for therapy in entry.period_of_fluid_therapy.split(';')]

                    if ';' in entry.surgery_type and ';' not in entry.period_of_fluid_therapy:
                        for surgery in surgery_types:
                            update_links(links, surgery, entry.period_of_fluid_therapy.strip().title(), entry.value)
                    elif ';' not in entry.surgery_type and ';' in entry.period_of_fluid_therapy:
                        for therapy in therapies:
                            update_links(links, entry.surgery_type.strip().title(), therapy, entry.value)
                    elif ';' in entry.surgery_type and ';' in entry.period_of_fluid_therapy:
                        for surgery in surgery_types:
                            for therapy in therapies:
                                update_links(links, surgery, therapy, entry.value)
                    else:
                        update_links(links, entry.surgery_type.strip().title(),
                                     entry.period_of_fluid_therapy.strip().title(),
                                     entry.value)

                test2 = PftdDecisionIndicator.objects.raw(
                    "SELECT id, period_of_fluid_therapy,Application ,count(*) as value FROM pftd_decision_indicator GROUP BY Period_of_fluid_therapy,Application HAVING Application != 'NA'")
                for entry in test2:
                    applications = [application.strip().title() for application in entry.application.split(';')]
                    therapies = [therapy.strip().title() for therapy in entry.period_of_fluid_therapy.split(';')]

                    if ';' in entry.period_of_fluid_therapy and ';' not in entry.application:
                        for therapy in therapies:
                            update_links(links, therapy, entry.application.strip().title(), entry.value)
                    elif ';' not in entry.period_of_fluid_therapy and ';' in entry.application:
                        for app in applications:
                            update_links(links, entry.period_of_fluid_therapy.strip().title(), app, entry.value)
                    elif ';' in entry.application and ';' in entry.period_of_fluid_therapy:
                        for therapy in therapies:
                            for application in applications:
                                update_links(links, therapy, application, entry.value)
                    else:
                        update_links(links, entry.period_of_fluid_therapy.strip().title(),
                                     entry.application.strip().title(),
                                     entry.value)

                test3 = PftdDecisionIndicator.objects.raw(
                    "SELECT id,Application,Parameters,count(*) as value FROM pftd_decision_indicator GROUP BY Application,Parameters HAVING Application != 'NA' and Parameters != 'NA'")
                for entry in test3:
                    applications = [application.strip().title() for application in entry.application.split(';')]
                    parameters = [para.strip().title() for para in entry.parameters.split(';')]

                    if ';' in entry.application and ';' not in entry.parameters:
                        for application in applications:
                            update_links(links, application, entry.parameters.strip().title(), entry.value)
                    elif ';' not in entry.application and ';' in entry.parameters:
                        for para in parameters:
                            update_links(links, entry.application.strip().title(), para, entry.value)
                    elif ';' in entry.application and ';' in entry.parameters:
                        for application in applications:
                            for para in parameters:
                                update_links(links, application, para, entry.value)
                    else:
                        update_links(links, entry.application.strip().title(), entry.parameters.strip().title(),
                                     entry.value)
                # print(data)
                # return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
                return render(request, "tool.html",
                              {"form": form, "data": json.dumps(data1), 'nodes': data, 'links': links})
            else:
                arr = []
                category = []
                option_dict = {'classification_of_fluid_therapy_parameters': [],
                               'application': [], 'age': [], 'bmi': [],'surgery_type':[],
                               'surgical_approach': [], 'period_of_fluid_therapy': [],
                               'ASA_physical_status': []}

                if classification:
                    classification_temp = "( classification_of_fluid_therapy_parameters" + " LIKE '%%" + classification + "%%' )"
                    arr.append(classification_temp)
                    option_dict['classification_of_fluid_therapy_parameters'].append(classification)
                if application:
                    application_temp = "( application" + " LIKE '%%" + application + "%%' )"
                    arr.append(application_temp)
                    category.append('application')
                    option_dict['application'].append(application)
                if age:
                    age_temp = "( age" + " LIKE '%%" + age + "%%' )"
                    arr.append(age_temp)
                    option_dict['age'].append(age)
                if bmi:
                    bmi_temp = "( bmi" + " LIKE '%%" + bmi + "%%' )"
                    arr.append(bmi_temp)
                    option_dict['bmi'].append(bmi)
                if surgery_type:
                    if surgery_type == 'Other surgeries':
                        surgery_type_temp = "(surgery_type LIKE '%%Non-cardiac surgery%%' OR surgery_type LIKE '%%post-endoscopic retrograde cholangiopancreatography(ERCP)%%'" \
                                            "OR surgery_type LIKE '%%urgent PCI%%'OR surgery_type LIKE '%%Oncosurgery%%'" \
                                            "OR surgery_type = 'NA'OR surgery_type LIKE '%%other surgery%%'" \
                                            "OR surgery_type LIKE '%%other surgeries%%' )"
                        category.append('surgery_type')
                        option_dict['surgery_type'].append("Non-cardiac surgery")
                        option_dict['surgery_type'].append("post-endoscopic retrograde cholangiopancreatography(ERCP)")
                        option_dict['surgery_type'].append("urgent PCI")
                        option_dict['surgery_type'].append("Oncosurgery")
                        option_dict['surgery_type'].append("NA")
                        option_dict['surgery_type'].append("other surgery")
                        option_dict['surgery_type'].append("other surgeries")

                        # option_dict['surgery_type'] = ["Non-cardiac surgery",
                        #                                "post-endoscopic retrograde cholangiopancreatography(ERCP)",
                        #                                "urgent PCI", "Oncosurgery", "NA", "other surgery",
                        #                                "other surgeries"]
                    elif surgery_type == 'Cardiac surgery':
                        surgery_type_temp = "( surgery_type= '" + surgery_type + "')"
                        category.append('surgery_type')
                        option_dict['surgery_type'].append(surgery_type)
                    else:
                        surgery_type_temp = "( surgery_type" + " LIKE '%%" + surgery_type + "%%' )"
                        category.append('surgery_type')
                        option_dict['surgery_type'].append(surgery_type)
                    arr.append(surgery_type_temp)
                if surgery_app:
                    surgery_app_temp = "( surgical_approach" + " LIKE '%%" + surgery_app + "%%' )"
                    arr.append(surgery_app_temp)
                    option_dict['surgical_approach'].append(surgery_app)
                if period_of_FT:
                    period_of_FT_temp = "( period_of_fluid_therapy" + " LIKE '%%" + period_of_FT + "%%' )"
                    arr.append(period_of_FT_temp)
                    category.append('period_of_fluid_therapy')
                    option_dict['period_of_fluid_therapy'].append(period_of_FT)
                if asa:
                    asa_temp = "( ASA_physical_status" + " LIKE '%%" + asa + "%%' )"
                    arr.append(asa_temp)
                    option_dict['ASA_physical_status'].append(asa)
                search_temp_arr = []

                for j in range(len(arr), 0, -1):
                    for e in it.combinations(arr, j):
                        search_temp_demo = " and ".join(e)
                        search_temp_arr.append(search_temp_demo)
                # search_temp_arr.append(search_base_temp)
                # print(search_temp_arr)
                # print(option_dict)

                rows = []
                queryset = []
                raw_out = []
                links = []
                nodes = []

                sign = 1  # 初始化 sign 为 1，假设第一个查询为空
                first_query = True  # 用于标记是否是第一个查询
                # print(option_dict)
                # print(len(option_dict))
                for search_temp1 in search_temp_arr:

                    queryset1 = PftdDecisionIndicator.objects.raw(
                        "select * from pftd_decision_indicator where " + search_temp1)

                    if queryset1:
                        print("select * from pftd_decision_indicator where " + search_temp1)
                        print(option_dict)
                        # 只有在第一次查询时，才修改 sign 值
                        if first_query:
                            sign = 0  # 第一个查询有结果时，sign 设置为 0，表示不需要弹窗
                        search_temps = []
                        if option_dict:
                            new_dict = {key: option_dict[key] for key in
                                        ['surgery_type', 'period_of_fluid_therapy', 'application'] if
                                        key in option_dict}
                            # for category, options in option_dict.items():
                            #     if options:  # 确保options是非空列表
                            #         # 对于当前category的每个option值，构造 LIKE 子句并用 OR 连接
                            #         if options[0] == 'Cardiac surgery':
                            #             category_conditions = [f"{category} = '{options[0]}'"]
                            #         elif len(options) > 1:
                            #             category_conditions = [
                            #                 f"{category} = '{option}'" if option == 'NA' else f"{category} LIKE '%%{option}%%'"
                            #                 for option in options]
                            #         else:
                            #             category_conditions = [f"{category} LIKE '%%{options[0]}%%'"]
                            #
                            #         # 将当前category的所有条件用 OR 连接起来，并用括号括起
                            #         search_temps.append(f"({' OR '.join(category_conditions)})")
                            #
                            # # 将不同category的条件用 AND 连接
                            # search_temp = ' AND '.join(search_temps)
                            # search_res = PftdDecisionIndicator.objects.raw("SELECT id, surgery_type,Period_of_fluid_therapy,Application,Parameters,count(*) as value FROM pftd_decision_indicator"
                            #     " where  id = 180"
                            #     " GROUP BY surgery_type,Period_of_fluid_therapy,Application,Parameters HAVING surgery_type != 'NA' ")
                            search_res = PftdDecisionIndicator.objects.raw(
                                "SELECT id, surgery_type,Period_of_fluid_therapy,Application,Parameters,count(*) as value FROM pftd_decision_indicator"
                                " where " + search_temp1 +
                                " GROUP BY surgery_type,Period_of_fluid_therapy,Application,Parameters HAVING surgery_type != 'NA' ")
                            # for category, options in option_dict.items():

                            # filter_options = [option.strip().title() for option in options]

                            process_entries1(search_res, 'surgery_type', 'period_of_fluid_therapy', links,
                                             option_dict['surgery_type'],
                                             option_dict['period_of_fluid_therapy'])
                            process_entries1(search_res, 'period_of_fluid_therapy', 'application', links,
                                             option_dict['period_of_fluid_therapy'],
                                             option_dict['application'])
                            process_entries1(search_res, 'application', 'parameters', links, option_dict['application'],
                                             [])

                            #         # 处理不同的字段组合
                            # for link in links:
                            #     link['value'] = link['value'] // len(search_temp1.split('and'))
                            print(links)
                            nodes = list(set([link['source'] for link in links] + [link['target'] for link in links]))
                            print(nodes)

                        # else:
                        #     search_res1 = PftdDecisionIndicator.objects.raw(
                        #         "SELECT id, surgery_type,Period_of_fluid_therapy,Application,Parameters,count(*) as value FROM pftd_decision_indicator"
                        #         " where " + search_temp1 +
                        #         " GROUP BY surgery_type,Period_of_fluid_therapy,Application,Parameters HAVING surgery_type != 'NA' ")
                        #     for category, options in option_dict.items():
                        #         filter_options = [option.strip().title() for option in options]
                        #         process_entries(search_res1, 'surgery_type', 'period_of_fluid_therapy', links, category,
                        #                         filter_options)
                        #         process_entries(search_res1, 'period_of_fluid_therapy', 'application', links, category,
                        #                         filter_options)
                        #         process_entries(search_res1, 'application', 'parameters', links, category, filter_options)
                        #     #         # 处理不同的字段组合
                        #     nodes = list(set([link['source'] for link in links] + [link['target'] for link in links]))
                        queryset = queryset1
                        break
                    # 标记已经完成第一个查询
                    first_query = False
                        # for item in queryset1:
                        #     surgeryType = item.surgery_type
                        #     PT = item.period_of_fluid_therapy
                        #     applicate = item.application
                        #     para = item.parameters

                    # if queryset1:
                    #     form = ana_sankey_form(data=request.POST)
                    #     if form.is_valid():
                    #         category = form.cleaned_data.get("category")
                    #         options2 = request.POST.getlist("name")
                    #         name = ",".join(options2)
                    #         res = "——【" + name + "】"
                    #
                    #         search_temp = ""
                    #         if len(options2) == 1:
                    #             search_temp += category + " LIKE '%%" + options2[-1] + "%%'"
                    #
                    #
                    #         else:
                    #             for i in range(0, len(options2) - 1):
                    #                 temp = category + " LIKE '%%" + options2[i] + "%%' OR "
                    #                 search_temp += temp
                    #             search_temp += category + " LIKE '%%" + options2[-1] + "%%'"
                    #
                    #         data = []  # 存储节点数据
                    #         links = []  # 存储关系数据
                    #
                    #         search_res = PftdDecisionIndicator.objects.raw(
                    #             "SELECT id, surgery_type,Period_of_fluid_therapy,Application,Parameters,count(*) as value FROM pftd_decision_indicator"
                    #             " where " + search_temp +
                    #             " GROUP BY surgery_type,Period_of_fluid_therapy,Application,Parameters HAVING surgery_type != 'NA' ")
                    #
                    #         # 处理不同的字段组合
                    #         process_entries(search_res, 'surgery_type', 'period_of_fluid_therapy', links, category,
                    #                         options2)
                    #         process_entries(search_res, 'period_of_fluid_therapy', 'application', links, category,
                    #                         options2)
                    #         process_entries(search_res, 'application', 'parameters', links, category, options2)
                    #
                    #         # 从链接中提取唯一数据项
                    #         data = list(set([link['source'] for link in links] + [link['target'] for link in links]))
                    #
                    #         print(data)
                    #         print(links)
                    #
                    #         # 检测循环
                    #         has_cycle = detect_cycles(links)
                    #         print(f"Does the graph have a cycle? {has_cycle}")
                    #         return render(request, "analysis/analysis_di_sankey.html",
                    #                       {'data': data, 'links': links, "form": form, 'option': res})
                    # search_temp_select = "select * from pftd_decision_indicator where " + search_temp
                    # query_vis = PftdDecisionIndicator.objects.raw(
                    #     "select id, surgery_type as st,Period_of_fluid_therapy as pft,Parameters as para from "
                    #     "(" + search_temp_select + ") as Temp GROUP BY st,pft,para")
                    # for i in query_vis:
                    #     raw_in = []
                    #     sts = [st.strip().title() for st in
                    #            i.st.split(';')]
                    #     sts = [x for x in sts if x]
                    #     pfts = [pft.strip().title() for pft in
                    #             i.pft.split(';')]
                    #
                    #     paras = []
                    #     paras.append(i.parameters.strip().title())
                    #     # paras = [para.strip().title() for para in i.parameters.split(';')]
                    #
                    #     for st in sts:
                    #         for pft in pfts:
                    #             for para in paras:
                    #                 raw_in.append(st)
                    #                 raw_in.append(pft)
                    #                 raw_in.append(para)
                    #                 raw_out.append(raw_in)
                    #                 raw_in = []
                    #
                    # unique_tuples = set(tuple(item) for item in raw_out)
                    #
                    # # 将集合转换回列表的列表
                    # unique_nested_list = [list(item) for item in unique_tuples]
                    #
                    # result = build_tree(unique_nested_list)
                    # print(result)
                    # print(result[0])

                if queryset:
                    # for item in queryset:
                    #     i =1

                    for obj in queryset:
                        rows.append({'id': obj.id, 'Pid': obj.pid, 'parameters': obj.parameters,
                                     'classification_of_fluid_therapy_parameters': obj.classification_of_fluid_therapy_parameters,
                                     'application': obj.application, 'surgery_type': obj.surgery_type,
                                     'period_of_fluid_therapy': obj.period_of_fluid_therapy,
                                     'group_name': obj.group_name,
                                     'pmid': obj.pmid})
                data = {'total': len(queryset), 'rows': rows}
                # print(len(data))
                # print(data)
                # return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
                print(sign)
                return render(request, "tool.html",
                              {"form": form, "data": json.dumps(data), 'nodes': nodes, 'links': links, 'sign':sign})






        else:
            return render(request, "tool.html", {"form": form})

    if request.method == 'GET':
        form = PFTD_Form()

        return render(request, "tool.html", {'form': form})



'''
-------------------------------------------------- recommend --------------------------------------------------
'''

def getInfoBySurgeryType(request):
    if request.method == 'GET':
        data = request.GET.get('type')
        #query1 = PftdDecisionIndicator.objects.raw(
        #    "select id,surgical_site as name from pftd where surgery_type like " + "'%%" + data + "%%'" + " GROUP BY surgical_site ")
        query1 = Pftd.objects.filter(surgery_type=data).values("surgical_site").annotate(counts=Count("surgical_site"))
        # res = ""
        res = []
        dis_array = []
        for i in query1:
            if ";" in i.name:
                temp = i.name.split(";")
                for j in temp:
                    if j not in dis_array:
                        dis_array.append(j)
                        dic_temp = {}
                        dic_temp['name'] = j
                        res.append(dic_temp)
            else:
                if i.name not in dis_array:
                    dis_array.append(i)
                    dic_temp = {}
                    dic_temp['name'] = i.name
                    res.append(dic_temp)

        print(query1)
        # for i in query1:
        #     obj = "(" + "'" + i["surgical_site"] + "'" + ")" + ","
        #     res += obj
        # surgery_site_choices = "(" + res + ")"

        return render(request, "option.html", {'query1': res})
        # for obj in query1:
        #     res.append({'surgical_site':obj['surgical_site']})


def initClass(request):
    if request.method == 'GET':
        data = request.GET.get('type')
        name = request.GET.get('name')
        arr = name.split("_")
        num = "cla" + arr[1]
        dis_array = []
        res = []
        for i in range(1, 6):
            i = str(i)
            temp = "select id,Application" + i + ",`Classification_FT_assessment_factors" + i + "` as cla FROM pftd  GROUP BY Application" + i + ",cla HAVING Application" + i + " LIKE '%%" + data + "%%' "
            # print(temp)
            query = Pftd.objects.raw(temp)
            for j in query:
                if ";" in j.cla:
                    temp = j.cla.split(";")
                    for k in temp:
                        k = k.capitalize()
                        if k not in dis_array:
                            dis_array.append(k)
                else:
                    if j.cla not in dis_array:
                        dis_array.append(j.cla)
        for item in dis_array:
            dic_temp = {}
            dic_temp["name"] = item
            res.append(dic_temp)
        print(num)

        # query1 = Pftd.objects.raw(
        #     "select id,Application1,Classification_FT_ assessment_factors1 as cla1 FROM pftd  GROUP BY Application1,cla1 HAVING Application1 LIKE '%%Fluid volume estimation%%' ")

        return render(request, "option.html", {'query1': res, 'num': num})

    if request.method == 'POST':
        data = request.POST.get('type')
        columnData = json.loads(request.POST.get('columndata'))
        # print(data)
        # print(columnData)
        arr = []
        rows = []
        # 筛选合适的条目
        for id in columnData:
            temp = "SELECT id,Application1,Application2,Application3,Application4,Application5 FROM `pftd` where id =" + str(
                id)
            # temp = "SELECT id,Application1,Application2,Application3,Application4,Application5 FROM `pftd` where id = 70"
            # print(temp)
            query = Pftd.objects.raw(temp)
            if (data.lower() in query[0].application1.lower()) or (data.lower() in query[0].application2.lower()) or (
                    data.lower() in query[0].application3.lower()) or (
                    data.lower() in query[0].application4.lower()) or (
                    data.lower() in query[0].application5.lower()):
                # arr.append(id)
                queryset = Pftd.objects.get(id=id)
                arr.append(queryset)
        if len(arr) > 0:
            print(len(arr))
            for obj in arr:
                rows.append({
                    "id": obj.id,
                    "Period_of_fluid": obj.Period_of_fluid_therapy,
                    "Liquid_treatment": obj.liquid_treatment,
                    "Fluid_name": obj.Fluid_name,
                    "Fluid_type": obj.Fluid_type,
                    "dose": obj.dose,
                    "rate": obj.rate,
                    "duration": obj.duration,
                    "monitoring": obj.monitoring,
                    "monitoring_parameters": obj.monitoring_parameters,
                    "monitoring_frequency": obj.monitoring_frequency,
                    "use_of_vasopressors": obj.use_of_vasopressors,
                    "blood_transfusion": obj.blood_transfusion,
                    "additional_information": obj.additional_information,
                })
        data = {'total': len(arr), 'rows': rows}
        print(data)
        # return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        # return render(request, "recommend.html", {"filter_data": json.dumps(data)})


def initPara(request):
    if request.method == 'GET':
        data = request.GET.get('type')
        name = request.GET.get('id')
        num = "para" + name[-1]
        dis_array = []
        res = []
        for i in range(1, 6):
            i = str(i)
            temp = "select id,Parameter" + i + " as para,`Classification_FT_assessment_factors" + i + "` as cla FROM pftd  GROUP BY Application" + i + ", cla, para HAVING cla LIKE '%%" + data + "%%' "
            # print(temp)
            query = Pftd.objects.raw(temp)
            for j in query:
                if ";" in j.para:
                    temp = j.para.split(";")
                    for k in temp:
                        k = k.capitalize()
                        if k not in dis_array:
                            dis_array.append(k)
                else:
                    if j.para not in dis_array:
                        ar = j.para
                        ar = ar.capitalize()
                        dis_array.append(ar)
        dis_array = list(set(dis_array))
        # print(dis_array)
        for item in dis_array:
            dic_temp = {}
            dic_temp["name"] = item
            res.append(dic_temp)

        # query1 = Pftd.objects.raw(
        #     "select id,Application1,Classification_FT_ assessment_factors1 as cla1 FROM pftd  GROUP BY Application1,cla1 HAVING Application1 LIKE '%%Fluid volume estimation%%' ")

        return render(request, "option.html", {'query1': res, 'num': num})
    if request.method == 'POST':
        data = request.POST.get('type')
        columnData = json.loads(request.POST.get('columndata'))
        # print(data)
        # print(columnData)
        arr = []
        rows = []
        # 筛选合适的条目
        for id in columnData:
            temp = "SELECT id,Classification_FT_assessment_factors1,Classification_FT_assessment_factors2,Classification_FT_assessment_factors3,Classification_FT_assessment_factors4,Classification_FT_assessment_factors5 FROM `pftd` where id =" + str(
                id)
            # temp = "SELECT id,Application1,Application2,Application3,Application4,Application5 FROM `pftd` where id = 70"
            # print(temp)
            query = Pftd.objects.raw(temp)
            if (data.lower() in query[0].classification_ft_assessment_factors1.lower()) or (
                    data.lower() in query[0].classification_ft_assessment_factors2.lower()) or (
                    data.lower() in query[0].classification_ft_assessment_factors3.lower()) or (
                    data.lower() in query[0].classification_ft_assessment_factors4.lower()) or (
                    data.lower() in query[0].classification_ft_assessment_factors5.lower()):
                # arr.append(id)
                queryset = PftdDecisionIndicator.objects.get(id=id)
                arr.append(queryset)
        if len(arr) > 0:
            print(len(arr))
            for obj in arr:
                rows.append({
                    "id": obj.id,
                    "Period_of_fluid": obj.Period_of_fluid_therapy,
                    "Liquid_treatment": obj.liquid_treatment,
                    "Fluid_name": obj.Fluid_name,
                    "Fluid_type": obj.Fluid_type,
                    "dose": obj.dose,
                    "rate": obj.rate,
                    "duration": obj.duration,
                    "monitoring": obj.monitoring,
                    "monitoring_parameters": obj.monitoring_parameters,
                    "monitoring_frequency": obj.monitoring_frequency,
                    "use_of_vasopressors": obj.use_of_vasopressors,
                    "blood_transfusion": obj.blood_transfusion,
                    "additional_information": obj.additional_information,
                })
        data = {'total': len(arr), 'rows': rows}
        print(data)
        # return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')


def LastScreening(request):
    if request.method == 'POST':
        data = request.POST.get('type')
        columnData = json.loads(request.POST.get('columndata'))
        # print(data)
        # print(columnData)
        arr = []
        rows = []
        # 筛选合适的条目
        for id in columnData:
            temp = "SELECT id,Parameter1,Parameter2,Parameter3,Parameter4,Parameter5 FROM `pftd` where id =" + str(id)
            # temp = "SELECT id,Application1,Application2,Application3,Application4,Application5 FROM `pftd` where id = 70"
            # print(temp)
            query = Pftd.objects.raw(temp)
            if (data.lower() in query[0].parameter1.lower()) or (data.lower() in query[0].parameter2.lower()) or (
                    data.lower() in query[0].parameter3.lower()) or (
                    data.lower() in query[0].parameter4.lower()) or (data.lower() in query[0].parameter5.lower()):
                # arr.append(id)
                queryset = Pftd.objects.get(id=id)
                arr.append(queryset)
        if len(arr) > 0:
            print(len(arr))
            for obj in arr:
                rows.append({
                    "id": obj.id,
                    "Period_of_fluid": obj.period_of_fluid_therapy1,
                    "Liquid_treatment": obj.liquid_treatment,
                    "Fluid_name": obj.fluid_name,
                    "Fluid_type": obj.fluid_type,
                    "dose": obj.dose,
                    "rate": obj.rate,
                    "duration": obj.duration,
                    "monitoring": obj.monitoring,
                    "monitoring_parameters": obj.monitoring_parameters,
                    "monitoring_frequency": obj.monitoring_frequency,
                    "use_of_vasopressors": obj.use_of_vasopressors,
                    "blood_transfusion": obj.blood_transfusion,
                    "additional_information": obj.additional_information,
                })
        data = {'total': len(arr), 'rows': rows}
        print(data)
        # return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
        return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')


class Recom_Form(forms.Form):
    age_choices = (
        ("children", "Children（0-6）"),
        ("youth", "Youth（7-17）"),
        ("Adults", "Adults（18-65）"),
        ("Elderly", "Elderly（≥65）"),
    )
    age = forms.MultipleChoiceField(label="Age", widget=forms.CheckboxSelectMultiple, choices=age_choices,
                                    required=True)
    # age = forms.DecimalField(label="Age", widget=forms.TextInput(attrs={"class": "form-control"}), min_value=0,
    #                          decimal_places=2, required=True)
    gender = forms.MultipleChoiceField(label="Gender", widget=forms.CheckboxSelectMultiple,
                                       choices=(('Male', 'Male'), ('Female', 'Female')),
                                       # choices=(('Male', 'Male'), ('Female', 'Female'),('Male, Female','Male & Female')),
                                       required=True)

    bmi_choices = (
        ("underweight", "Underweight（BMI＜18.5）"),
        ("normal", "Normal（BMI18.5～23.9）"),
        ("overweight", "Overweight（BMI24～27.9）"),
        ("obesity", "Obesity（BMI≥28）"),
    )

    bmi = forms.MultipleChoiceField(label="BMI", widget=forms.CheckboxSelectMultiple, choices=bmi_choices,
                                    required=True)

    # bmi = forms.DecimalField(label="BMI", widget=forms.TextInput(attrs={"class": "form-control"}), min_value=0,
    #                          decimal_places=2, required=True)
    surgery_app = forms.MultipleChoiceField(label="Surgery approach", widget=forms.CheckboxSelectMultiple, choices=(
        ('Endoscopic surgery', 'Endoscopic surgery'),
        ('Open surgery', 'Open surgery'), ('Laparoscopic surgery', 'Laparoscopic surgery')), required=False)

    # surgery_site = forms.Select(attrs={"id": "user"})
    # surgery_site = forms.ChoiceField(label="Surgery site", widget=forms.Select(attrs={"id": "user"}))

    asa_choices = (
        ("I", "Ⅰ"),
        ("II", "Ⅱ"),
        ("III", "Ⅲ"),
        ("IV", "Ⅳ"),
    )
    asa = forms.MultipleChoiceField(label="ASA physical status", widget=forms.CheckboxSelectMultiple,
                                    choices=asa_choices, required=False)

    period_of_FT_chioces = (
        ("preoperative", "preoperative"),
        ("intraoperative", "intraoperative"),
        ("postoperative", "postoperative"),
    )
    period_of_FT = forms.MultipleChoiceField(label="Period of FT", widget=forms.CheckboxSelectMultiple,
                                             choices=period_of_FT_chioces, required=False)

    surgery_type_choices = (
        ('', ''),
        ('Thoracic surgery', 'Thoracic surgery'),
        ("Abdominal Surgery", "Abdominal Surgery"),
        ("Cardiac surgery", "Cardiac surgery"),
        ("Gynaecology and obstetrics", "Gynaecology and obstetrics"),
        ("Neurosurgery", "Neurosurgery"),
        ("Bone surgery", "Bone surgery"),
        ("Vascular Surgery", "Vascular Surgery"),
        ("Otolaryngology", "Otolaryngology"),
        ("Craniotomy", "Craniotomy"),
        ("Urology Surgery", "Urology Surgery"),
        ("Pediatric surgery", "Pediatric surgery"),
        ("Others", "Others"),

    )
    surgery_type = forms.ChoiceField(label="Surgery type",
                                     widget=forms.Select(
                                         attrs={"class": "form-control", "style": "font-size: 20px",
                                                "onchange": "selectOnchange(this)"}),
                                     choices=surgery_type_choices, required=False)


    parameter_choices = (
        ('', ''),
        ('Clinical signs', 'Clinical signs'),
        ('Complications', 'Complications'),
        ('Hemodynamic parameters', 'Hemodynamic parameters'),
        ('Insensible losses', 'Insensible losses'),
        ('Intake factors', 'Intake factors'),
        ('Laboratory tests', 'Laboratory tests'),
        ('Other factors', 'Other factors'),
        ('Physical examinations', 'Physical examinations'),
        ('Physiological factors', 'Physiological factors'),
        ('Treatment information', 'Treatment information'),
        ('Vital signs', 'Vital signs'),
        ('Volume loss factors', 'Volume loss factors'),
    )
    classification_1 = forms.ChoiceField(label="Classifications",
                                     widget=forms.Select(
                                    attrs={"class": "form-label", "style": "font-size: 20px",
                                                "onchange": "onDropdown1Change(this)"}),
                                     choices=parameter_choices, required=False)

    classification_2 = forms.ChoiceField(label="Classifications",
                                   widget=forms.Select(
                                       attrs={"class": "form-label", "style": "font-size: 20px",
                                              "onchange": "onDropdown1Change(this)"}),
                                   choices=parameter_choices, required=False)

    classification_3 = forms.ChoiceField(label="Classifications",
                                   widget=forms.Select(
                                       attrs={"class": "form-label", "style": "font-size: 20px",
                                              "onchange": "onDropdown1Change(this)"}),
                                   choices=parameter_choices, required=False)



    dropdown_choices = (
        ('', ''),  # 空选项
        ('normovolaemia', 'normovolaemia'),
        ('reported no pain at 8 hours', 'reported no pain at 8 hours'),
        ('signs of ischaemia', 'signs of ischaemia'),
        ('tachycardia', 'tachycardia'),
        ('oliguria', 'oliguria'),
        ('hypovolemia', 'hypovolemia'),
        ('Clinical indication', 'Clinical indication'),
        ('skin turgor', 'skin turgor'),
        ('clinical signs of inadequate cardiac output', 'clinical signs of inadequate cardiac output'),
        ('hypotensive', 'hypotensive'),
        ('hemodynamic instability', 'hemodynamic instability'),
        ('signs of platelet dysfunction', 'signs of platelet dysfunction'),
        ('severe cyanosis', 'severe cyanosis'),

        ('Postoperative complications', 'Postoperative complications'),
        ('systolic left ventricular failure', 'systolic left ventricular failure'),
        ('Sangrado postoperatorio', 'Sangrado postoperatorio'),
        ('Complications', 'Complications'),
        ('bleeding', 'bleeding'),
        ('thrombocytopenia', 'thrombocytopenia'),
        ('hyperkalemia', 'hyperkalemia'),

        ('SVV', 'SVV'),
        ('CI', 'CI'),
        ('MAP', 'MAP'),
        ('SV', 'SV'),
        ('PPV', 'PPV'),
        ('CVP', 'CVP'),
        ('blood flow time', 'blood flow time'),
        ('SAP', 'SAP'),
        ('SVI', 'SVI'),
        ('standard haemodynamic parameters', 'standard haemodynamic parameters'),
        ('FTc', 'FTc'),
        ('PCWP', 'PCWP'),
        ('respiratory variation in systole', 'respiratory variation in systole'),
        ('nonpulsatile blood flow', 'nonpulsatile blood flow'),
        ('SVRI', 'SVRI'),
        ('PVI', 'PVI'),
        ('LVETI', 'LVETI'),
        ('ACC', 'ACC'),
        ('TSVRi', 'TSVRi'),
        ('GEDI', 'GEDI'),
        ('ejection fraction', 'ejection fraction'),
        ('△SV', '△SV'),
        ('perfusion pressure', 'perfusion pressure'),
        ('CO', 'CO'),
        ('central venous diastolic pressures', 'central venous diastolic pressures'),
        ('pulmonary artery diastolic pressures', 'pulmonary artery diastolic pressures'),
        ('INVOS value', 'INVOS value'),
        ('BIS', 'BIS'),
        ('mean systemic arterial BP', 'mean systemic arterial BP'),
        ('left ventricular filling pressure', 'left ventricular filling pressure'),
        ('△PV', '△PV'),
        ('rSO2', 'rSO2'),
        ('IVC respiratory variation', 'IVC respiratory variation'),
        ('PAOP', 'PAOP'),
        ('ΔPP', 'ΔPP'),
        ('PAM', 'PAM'),
        ('VFDVⅡ', 'VFDVⅡ'),
        ('DO2', 'DO2'),
        ('Afterload', 'Afterload'),
        ('HPI', 'HPI'),
        ('dP/dTmax', 'dP/dTmax'),
        ('left ventricular ejection fraction', 'left ventricular ejection fraction'),


        ('ongoing insensible losses', 'ongoing insensible losses'),
        ('sweating losses', 'sweating losses'),
        ('perspiratio insensibilis', 'perspiratio insensibilis'),
        ('evaporative loss arising from visceral exposure', 'evaporative loss arising from visceral exposure'),


        ('clinical signs of inadequate cardiac output', 'clinical signs of inadequate cardiac output'),
        ('tachycardia', 'tachycardia'),
        ('Clinical indication', 'Clinical indication'),

        ('Hb', 'Hb'),
        ('O2ER', 'O2ER'),
        ('EBV', 'EBV'),
        ('hematocrit', 'hematocrit'),
        ('Plasma sodium level', 'Plasma sodium level'),
        ('Albumin concentration', 'Albumin concentration'),
        ('DO2I', 'DO2I'),
        ('arterial blood gas values', 'arterial blood gas values'),
        ('Scvo2', 'Scvo2'),
        ('Dco2', 'Dco2'),
        ('SaO2', 'SaO2'),
        ('CI', 'CI'),
        ('packed red blood cell', 'packed red blood cell'),
        ('base excess', 'base excess'),
        ('INR', 'INR'),
        ('APTT', 'APTT'),
        ('platelet count', 'platelet count'),
        ('fibrinogen', 'fibrinogen'),
        ('acPDD', 'acPDD'),
        ('acPED', 'acPED'),
        ('serum amylase', 'serum amylase'),
        ('lipase', 'lipase'),
        ('serum lactate', 'serum lactate'),
        ('SvO2', 'SvO2'),
        ('ACT', 'ACT'),
        ('PT', 'PT'),
        ('antithrombin Ⅲ', 'antithrombin Ⅲ'),
        ('HB', 'HB'),
        ('pH', 'pH'),
        ('RBCV', 'RBCV'),
        ('creatinine', 'creatinine'),
        ('FLEV', 'FLEV'),
        ('TSP', 'TSP'),

        ('the total crystalloid administration', 'the total crystalloid administration'),
        ('thromboelastography', 'thromboelastography'),
        ('the maximum dose of HES 130/0.4', 'the maximum dose of HES 130/0.4'),
        ('positive fluid balance', 'positive fluid balance'),
        ('dose of crystalloid', 'dose of crystalloid'),
        ('HL', 'HL'),
        ('Killip class', 'Killip class'),
        ('COP', 'COP'),
        ('vasopressor requirement', 'vasopressor requirement'),
        ('CVP minus PEEP', 'CVP minus PEEP'),
        ('the maximum amount of the study fluid', 'the maximum amount of the study fluid'),
        ('Total Protocol Fluid', 'Total Protocol Fluid'),
        ('VTI', 'VTI'),
        ('IV fluid dose', 'IV fluid dose'),
        ('PaO2/FiO2', 'PaO2/FiO2'),
        ('pharmacological agents', 'pharmacological agents'),
        ('anesthesia expansion volume', 'anesthesia expansion volume'),
        ('Eadyn', 'Eadyn'),

        ('capillary refill time', 'capillary refill time'),
        ('ECG', 'ECG'),
        ('OCT', 'OCT'),

        ('Weight', 'Weight'),
        ('gender', 'gender'),
        ('weight', 'weight'),
        ('ideal body weight', 'ideal body weight'),
        ('PCWP', 'PCWP'),
        ('BV', 'BV'),
        ('physiological requirement', 'physiological requirement'),


        ('complex surgery', 'complex surgery'),


        ('SBP', 'SBP'),
        ('HR', 'HR'),
        ('BP', 'BP'),
        ('arterial BP', 'arterial BP'),
        ('PPV', 'PPV'),
        ('MHR', 'MHR'),
        ('MBP', 'MBP'),
        ('PR', 'PR'),
        ('DBP', 'DBP'),
        ('body temperature', 'body temperature'),


        ('blood loss', 'blood loss'),
        ('urine output', 'urine output'),
        ('fluid losses', 'fluid losses'),
        ('Blood loss', 'Blood loss'),
        ('drainage losses', 'drainage losses'),
        ('gastric tube drainage', 'gastric tube drainage'),
    )

    classification_1_dropdown = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-label", "style": "font-size: 20px"}), choices=dropdown_choices, required=False)
    classification_2_dropdown = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-label", "style": "font-size: 20px"}), choices=dropdown_choices,required=False)
    classification_3_dropdown = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-label", "style": "font-size: 20px"}), choices=dropdown_choices,required=False)

    #Application_choices = (
    #    ('Fluid volume estimation', 'Fluid volume estimation'),
    #    ("Fluid type estimation", "Fluid type estimation"),
    #    ("Use of vasoactive agents Assessment", "Use of vasoactive agents Assessment"),
    #    ("Transfusion Assessment", "Transfusion Assessment"),
    #    ("NA", "NA")
    #)
    #application_1 = forms.ChoiceField(label="Application1",
    #                                  widget=forms.Select(
    #                                      attrs={"class": "selectpicker", "data-live-search": "true", "data-size": "5",
    #                                             "title": "Application1", "onchange": "initclass(this)"}),
    #                                  choices=Application_choices, required=False)
    # application_2 = forms.ChoiceField(label="Application2",
    #                                   widget=forms.Select(
    #                                       attrs={"class": "selectpicker", "data-live-search": "true", "data-size": "5",
    #                                              "title": "Application2", "onchange": "initclass(this)"}),
    #                                   choices=Application_choices, required=False)
    # application_3 = forms.ChoiceField(label="Application3",
    #                                   widget=forms.Select(
    #                                       attrs={"class": "selectpicker", "data-live-search": "true", "data-size": "5",
    #                                              "title": "Application3", "onchange": "initclass(this)"}),
    #                                   choices=Application_choices, required=False)
    # application_4 = forms.ChoiceField(label="Application4",
    #                                   widget=forms.Select(
    #                                       attrs={"class": "selectpicker", "data-live-search": "true", "data-size": "5",
    #                                              "title": "Application4", "onchange": "initclass(this)"}),
    #                                   choices=Application_choices, required=False)
    # application_5 = forms.ChoiceField(label="Application5",
    #                                   widget=forms.Select(
    #                                       attrs={"class": "selectpicker", "data-live-search": "true", "data-size": "5",
    #                                              "title": "Application5", "onchange": "initclass(this)"}),
    #                                   choices=Application_choices, required=False)


def generate_temp(map):
    list = map["list"]
    if len(list) == 0:
        return ""
    type = map["type"]
    res_temp = ""
    if len(list) == 1:
        res_temp += type + " LIKE '%%" + list[-1] + "%%'"
    else:
        for i in range(0, len(list) - 1):
            temp = type + " LIKE '%%" + list[i] + "%%' OR "
            res_temp += temp
        res_temp += type + " LIKE '%%" + list[-1] + "%%'"
    res_temp = '(' + res_temp + ')'
    return res_temp


def generate_map(str, list):
    map_temp = {}
    map_temp["type"] = str
    map_temp["list"] = list
    return map_temp


def recommend(request):
    if request.method == "GET":
        # query1 = Pftd.objects.values("surgical_site").filter(surgery_type='Abdominal Surgery')[:5]
        form = Recom_Form()
        return render(request, "recommend.html", {"form": form})
    if request.method == "POST":
        form = Recom_Form(data=request.POST)
        #print(form.is_valid())
        if form.is_valid():
            # 从表单中获取清洗后的数据
            age = form.cleaned_data.get("age")
            gender = form.cleaned_data.get("gender")
            bmi = form.cleaned_data.get("bmi")
            surgery_app = form.cleaned_data.get("surgery_app")
            period_of_FT = form.cleaned_data.get("period_of_FT")
            surgery_type = form.cleaned_data.get("surgery_type")
            surgery_site = request.POST.get("surgery_site")
            asa = form.cleaned_data.get("asa")

            classification_1 = form.cleaned_data.get("classification_1")
            classification_2 = form.cleaned_data.get("classification_2")
            classification_3 = form.cleaned_data.get("classification_3")
            classification_1_dropdown = form.cleaned_data.get("classification_1_dropdown")
            classification_2_dropdown = form.cleaned_data.get("classification_2_dropdown")
            classification_3_dropdown = form.cleaned_data.get("classification_3_dropdown")


            # 生成搜索条件的映射和临时查询条件
            gender_map = generate_map("gender", gender)
            gender_temp = generate_temp(gender_map)
            age_map = generate_map("age", age)
            age_temp = generate_temp(age_map)
            bmi_map = generate_map("bmi", bmi)
            bmi_temp = generate_temp(bmi_map)

            step2_arr = []
            if surgery_app:
                surgery_app_map = generate_map("Surgical_approach", surgery_app)
                surgery_app_temp = generate_temp(surgery_app_map)

                step2_arr.append(surgery_app_temp)

            if surgery_type:
                surgery_type_temp = "( surgery_type = '" + surgery_type + "' )"
                step2_arr.append(surgery_type_temp)

            if surgery_site:
                surgery_site_temp = "( surgical_site" + " LIKE '%%" + surgery_site + "%%' )"
                step2_arr.append(surgery_site_temp)

            if asa:
                asa_map = generate_map("ASA_physical_status", asa)
                asa_temp = generate_temp(asa_map)
                step2_arr.append(asa_temp)

            if period_of_FT:
                period_of_FT_map = generate_map("Period_of_fluid_therapy", period_of_FT)
                period_of_FT_temp = generate_temp(period_of_FT_map)
                step2_arr.append(period_of_FT_temp)

            step3_arr = []


            if classification_1:
                classification_1_temp = "( Classification_FT_assessment_factors1" + " LIKE '%%" + classification_1 + "%%' )"
                classification_2_temp = "( Classification_FT_assessment_factors2" + " LIKE '%%" + classification_1 + "%%' )"
                classification_3_temp = "( Classification_FT_assessment_factors3" + " LIKE '%%" + classification_1 + "%%' )"
                classification_4_temp = "( Classification_FT_assessment_factors4" + " LIKE '%%" + classification_1 + "%%' )"
                classification_5_temp = "( Classification_FT_assessment_factors5" + " LIKE '%%" + classification_1 + "%%' )"
                temp1 = "(" + classification_1_temp + " OR " + classification_2_temp + " OR " + classification_3_temp + " OR " + classification_4_temp + " OR "+ classification_5_temp + ")"

                classification_1_dropdown_temp = "( Parameter1" + " LIKE '%%" + classification_1_dropdown + "%%' )"
                classification_2_dropdown_temp = "( Parameter2" + " LIKE '%%" + classification_1_dropdown + "%%' )"
                classification_3_dropdown_temp = "( Parameter3" + " LIKE '%%" + classification_1_dropdown + "%%' )"
                classification_4_dropdown_temp = "( Parameter4" + " LIKE '%%" + classification_1_dropdown + "%%' )"
                classification_5_dropdown_temp = "( Parameter5" + " LIKE '%%" + classification_1_dropdown + "%%' )"
                temp2 = "(" + classification_1_dropdown_temp + " OR " + classification_2_dropdown_temp + " OR " + classification_3_dropdown_temp + " OR " + classification_4_dropdown_temp + " OR " + classification_5_dropdown_temp + ")"

                temp = temp1 + "and" + temp2
                step3_arr.append(temp)


            if classification_2:
                classification_1_temp = "( Classification_FT_assessment_factors1" + " LIKE '%%" + classification_2 + "%%' )"
                classification_2_temp = "( Classification_FT_assessment_factors2" + " LIKE '%%" + classification_2 + "%%' )"
                classification_3_temp = "( Classification_FT_assessment_factors3" + " LIKE '%%" + classification_2 + "%%' )"
                classification_4_temp = "( Classification_FT_assessment_factors4" + " LIKE '%%" + classification_2 + "%%' )"
                classification_5_temp = "( Classification_FT_assessment_factors5" + " LIKE '%%" + classification_2 + "%%' )"
                temp1 = "(" + classification_1_temp + " OR " + classification_2_temp + " OR " + classification_3_temp + " OR " + classification_4_temp + " OR " + classification_5_temp + ")"

                classification_1_dropdown_temp = "( Parameter1" + " LIKE '%%" + classification_2_dropdown + "%%' )"
                classification_2_dropdown_temp = "( Parameter2" + " LIKE '%%" + classification_2_dropdown + "%%' )"
                classification_3_dropdown_temp = "( Parameter3" + " LIKE '%%" + classification_2_dropdown + "%%' )"
                classification_4_dropdown_temp = "( Parameter4" + " LIKE '%%" + classification_2_dropdown + "%%' )"
                classification_5_dropdown_temp = "( Parameter5" + " LIKE '%%" + classification_2_dropdown + "%%' )"
                temp2 = "(" + classification_1_dropdown_temp + " OR " + classification_2_dropdown_temp + " OR " + classification_3_dropdown_temp + " OR " + classification_4_dropdown_temp + " OR " + classification_5_dropdown_temp + ")"

                temp = temp1 + "and" + temp2
                step3_arr.append(temp)



            if classification_2:
                classification_1_temp = "( Classification_FT_assessment_factors1" + " LIKE '%%" + classification_3 + "%%' )"
                classification_2_temp = "( Classification_FT_assessment_factors2" + " LIKE '%%" + classification_3 + "%%' )"
                classification_3_temp = "( Classification_FT_assessment_factors3" + " LIKE '%%" + classification_3 + "%%' )"
                classification_4_temp = "( Classification_FT_assessment_factors4" + " LIKE '%%" + classification_3 + "%%' )"
                classification_5_temp = "( Classification_FT_assessment_factors5" + " LIKE '%%" + classification_3 + "%%' )"
                temp1 = "(" + classification_1_temp + " OR " + classification_2_temp + " OR " + classification_3_temp + " OR " + classification_4_temp + " OR " + classification_5_temp + ")"

                classification_1_dropdown_temp = "( Parameter1" + " LIKE '%%" + classification_3_dropdown + "%%' )"
                classification_2_dropdown_temp = "( Parameter2" + " LIKE '%%" + classification_3_dropdown + "%%' )"
                classification_3_dropdown_temp = "( Parameter3" + " LIKE '%%" + classification_3_dropdown + "%%' )"
                classification_4_dropdown_temp = "( Parameter4" + " LIKE '%%" + classification_3_dropdown + "%%' )"
                classification_5_dropdown_temp = "( Parameter5" + " LIKE '%%" + classification_3_dropdown + "%%' )"
                temp2 = "(" + classification_1_dropdown_temp + " OR " + classification_2_dropdown_temp + " OR " + classification_3_dropdown_temp + " OR " + classification_4_dropdown_temp + " OR " + classification_5_dropdown_temp + ")"

                temp = temp1 + "and" + temp2
                step3_arr.append(temp)

            #(Classification_FT_assessment_factors1 LIKE '%%Clinical signs%%') OR (Classification_FT_assessment_factors2 LIKE '%%Clinical signs%%') OR (Classification_FT_assessment_factors3 LIKE '%%Clinical signs%%')





            # 生成最终的搜索查询条件
            search_temp_arr = []

            step1 = age_temp + " and " + bmi_temp + " and " + gender_temp

            # search_temp = " and ".join(arr)
            # search_temp_arr.append(search_base_temp+" and "+search_temp)

            '''
            # step1 和 step2 排列组合
            for j in range(len(step2_arr), 0, -1):              # 递减步长为1,     4,3,2,1
                #print(j)
                for e in it.combinations(step2_arr, j):
                    #print(e)
                    search_temp_demo = " and ".join(e)
                    search_temp = step1 + " and " + search_temp_demo
                    search_temp_arr.append(search_temp)
            search_temp_arr.append(step1)  # 0
            '''

            search_arr1 = []
            search_arr2 = []

            step2_arr = step2_arr + step3_arr
            # Step 1: 排列组合 step2_arr
            for j in range(len(step2_arr), 0, -1):  # 递减步长为1, 4,3,2,1
                for e in it.combinations(step2_arr, j):
                    search_temp_demo = " and ".join(e)
                    search_temp = step1 + " and " + search_temp_demo
                    search_temp_arr.append(search_temp)
                    search_arr1.append((search_temp))

            '''
            # Step 2: 对 step3_arr 进行排列组合，并将其加到 step2_arr 的组合中
            for j in range(len(step2_arr), 0, -1):  # 递减步长为1, 4,3,2,1
                for e in it.combinations(step2_arr, j):
                    search_temp_demo = " and ".join(e)
                    for k in range(len(step3_arr), 0, -1):  # Step 3: 递减步长为1, 3,2,1
                        for e3 in it.combinations(step3_arr, k):
                            search_temp_demo3 = " and ".join(e3)
                            search_temp = step1 + " and " + search_temp_demo + " and " + search_temp_demo3
                            search_temp_arr.append(search_temp)
                            search_arr2.append(search_temp)  # final search
            '''

            # 添加只包含 step1 的查询
            search_temp_arr.append(step1)

            search_arr = search_arr2 + search_arr1
            search_arr.append(step1)

            # 输出结果
            #for search in search_temp_arr:
            #    print(search)

            #print(len(step2_arr))
            #print(len(step3_arr))


            for search in search_arr:
                print(search)
            #print(step2_arr)
            #print(search)
            #search_temp_arr = search_temp_arr[0:1]
            #for k in search_temp_arr:
            #    print(1, k)

            # application1 = form.cleaned_data.get("application_1")
            # application2 = form.cleaned_data.get("application_2")
            # application3 = form.cleaned_data.get("application_3")
            # application4 = form.cleaned_data.get("application_4")
            # application5 = form.cleaned_data.get("application_5")
            # print(application1)
            # print(application2)
            # print(application3)
            # print(application4)
            # print(application5)






            # 查询数据库并获取结果
            rows = []
            queryset = []
            for search_temp in search_temp_arr:
                #print(search_temp)
                queryset = Pftd.objects.raw("select * from pftd where " + search_temp)

            # queryset1 = Pftd.objects.all().filter(age__icontains=age, gender__contains=gender,
            #                                       bmi__contains=bmi, surgical_approach=surgery_app,
            #                                       period_of_fluid_therapy2=period_of_FT,
            #                                       surgery_type=surgery_type, surgical_site=surgery_site,
            #                                       asa_physical_status__contains=asa)
            # queryset2 = Pftd.objects.all().filter(age__icontains=age,
            #                                       gender__contains=gender, bmi__contains=bmi,
            #                                       surgical_approach=surgery_app,
            #                                       period_of_fluid_therapy2=period_of_FT,
            #                                       surgery_type=surgery_type, surgical_site=surgery_site)
            # queryset3 = Pftd.objects.all().filter(age__icontains=age, gender__contains=gender,
            #                                       bmi__contains=bmi,
            #                                       surgical_approach=surgery_app, surgery_type=surgery_type,
            #                                       surgical_site=surgery_site)
            # queryset4 = Pftd.objects.all().filter(age__icontains=age, gender__contains=gender,
            #                                       bmi__contains=bmi,
            #                                       surgery_type=surgery_type,
            #                                       surgical_site=surgery_site)
                if queryset:
                    # for item in queryset:
                    #     i =1

                    for obj in queryset:
                        # print(obj.id,  obj.Classification_FT_assessment_factors1)
                        rows.append({
                            "id": obj.id,
                            "IFTP": obj.IFTP,
                            "IFTP_subgroup": obj.IFTP_subgroup,
                            "Period_of_fluid": obj.Period_of_fluid_therapy,
                            "Liquid_treatment": obj.liquid_treatment,
                            "Fluid_name": obj.Fluid_name,
                            "Fluid_type": obj.Fluid_type,
                            "dose": obj.Dose,
                            "rate": obj.Rate,
                            "duration": obj.Duration,
                            "monitoring": obj.Monitoring,
                            "monitoring_parameters": obj.Monitoring_Parameters,
                            "monitoring_frequency": obj.Monitoring_frequency,
                            "use_of_vasopressors": obj.Use_of_vasopressors,
                            "blood_transfusion": obj.Blood_transfusion,
                            "additional_information": obj.Additional_information,
                            "parameter1": obj.Parameter1,
                            "classification1": obj.Classification_FT_assessment_factors1,
                            "parameter2": obj.Parameter2,
                            "classification2": obj.Classification_FT_assessment_factors2,
                            "parameter3": obj.Parameter3,
                            "classification3": obj.Classification_FT_assessment_factors3,
                            "parameter4": obj.Parameter4,
                            "classification4": obj.Classification_FT_assessment_factors4,
                            "parameter5": obj.Parameter5,
                            "classification5": obj.Classification_FT_assessment_factors5,
                        })

            data = {'total': len(queryset), 'rows': rows}
            # print(data)
            # return HttpResponse(json.dumps(data, separators=(',', ':')), content_type='application/json')
            return render(request, "recommend.html", {"form": form, "data": json.dumps(data)})
        else:
            return render(request, "recommend.html", {"form": form})



'''
-------------------------------------------------- recommend --------------------------------------------------
'''










'''
 Analysis for Publication Years (PMID)
'''


class ana_type_form(forms.Form):
    type_choices = (
        ('region', 'Region'),
        # ("race", "Race"),
        ("age", "Population"),
        # ("gender", "Gender"),
        ("asa_physical_status", "ASA physical status"),
        # ("bmi", "BMI"),
        ("surgical_approach", "Surgery Approach"),
        ("surgery_type", "Surgical Type"),
        ("period_of_fluid_therapy", "Period of Fluid Therapy"),
        ("classification_of_fluid_therapy_parameters", "Classification of PFTD parameters"),
        ("application", "Parameter Application"),

    )
    category = forms.ChoiceField(label="Category",
                                 widget=forms.Select(
                                     attrs={"class": "selectpicker", "id": "user2", "data-live-search": "true",
                                            "data-size": "5",
                                            "title": "Choose one of the following...",
                                            "onchange": "selectOnchange(this)"}),
                                 choices=type_choices, required=True)


def category_search(request):
    if request.method == 'GET':
        data = request.GET.get('type')
        tests = Pftd.objects.raw("select id," + data + " as name from pftd GROUP BY " + data)
        res = []
        if data == 'asa_physical_status':
            # chinese_chr = r'Ⅰ Ⅱ Ⅲ Ⅳ Ⅴ'
            # english_chr = r'I II'
            for i in tests:
                if i.name is None:
                    continue

                if ";" in i.name:
                    temp = i.name.split(";")
                    for j in temp:
                        dict_temp = {}
                        j = j.strip()
                        dict_temp["name"] = j
                        res.append(dict_temp)
                elif "；" in i.name:
                    temp = i.name.split("；")
                    for j in temp:
                        dict_temp = {}
                        j = j.strip()
                        dict_temp["name"] = j
                        res.append(dict_temp)
                else:
                    dict_temp = {}
                    i.name = i.name.strip()
                    dict_temp["name"] = i.name
                    res.append(dict_temp)
            res1 = [dict(t) for t in {tuple(d.items()) for d in res}
                    if not any(v in ('Na', None, '', 'NA') for k, v in dict(t).items())]
            roman_order = {
                'Ⅰ': 1, 'I': 1,
                'Ⅱ': 2, 'II': 2,
                'Ⅲ': 3, 'III': 3,
                'Ⅳ': 4, 'IV': 4,
                'Ⅴ': 5, 'V': 5
            }
            sorted_roman_numerals = sorted(res1, key=lambda x: roman_order[x['name']])
            return render(request, "option.html", {'query1': sorted_roman_numerals})
        else:

            for i in tests:
                if "; " in i.name:
                    temp = i.name.split("; ")
                    for j in temp:
                        dict_temp = {}
                        j = j.strip()
                        dict_temp["name"] = j.capitalize()
                        res.append(dict_temp)
                elif ";" in i.name:
                    temp = i.name.split(";")
                    for j in temp:
                        dict_temp = {}
                        j = j.strip()
                        dict_temp["name"] = j.capitalize()
                        res.append(dict_temp)
                else:
                    dict_temp = {}
                    i.name = i.name.strip()
                    dict_temp["name"] = i.name.capitalize()
                    res.append(dict_temp)
            res1 = [dict(t) for t in {tuple(d.items()) for d in res}
                    if not any(v in ('Na', None, '', 'NA') for k, v in dict(t).items())]

            if data == 'age':
                roman_order = {'Children': 1, 'Youths': 2, 'Adults': 3, 'Elderly': 4}
                sorted_roman_numerals = sorted(res1, key=lambda x: roman_order[x['name']])
                print(sorted_roman_numerals)
                return render(request, "option.html", {'query1': sorted_roman_numerals})

            elif data == 'bmi':
                roman_order = {'Underweight': 1, 'Normal': 2, 'Obesity': 3, 'Overweight': 4}
                sorted_roman_numerals = sorted(res1, key=lambda x: roman_order[x['name']])
                return render(request, "option.html", {'query1': sorted_roman_numerals})

            elif data == 'period_of_fluid_therapy':
                roman_order = {'Preoperative': 1, 'Intraoperative': 2, 'Postoperative': 3}
                sorted_roman_numerals = sorted(res1, key=lambda x: roman_order[x['name']])
                return render(request, "option.html", {'query1': sorted_roman_numerals})
            elif data == 'surgery_type':
                sorted_roman_numerals = [{'name': 'Cardiac surgery'}, {'name': 'Abdominal surgery'},
                                         {'name': 'Thoracic surgery'}, {'name': 'Urological surgery'},
                                         {'name': 'Vascular Surgery'}, {'name': 'Neurosurgery'},
                                         {'name': 'Head and neck surgery'}, {'name': 'Orthopedic surgery'},
                                         {'name': 'Gynecological surgery'}, {'name': 'Obstetric surgery'},
                                         {'name': 'Pediatric surgery'}, {'name': 'Bariatric surgery'},
                                         {'name': 'Critically ill surgery'}, {'name': 'Other surgeries'}]
                return render(request, "option.html", {'query1': sorted_roman_numerals})
            elif data == 'classification_of_fluid_therapy_parameters':
                sorted_roman_numerals = [{'name': 'Hemodynamic parameters'}, {'name': 'Physiological factors'},
                                         {'name': 'Laboratory tests'}, {'name': 'volume loss factors'},
                                         {'name': 'vital signs'}, {'name': 'Intake factors'},
                                         {'name': 'clinical signs'}, {'name': 'Insensible losses'},
                                         {'name': 'Physical examinations'}, {'name': 'Complications'},
                                         {'name': 'Treatment information'}, {'name': 'Other factors'}]
                return render(request, "option.html", {'query1': sorted_roman_numerals})
            elif data == 'application':
                sorted_roman_numerals = [{'name': 'fluid volume estimation'}, {'name': 'fluid type estimation'},
                                         {'name': 'fluid therapy rate assessment'},
                                         {'name': 'transfusion assessment'},
                                         {'name': 'Use of vasoactive agents Assessment'}]
                return render(request, "option.html", {'query1': sorted_roman_numerals})
            else:
                return render(request, "option.html", {'query1': res1})


def publication_years(request):
    if request.method == 'GET':
        form = ana_type_form()
        tests = PftdDecisionIndicator.objects.raw(
            "select id, Year as year,count(*)as count from (SELECT id, Year,pmid FROM pftd_decision_indicator GROUP BY pmid)as temp GROUP BY Year ORDER BY Year")
        # year = []
        # count = []
        # for i in tests:
        #     year.append(i.year)
        #     count.append(i.count)
        # data = {'xdata':year,'ydata':count}
        # print(data)
        # print(tests.db)
        return render(request, "analysis/analysis_py.html", {'data': tests, "form": form})
    if request.method == 'POST':
        form = ana_type_form(data=request.POST)
        if form.is_valid():
            category = form.cleaned_data.get("category")
            options = request.POST.getlist("name")
            name = ",".join(options)
            res = "——【" + name + "】"
            # if options == 'M&F':
            #     temp = 'M and F'
            #     res = "——【" + temp + "】"
            # else:
            #     res = "——【" + options + "】"

            # 根据options生成特定的检索式
            search_temp = ""
            if len(options) == 1:
                if options[-1] == 'Other surgeries':
                    search_temp = "(surgery_type LIKE '%%Non-cardiac surgery%%' OR surgery_type LIKE '%%post-endoscopic retrograde cholangiopancreatography(ERCP)%%'" \
                                  "OR surgery_type LIKE '%%urgent PCI%%'OR surgery_type LIKE '%%Oncosurgery%%'" \
                                  "OR surgery_type = 'NA'OR surgery_type LIKE '%%other surgery%%'" \
                                  "OR surgery_type LIKE '%%other surgeries%%' )"
                elif options[-1] == 'Cardiac surgery':
                    search_temp = "( surgery_type= '" + options[-1] + "')"
                else:
                    search_temp += category + " LIKE '%%" + options[-1] + "%%'"
            elif len(options) == 0:
                form = ana_type_form()
                tests = PftdDecisionIndicator.objects.raw(
                    "select id, Year as year,count(*)as count from (SELECT id, Year,pmid FROM pftd_decision_indicator GROUP BY pmid)as temp GROUP BY Year ORDER BY Year")
                return render(request, "analysis/analysis_py.html", {'data': tests, "form": form})
            else:
                for i in range(0, len(options) - 1):
                    if options[i] == 'Other surgeries':
                        temp = "(surgery_type LIKE '%%Non-cardiac surgery%%' OR surgery_type LIKE '%%post-endoscopic retrograde cholangiopancreatography(ERCP)%%'" \
                               "OR surgery_type LIKE '%%urgent PCI%%'OR surgery_type LIKE '%%Oncosurgery%%'" \
                               "OR surgery_type = 'NA'OR surgery_type LIKE '%%other surgery%%'" \
                               "OR surgery_type LIKE '%%other surgeries%%' ) OR "
                        search_temp += temp
                    if options[i] == 'Cardiac surgery':
                        temp = "( surgery_type= '" + options[i] + "') OR "
                        search_temp += temp
                    else:
                        temp = category + " LIKE '%%" + options[i] + "%%' OR "
                        search_temp += temp
                search_temp += category + " LIKE '%%" + options[-1] + "%%'"
                # print(search_temp)
            # test = "select id, Year as year,count(*)as count from (SELECT id, Year,pmid FROM pftd where " + search_temp+ " GROUP BY pmid)as temp GROUP BY Year"
            # print(test)

            # tests = Pftd.objects.raw("select id, Year as year,count(*)as count from (SELECT id, Year,pmid FROM pftd where region LIKE '%America%' GROUP BY pmid)as temp GROUP BY Year")
            # for i in tests:
            #     print(i.year)
            tests = PftdDecisionIndicator.objects.raw(
                "select id, Year as year,count(*)as count from (SELECT id, Year,pmid FROM pftd_decision_indicator where " + search_temp + " GROUP BY pmid)as temp GROUP BY Year ORDER BY Year")

            return render(request, "analysis/analysis_py.html", {"form": form, 'data': tests, 'option': res})
        else:

            return render(request, "analysis/analysis_py.html", {"form": form})


'''
 Analysis for Country distribution (PMID)
'''


class ana_cd_form(forms.Form):
    type_choices2 = (
        ('region', 'Region'),
        # ("race", "Race"),
        ("age", "Population"),
        # ("gender", "Gender"),
        ("asa_physical_status", "ASA physical status"),
        # ("bmi", "BMI"),
        ("surgical_approach", "Surgery Approach"),
        ("surgery_type", "Surgical Type"),
        ("period_of_fluid_therapy", "Period of Fluid Therapy"),
        ("classification_of_fluid_therapy_parameters", "Classification of PFTD parameters"),
        ("application", "Parameter Application"),

    )
    category_cd = forms.ChoiceField(label="Category",
                                    widget=forms.Select(
                                        attrs={"class": "selectpicker", "id": "user2", "data-live-search": "true",
                                               "data-size": "5",
                                               "title": "Choose one of the following...",
                                               "onchange": "selectOnchange(this)"}),
                                    choices=type_choices2)


import re
from collections import defaultdict
def country_dis(request):
    if request.method == 'GET':
        # 国家名称标准化映射
        COUNTRY_MAPPING = {
            'America': 'United States',
            'USA': 'United States',
            'UK': 'United Kingdom',
            'South Korea': 'Korea',
            'Espana': 'Spain',
            'Taiwan,China': 'China'
        }
        def clean_country_name(name):
            """清洗国家名称"""
            name = re.sub(r'[\r\n]', '', name.strip())  # 去除换行和首尾空格
            name = re.sub(r'，', ',', name)  # 替换中文逗号
            return COUNTRY_MAPPING.get(name, name)

        NON_COUNTRIES = {'Gothenburg', 'Istanbul', 'Scotland', 'Northern Ireland'}

        form = ana_cd_form()
        tests = PftdDecisionIndicator.objects.raw(
            "select id, Region as region, count(*) as count from(select id, pmid,Region from pftd_decision_indicator GROUP BY pmid) as temp GROUP BY Region")


        res = []
        dis_array = []
        for i in tests:
            if ";" in i.region:
                temp = i.region.split(";")


                for j in temp:
                    cleaned = clean_country_name(j)
                    if cleaned and cleaned not in NON_COUNTRIES:  # 新增过滤
                        if cleaned not in dis_array:
                            dis_array.append(cleaned)
                            res.append({'name': cleaned, 'count': i.count})
                        else:
                            for k in res:
                                if k["name"] == cleaned:
                                    k["count"] += i.count
            else:
                cleaned = clean_country_name(i.region)
                if cleaned and cleaned not in NON_COUNTRIES:  # 新增过滤
                    if cleaned not in dis_array:
                        dis_array.append(cleaned)
                        res.append({'name': cleaned, 'count': i.count})
                    else:
                        for k in res:
                            if k["name"] == cleaned:
                                k["count"] += i.count
        print(res)
        # print(tests)
        return render(request, "analysis/analysis_cd.html", {'data': res, "form": form})


    if request.method == 'POST':
        form = ana_cd_form(data=request.POST)
        if form.is_valid():
            category = form.cleaned_data.get("category_cd")
            options2 = request.POST.getlist("name")
            # print(options2)
            name = ",".join(options2)
            res = "——【" + name + "】"
            # if options2 == 'M&F':
            #     temp = 'M and F'
            #     res = "——【" + temp + "】"
            # else:
            #     res = "——【" + options2 + "】"
            # 根据options生成特定的检索式
            search_temp = ""
            if len(options2) == 1:
                if options2[-1] == 'Other surgeries':
                    search_temp = "(surgery_type LIKE '%%Non-cardiac surgery%%' OR surgery_type LIKE '%%post-endoscopic retrograde cholangiopancreatography(ERCP)%%'" \
                                  "OR surgery_type LIKE '%%urgent PCI%%'OR surgery_type LIKE '%%Oncosurgery%%'" \
                                  "OR surgery_type = 'NA'OR surgery_type LIKE '%%other surgery%%'" \
                                  "OR surgery_type LIKE '%%other surgeries%%' )"
                elif options2[-1] == 'Cardiac surgery':
                    search_temp = "( surgery_type= '" + options2[-1] + "')"
                else:
                    search_temp += category + " LIKE '%%" + options2[-1] + "%%'"
            elif len(options2) == 0:
                form = ana_cd_form()
                tests = PftdDecisionIndicator.objects.raw(
                    "select id, Region as region, count(*) as count from(select id, pmid,Region from pftd_decision_indicator GROUP BY pmid) as temp GROUP BY Region")
                res = []
                dis_array = []
                for i in tests:
                    if ";" in i.region:
                        temp = i.region.split(";")
                        for j in temp:
                            if j not in dis_array:
                                dis_array.append(j)
                                dic_temp = {}
                                dic_temp['name'] = j
                                dic_temp['count'] = i.count
                                res.append(dic_temp)
                    else:
                        if i.region not in dis_array:
                            dis_array.append(i)
                            dic_temp = {}
                            dic_temp['name'] = i.region
                            dic_temp['count'] = i.count
                            res.append(dic_temp)
                        else:
                            for k in res:
                                if k["name"] == i.region:
                                    k["count"] += int(i.count)
                # print(res)
                # print(tests)
                return render(request, "analysis/analysis_cd.html", {'data': res, "form": form})
            else:
                for i in range(0, len(options2) - 1):
                    if options2[i] == 'Other surgeries':
                        temp = "(surgery_type LIKE '%%Non-cardiac surgery%%' OR surgery_type LIKE '%%post-endoscopic retrograde cholangiopancreatography(ERCP)%%'" \
                               "OR surgery_type LIKE '%%urgent PCI%%'OR surgery_type LIKE '%%Oncosurgery%%'" \
                               "OR surgery_type = 'NA'OR surgery_type LIKE '%%other surgery%%'" \
                               "OR surgery_type LIKE '%%other surgeries%%' ) OR "
                        search_temp += temp
                    if options2[i] == 'Cardiac surgery':
                        temp = "( surgery_type= '" + options2[i] + "') OR "
                        search_temp += temp
                    else:
                        temp = category + " LIKE '%%" + options2[i] + "%%' OR "
                        search_temp += temp
                search_temp += category + " LIKE '%%" + options2[-1] + "%%'"
            tests = PftdDecisionIndicator.objects.raw(
                "select id, Region as region, count(*) as count from(select id, pmid,Region from pftd_decision_indicator  where " + search_temp + " GROUP BY pmid) as temp GROUP BY Region")
            res2 = []
            dis_array = []
            for i in tests:
                if ";" in i.region:
                    temp = i.region.split(";")
                    for j in temp:
                        if j not in dis_array:
                            dis_array.append(j)
                            dic_temp = {}
                            dic_temp['name'] = j
                            dic_temp['count'] = i.count
                            res2.append(dic_temp)
                else:
                    if i.region not in dis_array:
                        dis_array.append(i)
                        dic_temp = {}
                        dic_temp['name'] = i.region
                        dic_temp['count'] = i.count
                        res2.append(dic_temp)
                    else:
                        for k in res2:
                            if k["name"] == i.region:
                                k["count"] += int(i.count)
            # print(tests)

            return render(request, "analysis/analysis_cd.html", {"form": form, 'data': res2, 'option': res})
        else:

            return render(request, "analysis/analysis_cd.html", {"form": form})


def get_geodata(request):
    with open('app01/static/js/world.json') as data:
        geodata = json.load(data)
        # print(geodata)
        # return HttpResponse(geodata,content_type='application/json')
        return HttpResponse(json.dumps(geodata, separators=(',', ':')), content_type='application/json')


'''
 Analysis for Sankey 
'''
class ana_sankey_form(forms.Form):
    type_choices = (
        ("surgery_type", "Surgical Type"),
        ("period_of_fluid_therapy", "Period of Fluid Therapy Protocol"),
        ("application", "Application"),

    )
    category = forms.ChoiceField(label="Category_sankey",
                                 widget=forms.Select(
                                     attrs={"class": "selectpicker", "id": "user2", "data-live-search": "true",
                                            "data-size": "5",
                                            "title": "Choose one of the following...",
                                            "onchange": "selectOnchange(this)"}),
                                 choices=type_choices, required=True)


def update_links(links, source, target, value):
    for link in links:
        if link['source'] == source and link['target'] == target:
            link['value'] += value
            return
    else:
        links.append({'source': source, 'target': target, 'value': value})


def dfs(visited, graph, node, parent, recursion_stack):
    visited[node] = True
    recursion_stack[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            if dfs(visited, graph, neighbour, node, recursion_stack):
                return True
        elif recursion_stack[neighbour]:
            print(f"Found a cycle: {parent} -> {node} -> {neighbour}")
            return True
    recursion_stack[node] = False
    return False


def detect_cycles(links):
    graph = {}
    visited = {}
    recursion_stack = {}

    # Construct the graph
    for link in links:
        source = link['source']
        target = link['target']
        if source not in graph:
            graph[source] = []
        if target not in graph:
            graph[target] = []
        graph[source].append(target)

    # Initialize visited and recursion stack
    for node in graph.keys():
        visited[node] = False
        recursion_stack[node] = False

    # Call the recursive helper function to detect cycle in different DFS trees
    for node in graph.keys():
        if not visited[node]:
            if dfs(visited, graph, node, None, recursion_stack):
                return True

    return False


def clean_and_split(value, filter_options=None):
    """清理字符串并按分号分割，返回标题格式的列表。"""
    # if not value:
    #     return []
    # return [item.strip().title() for item in value.split(';') if item.strip()]
    if not value:
        return []
    items = [item.strip().title() for item in value.split(';') if item.strip()]
    if filter_options:
        # 将filter_options中的值也转换为标题格式以确保匹配
        filter_options = [option.title() for option in filter_options]
        items = [item for item in items if item in filter_options]
    return items


def process_entries(search_res, field1, field2, links, category=None, options2=None):
    """处理条目并更新链接。"""
    # for entry in search_res:
    #     items1 = clean_and_split(getattr(entry, field1),options)
    #     items2 = clean_and_split(getattr(entry, field2),options)
    #
    #     if not items1:
    #         items1 = ['Unknown']  # 为缺失数据提供默认值
    #     if not items2:
    #         items2 = ['Unknown']
    #
    #     for item1 in items1:
    #         for item2 in items2:
    #             update_links(links, item1, item2, entry.value)
    for entry in search_res:
        filter_options1 = options2 if category == field1 else None
        filter_options2 = options2 if category == field2 else None
        items1 = clean_and_split(getattr(entry, field1), filter_options1)
        items2 = clean_and_split(getattr(entry, field2), filter_options2)

        if not items1:
            items1 = ['Unknown']  # 为缺失数据提供默认值
        if not items2:
            items2 = ['Unknown']

        for item1 in items1:
            for item2 in items2:
                update_links(links, item1, item2, entry.value)


def ana_sankey(request):
    if request.method == 'GET':
        form = ana_sankey_form()
        data = []  # 存储节点数据
        links = []  # 存储关系数据
        first_level = PftdDecisionIndicator.objects.exclude(surgery_type='NA').values('surgery_type').distinct()
        for i in first_level:
            if ";" in i["surgery_type"]:
                temp = i["surgery_type"].split(";")
                for j in temp:
                    data.append(j)
            elif "；" in i["surgery_type"]:
                temp = i["surgery_type"].split("；")
                for j in temp:
                    data.append(j)
            elif "," in i["surgery_type"]:
                temp = i["surgery_type"].split(",")
                for j in temp:
                    data.append(j)
            elif ", " in i["surgery_type"]:
                temp = i["surgery_type"].split(", ")
                for j in temp:
                    data.append(j)
            else:
                data.append(i["surgery_type"])
            # dic = {}
            # dic['name'] = i.surgery_type
            # data.append(dic)
        second_level = PftdDecisionIndicator.objects.exclude(period_of_fluid_therapy='NA').values(
            'period_of_fluid_therapy').distinct()
        for i in second_level:
            if ";" in i["period_of_fluid_therapy"]:
                temp = i["period_of_fluid_therapy"].split(";")
                for j in temp:
                    data.append(j)
            else:
                data.append(i["period_of_fluid_therapy"])
        third_level = PftdDecisionIndicator.objects.exclude(application='NA').values('application').distinct()
        for i in third_level:
            if ";" in i["application"]:
                temp = i["application"].split(";")
                for j in temp:
                    data.append(j)
            elif "；" in i["application"]:
                temp = i["application"].split("；")
                for j in temp:
                    data.append(j)
            elif "," in i["application"]:
                temp = i["application"].split(",")
                for j in temp:
                    data.append(j)
            elif ", " in i["application"]:
                temp = i["application"].split(", ")
                for j in temp:
                    data.append(j)
            else:
                data.append(i["application"])

        forth_level = PftdDecisionIndicator.objects.exclude(parameters='NA').values('parameters').distinct()
        for i in forth_level:
            if ";" in i["parameters"]:
                temp = i["parameters"].split(";")
                for j in temp:
                    data.append(j)
            else:
                data.append(i["parameters"])
        data = [item.strip().title() for item in data if item.strip()]

        data = list(set(data))
        # 获取各level间的关系数据

        test1 = PftdDecisionIndicator.objects.raw(
            "SELECT id, surgery_type,period_of_fluid_therapy,count(*) as value FROM pftd_decision_indicator GROUP BY surgery_type,Period_of_fluid_therapy HAVING surgery_type != 'NA'")
        for entry in test1:
            surgery_types = [surgery.strip().title() for surgery in entry.surgery_type.split(';')]
            therapies = [therapy.strip().title() for therapy in entry.period_of_fluid_therapy.split(';')]

            if ';' in entry.surgery_type and ';' not in entry.period_of_fluid_therapy:
                for surgery in surgery_types:
                    update_links(links, surgery, entry.period_of_fluid_therapy.strip().title(), entry.value)
            elif ';' not in entry.surgery_type and ';' in entry.period_of_fluid_therapy:
                for therapy in therapies:
                    update_links(links, entry.surgery_type.strip().title(), therapy, entry.value)
            elif ';' in entry.surgery_type and ';' in entry.period_of_fluid_therapy:
                for surgery in surgery_types:
                    for therapy in therapies:
                        update_links(links, surgery, therapy, entry.value)
            else:
                update_links(links, entry.surgery_type.strip().title(), entry.period_of_fluid_therapy.strip().title(),
                             entry.value)

        test2 = PftdDecisionIndicator.objects.raw(
            "SELECT id, period_of_fluid_therapy,Application ,count(*) as value FROM pftd_decision_indicator GROUP BY Period_of_fluid_therapy,Application HAVING Application != 'NA'")
        for entry in test2:
            applications = [application.strip().title() for application in entry.application.split(';')]
            therapies = [therapy.strip().title() for therapy in entry.period_of_fluid_therapy.split(';')]

            if ';' in entry.period_of_fluid_therapy and ';' not in entry.application:
                for therapy in therapies:
                    update_links(links, therapy, entry.application.strip().title(), entry.value)
            elif ';' not in entry.period_of_fluid_therapy and ';' in entry.application:
                for app in applications:
                    update_links(links, entry.period_of_fluid_therapy.strip().title(), app, entry.value)
            elif ';' in entry.application and ';' in entry.period_of_fluid_therapy:
                for therapy in therapies:
                    for application in applications:
                        update_links(links, therapy, application, entry.value)
            else:
                update_links(links, entry.period_of_fluid_therapy.strip().title(), entry.application.strip().title(),
                             entry.value)

        test3 = PftdDecisionIndicator.objects.raw(
            "SELECT id,Application,Parameters,count(*) as value FROM pftd_decision_indicator GROUP BY Application,Parameters HAVING Application != 'NA' and Parameters != 'NA'")
        for entry in test3:
            applications = [application.strip().title() for application in entry.application.split(';')]
            parameters = [para.strip().title() for para in entry.parameters.split(';')]

            if ';' in entry.application and ';' not in entry.parameters:
                for application in applications:
                    update_links(links, application, entry.parameters.strip().title(), entry.value)
            elif ';' not in entry.application and ';' in entry.parameters:
                for para in parameters:
                    update_links(links, entry.application.strip().title(), para, entry.value)
            elif ';' in entry.application and ';' in entry.parameters:
                for application in applications:
                    for para in parameters:
                        update_links(links, application, para, entry.value)
            else:
                update_links(links, entry.application.strip().title(), entry.parameters.strip().title(), entry.value)

        print(data)
        print(links)

        # Now call the function with your links
        has_cycle = detect_cycles(links)
        print(f"Does the graph have a cycle? {has_cycle}")
        return render(request, "analysis/analysis_di_sankey.html", {'data': data, 'links': links, "form": form})
    if request.method == 'POST':
        form = ana_sankey_form(data=request.POST)
        if form.is_valid():
            category = form.cleaned_data.get("category")
            options2 = request.POST.getlist("name")
            name = ",".join(options2)
            res = "——【" + name + "】"

            search_temp = ""
            if len(options2) == 1:
                search_temp += category + " LIKE '%%" + options2[-1] + "%%'"


            else:
                for i in range(0, len(options2) - 1):
                    temp = category + " LIKE '%%" + options2[i] + "%%' OR "
                    search_temp += temp
                search_temp += category + " LIKE '%%" + options2[-1] + "%%'"

            data = []  # 存储节点数据
            links = []  # 存储关系数据

            search_res = PftdDecisionIndicator.objects.raw(
                "SELECT id, surgery_type,Period_of_fluid_therapy,Application,Parameters,count(*) as value FROM pftd_decision_indicator"
                " where " + search_temp +
                " GROUP BY surgery_type,Period_of_fluid_therapy,Application,Parameters HAVING surgery_type != 'NA' ")

            # 处理不同的字段组合
            process_entries(search_res, 'surgery_type', 'period_of_fluid_therapy', links, category, options2)
            process_entries(search_res, 'period_of_fluid_therapy', 'application', links, category, options2)
            process_entries(search_res, 'application', 'parameters', links, category, options2)

            # 从链接中提取唯一数据项
            data = list(set([link['source'] for link in links] + [link['target'] for link in links]))

            print(data)
            print(links)

            # 检测循环
            has_cycle = detect_cycles(links)
            print(f"Does the graph have a cycle? {has_cycle}")
            return render(request, "analysis/analysis_di_sankey.html",
                          {'data': data, 'links': links, "form": form, 'option': res})
        else:
            return render(request, "analysis/analysis_di_sankey.html",
                          {"form": form})


'''
 Analysis for Pie
'''


def create_node(name, value=None, children=None):
    node = {'name': name}
    if value is not None:
        node['value'] = 1
    if children is not None:
        node['children'] = children
    return node


def build_tree(data):
    root = {}
    for entry in data:
        current_node = root
        for name in entry:
            found_child = None
            if 'children' in current_node:
                for child in current_node['children']:
                    if child['name'] == name:
                        found_child = child
                        break
            if found_child is None:
                new_child = create_node(name)
                current_node.setdefault("children", []).append(new_child)
                current_node = new_child
            else:
                current_node = found_child
        current_node['value'] = 1
    return root.get('children', [])


# def generate_data(raw_out,cla,app,para):


def ana_pie(request):
    if request.method == 'GET':
        raw_out = []
        test = PftdDecisionIndicator.objects.raw(
            "SELECT id,Classification_of_fluid_therapy_Parameters,Application,Parameters FROM pftd_decision_indicator GROUP BY Classification_of_fluid_therapy_Parameters,Application,Parameters")

        for i in test:
            raw_in = []
            classes = [class1.strip().title() for class1 in i.classification_of_fluid_therapy_parameters.split(';')]
            apps = []
            if ";" in i.application:
                temp = i.application.split(";")
                for j in temp:
                    apps.append(j.strip().title())
            elif "；" in i.application:
                temp = i.application.split("；")
                for j in temp:
                    apps.append(j.strip().title())
            elif "," in i.application:
                temp = i.application.split(",")
                for j in temp:
                    apps.append(j.strip().title())
            elif ", " in i.application:
                temp = i.application.split(", ")
                for j in temp:
                    apps.append(j.strip().title())
            else:
                apps.append(i.application.strip().title())

            # apps = [app.strip().title() for app in i.application.split(';')]
            paras = []
            paras.append(i.parameters.strip())
            # paras = [para.strip().title() for para in i.parameters.split(';')]

            for cla in classes:
                for app in apps:
                    for para in paras:
                        raw_in.append(cla)
                        raw_in.append(app)
                        raw_in.append(para)
                        raw_out.append(raw_in)
                        raw_in = []
            #
            # if ";" in i.application:
            #     temp = i.application.split("; ")
            #     for j in temp:
            #         raw_in.append(i.classification_of_fluid_therapy_parameters)
            #         raw_in.append(j)
            #         raw_in.append(i.parameters)
            #         raw_out.append(raw_in)
            #         raw_in = []
            # elif ";" in i.application:
            #     temp = i.application.split(";")
            #     for j in temp:
            #         raw_in.append(i.classification_of_fluid_therapy_parameters)
            #         raw_in.append(j)
            #         raw_in.append(i.parameters)
            #         raw_out.append(raw_in)
            #         raw_in = []
            # else:
            #     raw_in.append(i.classification_of_fluid_therapy_parameters)
            #     raw_in.append(i.application)
            #     raw_in.append(i.parameters)
            #     raw_out.append(raw_in)

        unique_tuples = set(tuple(item) for item in raw_out)

        # 将集合转换回列表的列表
        unique_nested_list = [list(item) for item in unique_tuples]
        print(unique_nested_list)
        result = build_tree(unique_nested_list)

        # print(result)
        # last_res = format_data(raw_out)
        # print(last_res)

        # pie = Pie(i.classification_of_fluid_therapy_parameters)
        # pie.children.append(Pie(i.application).children.append(Pie(i.parameters)))
        return render(request, "analysis/analysis_di_circle.html", {"test": json.dumps(result)})


'''
 Analysis for Graph
'''


def change_size(value):
    if 1 <= value <= 10:
        return 10
    elif 10 < value <= 20:
        return 15
    elif 20 < value <= 40:
        return 25
    elif 40 < value <= 70:
        return 35
    elif 70 < value <= 100:
        return 45
    else:
        return 55


def ana_graph(request):
    nodes = []
    links = []
    categories = ['surgery_type', 'iftp', 'iftp_subgroup', 'parameter']
    type = []
    for i in categories:
        type_dic = {"name": i}
        type.append(type_dic)

    '''
    获取节点信息共8种节点
    '''
    test1 = Pftd.objects.raw(
        "SELECT id, surgery_type,COUNT(*) as value from pftd GROUP BY surgery_type"
    )
    st_array = []
    for i in test1:
        if ";" in i.surgery_type:
            temp = i.surgery_type.split(";")
            for j in temp:
                if j not in st_array:
                    st_array.append(j)
                    node_dic = {}
                    node_dic["id"] = j + "-st"
                    node_dic["name"] = j
                    node_dic["value"] = i.value
                    node_dic["category"] = "surgery_type"
                    node_dic["symbolSize"] = change_size(i.value)
                    nodes.append(node_dic)
                else:
                    for k in nodes:
                        if k["name"] == j:
                            k["value"] += int(i.value)
                            k["symbolSize"] = change_size(k["value"])
        else:
            if i.surgery_type not in st_array:
                st_array.append(i.surgery_type)
                node_dic = {}
                node_dic["id"] = i.surgery_type + "-st"
                node_dic["name"] = i.surgery_type
                node_dic["value"] = i.value
                node_dic["category"] = "surgery_type"
                node_dic["symbolSize"] = change_size(i.value)
                nodes.append(node_dic)
            else:
                for k in nodes:
                    if k["name"] == i.surgery_type:
                        k["value"] += int(i.value)
                        k["symbolSize"] = change_size(k["value"])

    test2 = Pftd.objects.raw(
        "SELECT id,  IFTP,COUNT(*) as value from pftd GROUP BY IFTP"
    )
    for i in test2:
        node_dic = {}
        node_dic["id"] = i.iftp + "-iftp"
        node_dic["name"] = i.iftp
        node_dic["value"] = i.value
        node_dic["category"] = "iftp"
        node_dic["symbolSize"] = change_size(i.value)
        nodes.append(node_dic)
    test3 = Pftd.objects.raw(
        "SELECT id,  IFTP_subgroup ,COUNT(*) as value from pftd GROUP BY IFTP_subgroup"
    )
    for i in test3:
        node_dic = {}
        node_dic["id"] = i.iftp_subgroup + "-sub"
        node_dic["name"] = i.iftp_subgroup
        node_dic["value"] = i.value
        node_dic["category"] = "iftp_subgroup"
        node_dic["symbolSize"] = change_size(i.value)
        nodes.append(node_dic)

    para_array = []
    test4 = Pftd.objects.raw(
        "SELECT id,  Parameter1 ,COUNT(*) as value from pftd GROUP BY Parameter1 HAVING Parameter1 !='NA'"
    )
    for i in test4:
        node_dic = {}
        node_dic["id"] = i.parameter1 + "-p"
        node_dic["name"] = i.parameter1
        node_dic["value"] = i.value
        node_dic["category"] = "parameter"
        node_dic["symbolSize"] = change_size(i.value)
        nodes.append(node_dic)
        para_array.append(i.parameter1)

    test5 = Pftd.objects.raw(
        "SELECT id,  Parameter2 ,COUNT(*) as value from pftd GROUP BY Parameter2 HAVING Parameter2 !='NA'"
    )
    for i in test5:
        if i.parameter2 in para_array:
            for k in nodes:
                if k['name'] == i.parameter2:
                    k['value'] += i.value
                    k["symbolSize"] = change_size(k["value"])
        else:
            para_array.append(i.parameter2)
            node_dic = {}
            node_dic["id"] = i.parameter2 + "-p"
            node_dic["name"] = i.parameter2
            node_dic["value"] = i.value
            node_dic["category"] = "parameter"
            node_dic["symbolSize"] = change_size(i.value)
            nodes.append(node_dic)
    test6 = Pftd.objects.raw(
        "SELECT id,  Parameter3 ,COUNT(*) as value from pftd GROUP BY Parameter3 HAVING Parameter3 !='NA'"
    )
    for i in test6:
        if i.parameter3 in para_array:
            for k in nodes:
                if k['name'] == i.parameter3:
                    k['value'] += i.value
                    k["symbolSize"] = change_size(k["value"])
        else:
            para_array.append(i.parameter3)
            node_dic = {}
            node_dic["id"] = i.parameter3 + "-p"
            node_dic["name"] = i.parameter3
            node_dic["value"] = i.value
            node_dic["category"] = "parameter"
            node_dic["symbolSize"] = change_size(i.value)
            nodes.append(node_dic)
    test7 = Pftd.objects.raw(
        "SELECT id,  Parameter4 ,COUNT(*) as value from pftd GROUP BY Parameter4 HAVING Parameter4 !='NA'"
    )
    for i in test7:
        if i.parameter4 in para_array:
            for k in nodes:
                if k['name'] == i.parameter4:
                    k['value'] += i.value
                    k["symbolSize"] = change_size(k["value"])
        else:
            para_array.append(i.parameter4)
            node_dic = {}
            node_dic["id"] = i.parameter4 + "-p"
            node_dic["name"] = i.parameter4
            node_dic["value"] = i.value
            node_dic["category"] = "parameter"
            node_dic["symbolSize"] = change_size(i.value)
            nodes.append(node_dic)
    test8 = Pftd.objects.raw(
        "SELECT id,  Parameter5 ,COUNT(*) as value from pftd GROUP BY Parameter5 HAVING Parameter5 !='NA'"
    )
    for i in test8:
        if i.parameter5 in para_array:
            for k in nodes:
                if k['name'] == i.parameter5:
                    k['value'] += i.value
                    k["symbolSize"] = change_size(k["value"])
        else:
            para_array.append(i.parameter5)
            node_dic = {}
            node_dic["id"] = i.parameter5 + "-p"
            node_dic["name"] = i.parameter5
            node_dic["value"] = i.value
            node_dic["category"] = "parameter"
            node_dic["symbolSize"] = change_size(i.value)
            nodes.append(node_dic)
    # 去重
    node_ids = set()
    for node in nodes:
        node_id = node['id']
        if node_id in node_ids:
            print(f"Duplicate node id found: {node_id}")
        node_ids.add(node_id)
    # nodes = [dict(t) for t in set([tuple(d.items()) for d in nodes])]

    print(nodes)
    '''
    整理八种节点间关系
    '''
    # 'surgery_type - IFTP'
    link_info1 = Pftd.objects.raw(
        "SELECT id, surgery_type,IFTP from pftd GROUP BY surgery_type,IFTP"
    )
    for i in link_info1:
        if ";" in i.surgery_type:
            temp = i.surgery_type.split(";")
            for j in temp:
                link_dic = {}
                link_dic["source"] = j + "-st"
                link_dic["target"] = i.iftp + "-iftp"
                links.append(link_dic)
        else:
            link_dic = {}
            link_dic["source"] = i.surgery_type + "-st"
            link_dic["target"] = i.iftp + "-iftp"
            links.append(link_dic)

    # 'IFTP -IFTP_subgroup'
    link_info2 = Pftd.objects.raw(
        "SELECT id, IFTP,IFTP_subgroup from pftd"
    )
    for i in link_info2:
        link_dic = {}
        link_dic["source"] = i.iftp + "-iftp"
        link_dic["target"] = i.iftp_subgroup + "-sub"
        links.append(link_dic)

    # 'IFTP_subgroup - parameter'
    link_info3 = Pftd.objects.raw(
        "SELECT id, IFTP_subgroup as sp,Parameter1 as p1,Parameter2 as p2,Parameter3 as p3,Parameter4 as p4,Parameter5 as p5 from pftd GROUP BY sp,p1,p2,p3,p4,p5"
    )
    for i in link_info3:
        if i.p1 == "NA":
            continue
        else:
            link_dic = {}
            link_dic["source"] = i.sp + "-sub"
            link_dic["target"] = i.p1 + "-p"
            links.append(link_dic)
        if i.p2 == "NA":
            continue
        else:
            link_dic1 = {}
            link_dic1["source"] = i.sp + "-sub"
            link_dic1["target"] = i.p2 + "-p"
            links.append(link_dic1)
        if i.p3 == "NA":
            continue
        else:
            link_dic2 = {}
            link_dic2["source"] = i.sp + "-sub"
            link_dic2["target"] = i.p3 + "-p"
            links.append(link_dic2)
        if i.p4 == "NA":
            continue
        else:
            link_dic3 = {}
            link_dic3["source"] = i.sp + "-sub"
            link_dic3["target"] = i.p4 + "-p"
            links.append(link_dic3)
        if i.p5 == "NA":
            continue
        else:
            link_dic4 = {}
            link_dic4["source"] = i.sp + "-sub"
            link_dic4["target"] = i.p5 + "-p"
            links.append(link_dic4)

    # 'IFTP - parameter'
    # link_info4 = Pftd.objects.raw(
    #     "SELECT id, IFTP as sp,Parameter1 as p1,Parameter2 as p2,Parameter3 as p3,Parameter4 as p4,Parameter5 as p5 from pftd GROUP BY sp,p1,p2,p3,p4,p5"
    # )
    # for i in link_info4:
    #     if i.p1 == "NA":
    #         continue
    #     else:
    #         link_dic = {}
    #         link_dic["source"] = i.sp+"-iftp"
    #         link_dic["target"] = i.p1+"-p1"
    #         links.append(link_dic)
    #     if i.p2 == "NA":
    #         continue
    #     else:
    #         link_dic1 = {}
    #         link_dic1["source"] = i.sp+"-iftp"
    #         link_dic1["target"] = i.p2+"-p2"
    #         links.append(link_dic1)
    #     if i.p3 == "NA":
    #         continue
    #     else:
    #         link_dic2 = {}
    #         link_dic2["source"] = i.sp+"-iftp"
    #         link_dic2["target"] = i.p3+"-p3"
    #         links.append(link_dic2)
    #     if i.p4 == "NA":
    #         continue
    #     else:
    #         link_dic3 = {}
    #         link_dic3["source"] = i.sp+"-iftp"
    #         link_dic3["target"] = i.p4+"-p4"
    #         links.append(link_dic3)
    #     if i.p5 == "NA":
    #         continue
    #     else:
    #         link_dic4 = {}
    #         link_dic4["source"] = i.sp+"-iftp"
    #         link_dic4["target"] = i.p5+"-p5"
    #         links.append(link_dic4)

    # 去重操作
    link_pairs = set()
    for link in links:
        link_pair = (link['source'], link['target'])
        # if link_pair in link_pairs:
        #     print(f"Duplicate link found between source: {link['source']} and target: {link['target']}")
        link_pairs.add(link_pair)
    # links = [dict(t) for t in set([tuple(d.items()) for d in links])]
    # print(links)
    return render(request, "analysis/analysis_graph.html",
                  {"nodes": json.dumps(nodes), "links": json.dumps(links), "type": json.dumps(type)})


'''
 Analysis for Sample Size and Year Line
'''


class ana_sy_form(forms.Form):
    type_choices2 = (
        # ('surgery_type', 'Surgical Type'),
        # ('region', 'Region'),
        # # ("race", "Race"),
        # ("gender", "Gender"),
        # ("age", "Age"),
        # ("bmi", "BMI"),
        # ("surgical_approach", "Surgery Approach"),
        # # ("surgical_site", "Surgical Site"),
        # ("period_of_fluid_therapy", "Period of Fluid Therapy"),
        # # ("disease", "Disease"),
        # # ("comorbidity", "Comorbidity"),
        # # ("fluid_therapy_concept", "Fluid Therapy Concept"),
        ("surgery_type", "Surgical Type"),
        ("age", "Population"),
        # ("gender", "Gender"),
        ("asa_physical_status", "ASA physical status"),
        # ("bmi", "BMI"),
        ("surgical_approach", "Surgery Approach"),

        ("period_of_fluid_therapy", "Period of Fluid Therapy"),
        ("classification_of_fluid_therapy_parameters", "Classification of PFTD parameters"),
        ("application", "Parameter Application"),

    )
    category_cd = forms.ChoiceField(label="Category",
                                    widget=forms.Select(
                                        attrs={"class": "form-control"}),
                                    choices=type_choices2)


def ana_sy_line(request):
    if request.method == 'GET':
        form = ana_sy_form()
        option = 'Surgery Type'
        years = {}
        x = []
        surgery_type = []
        # 获取年份及其位置的字典
        years_res = PftdDecisionIndicator.objects.values('year').distinct().order_by("year")
        # print(years_res)
        temp = 0
        for i in years_res:
            x.append(i["year"])
            years[i["year"]] = temp
            temp += 1
        # print(years)
        res = []

        data_st = PftdDecisionIndicator.objects.raw(
            "SELECT id, `Year`,surgery_type as name,SUM(Sample_Size) as value from (SELECT id, pmid,`Year`,surgery_type,Sample_Size FROM pftd_decision_indicator GROUP BY pmid,`Year`,surgery_type,Sample_Size) as test GROUP BY `Year`,surgery_type"
        )
        for i in data_st:
            if i.name is None or i.name == 'Na' or i.name == "":
                continue
            elif ";" in i.name:
                split_temp = i.name.split(";")
                for item in split_temp:
                    if item is None or item == "" or item == 'Na':
                        continue
                    name = item.strip().title()
                    if item.strip().title() not in surgery_type:
                        dic_temp = {
                            "name": '',
                            "type": 'line',
                            # "stack":'Total',
                            "data": [0] * len(years)
                        }
                        surgery_type.append(name)
                        dic_temp["name"] = name
                        dic_temp["data"][years[i.year]] = int(i.value)
                        res.append(dic_temp)
                    else:
                        for j in res:
                            if j["name"] == name:
                                j["data"][years[i.year]] += int(i.value)
            else:
                name = i.name.strip().title()
                dic_temp = {
                    "name": '',
                    "type": 'line',
                    # "stack":'Total',
                    "data": [0] * len(years)
                }
                if name not in surgery_type:
                    surgery_type.append(name)
                    dic_temp["name"] = name
                    dic_temp["data"][years[i.year]] = int(i.value)
                    res.append(dic_temp)

                else:
                    for j in res:
                        if j["name"] == name.strip().title():
                            j["data"][years[i.year]] += int(i.value)

        seen = set()
        surgery_type = [x for x in surgery_type if x not in seen and not seen.add(x) and x not in [None, ""]]

        # 现在 surgery_type 不包含 None, 空字符串或 'Na'
        # 我们可以计算 'Na' 的数量然后在末尾添加相应数量的 'Na'
        na_count = surgery_type.count('Na')

        # 移除所有的 'Na'
        surgery_type = [x for x in surgery_type if x != 'Na']

        # 在列表末尾添加回 'Na' 元素
        surgery_type.extend(['Na'] * na_count)

        # print(surgery_type)
        # print(res)

        return render(request, "analysis/analysis_sy_line.html",
                      {"type": json.dumps(surgery_type), "x": json.dumps(x), "res": json.dumps(res), 'title': option,
                       'form': form})
    if request.method == 'POST':
        form = ana_sy_form(data=request.POST)
        if form.is_valid():
            category = form.cleaned_data.get("category_cd")
            # print(category)
            years = {}
            x = []
            surgery_type = []
            # 获取年份及其位置的字典
            years_res = PftdDecisionIndicator.objects.values('year').distinct().order_by("year")
            # print(years_res)
            temp = 0
            for i in years_res:
                x.append(i["year"])
                years[i["year"]] = temp
                temp += 1

            # print(years)
            res = []

            data_st = PftdDecisionIndicator.objects.raw(
                "SELECT id, `Year`," + category + " as name,SUM(Sample_Size) as value from (SELECT id, pmid,`Year`," + category + ",Sample_Size FROM pftd_decision_indicator GROUP BY pmid,`Year`," + category + ",Sample_Size) as test GROUP BY " + category + ",`Year`"
            )
            for i in data_st:
                if i.name is None or i.name == 'Na' or i.name == "":
                    continue
                if ";" in i.name:
                    split_temp = i.name.split(";")
                    for item in split_temp:
                        if item is None or item == "" or item == 'Na':
                            continue
                        name = item.strip().title()
                        if item.strip().title() not in surgery_type:
                            dic_temp = {
                                "name": '',
                                "type": 'line',
                                # "stack":'Total',
                                "data": [0] * len(years)
                            }
                            surgery_type.append(name)
                            dic_temp["name"] = name
                            dic_temp["data"][years[i.year]] = int(i.value)
                            res.append(dic_temp)
                        else:
                            for j in res:
                                if j["name"] == name:
                                    j["data"][years[i.year]] += int(i.value)
                else:
                    name = i.name.strip().title()
                    dic_temp = {
                        "name": '',
                        "type": 'line',
                        # "stack":'Total',
                        "data": [0] * len(years)
                    }
                    if name not in surgery_type:
                        surgery_type.append(name)
                        dic_temp["name"] = name
                        dic_temp["data"][years[i.year]] = int(i.value)
                        res.append(dic_temp)

                    else:
                        for j in res:
                            if j["name"] == name:
                                j["data"][years[i.year]] += int(i.value)
            if category == 'period_of_fluid_therapy':
                seen = set()
                temp_list = ['Preoperative', 'Intraoperative', 'Postoperative']
                surgery_type = [x for x in surgery_type if x not in seen and not seen.add(x) and x not in [None, ""]]
                # 使用 temp_list 的顺序对 surgery_type 进行排序
                surgery_type_sorted = sorted(surgery_type,
                                             key=lambda x: temp_list.index(x) if x in temp_list else len(temp_list))

                # surgery_type_sorted 现在是根据 temp_list 排序的列表
                surgery_type = surgery_type_sorted

            elif category == 'classification_of_fluid_therapy_parameters':
                seen = set()
                temp_list = ["Hemodynamic Parameters", "Physiological Factors", "Laboratory Tests",
                             "Volume Loss Factors"
                    , "Vital Signs", "Intake Factors", "Clinical Signs", "Insensible Losses", "Physical Examinations"
                    , "Complications", "Treatment Information", "Other Factors"]
                surgery_type = [x for x in surgery_type if x not in seen and not seen.add(x) and x not in [None, ""]]
                # 使用 temp_list 的顺序对 surgery_type 进行排序
                surgery_type_sorted = sorted(surgery_type,
                                             key=lambda x: temp_list.index(x) if x in temp_list else len(temp_list))

                # surgery_type_sorted 现在是根据 temp_list 排序的列表
                surgery_type = surgery_type_sorted
            else:
                seen = set()
                surgery_type = [x for x in surgery_type if x not in seen and not seen.add(x) and x not in [None, ""]]

                # 现在 surgery_type 不包含 None, 空字符串或 'Na'
                # 我们可以计算 'Na' 的数量然后在末尾添加相应数量的 'Na'
                na_count = surgery_type.count('Na')

                # 移除所有的 'Na'
                surgery_type = [x for x in surgery_type if x != 'Na']

                # 在列表末尾添加回 'Na' 元素
                surgery_type.extend(['Na'] * na_count)

            return render(request, "analysis/analysis_sy_line.html",
                          {"type": json.dumps(surgery_type), "x": json.dumps(x), "res": json.dumps(res),
                           'title': category, "form": form})
        else:

            return render(request, "analysis/analysis_sy_line.html", {"form": form})


'''
 Analysis for Decision Indicator for Surgery Type
'''


def update_data(res, para, loci, value, surgery_type):
    # if len(res) == 0:
    #     dic_temp = {"type": 'bar', "coordinateSystem": 'polar', "name": para, "stack": 'a', "emphasis": {
    #         "focus": 'series'
    #     }, "data": [0] * len(surgery_type)}
    #     dic_temp["data"][loci] = value
    #     res.append(dic_temp)

    for re in res:
        if re['name'] == para:
            re['data'][loci] += value
            return
    else:
        dic_temp = {"type": 'bar', "coordinateSystem": 'polar', "name": para, "stack": 'a', "emphasis": {
            "focus": 'series'
        }, "data": [0] * len(surgery_type)}
        dic_temp["data"][loci] = value
        res.append(dic_temp)


def ana_di_polar(request):
    # surgery_type = {}
    para_array = []
    # x = []
    # sp_res = PftdDecisionIndicator.objects.values('surgery_type').distinct()
    # temp = 0
    # for i in sp_res:
    #     if ";" in i['surgery_type']:
    #         st = i['surgery_type'].split(";")
    #         for j in st:
    #             if j.strip().title() not in x:
    #                 x.append(j.strip().title())
    #                 surgery_type[j.strip().title()] = temp
    #                 temp += 1
    #     else:
    #         if i['surgery_type'].strip().title() not in x:
    #             x.append(i['surgery_type'].strip().title())
    #             surgery_type[i['surgery_type'].strip().title()] = temp
    #             temp += 1
    # {'Abdominal Surgery': 0, 'Obstetric Surgery': 1, 'Vascular Surgery': 2, 'Urological Surgery': 3,
    #  'Gynecological Surgery': 4, '': 5, 'Thoracic Surgery': 6, 'Neurosurgery': 7, 'Cardiac Surgery': 8,
    #  'Orthopedic Surgery': 9, 'Oncosurgery': 10, 'Pediatric Surgery': 11, 'Other Surgeries': 12,
    #  'Post-Endoscopic Retrograde Cholangiopancreatography(Ercp)': 13, 'Na': 14, 'Head And Neck Surgery': 15,
    #  'Non-Cardiac Surgery': 16, 'Critically Ill Surgery': 17, 'Bariatric Surgery': 18, 'Other Surgery': 19,
    #  'Urgent Pci': 20}
    x = ['Cardiac surgery', 'Abdominal Surgery', 'Thoracic Surgery', 'Urological Surgery',
         'Vascular Surgery', 'Neurosurgery', 'Head And Neck Surgery', 'Orthopedic Surgery',
         'Gynecological Surgery', 'Obstetric Surgery', 'Pediatric Surgery', 'Bariatric Surgery',
         'Critically Ill Surgery', 'Other Surgeries']
    surgery_type = {'Cardiac Surgery': 0, 'Abdominal Surgery': 1, 'Thoracic Surgery': 2, 'Urological Surgery': 3,
                    'Vascular Surgery': 4, 'Neurosurgery': 5, 'Head And Neck Surgery': 6, 'Orthopedic Surgery': 7,
                    'Gynecological Surgery': 8, 'Obstetric Surgery': 9, 'Pediatric Surgery': 10,
                    'Bariatric Surgery': 11, 'Critically Ill Surgery': 12, 'Other Surgeries': 13}
    # print(surgery_type)
    res = []

    data_sp_para = PftdDecisionIndicator.objects.raw(
        "SELECT id, surgery_type as name,Application as app,COUNT(*) as nums FROM `pftd_decision_indicator` GROUP BY surgery_type,Application"
    )
    surgeries = ["Non-cardiac surgery",
                 "post-endoscopic retrograde cholangiopancreatography(ERCP)", "urgent PCI", "Oncosurgery", "NA",
                 "other surgery", "other surgeries"]
    for i in data_sp_para:
        print(i.name, i.app)
        if i.app is None or i.name is None:
            print(f"Skipping row with null values - name: {i.name}, app: {i.app}")
            continue
        if i.name.strip().lower() == 'gastrointestinal surgery':
            continue
        if i.name.strip().lower() == 'gastric surgery':
            continue
        if i.name.strip().lower() == 'autologous breast reconstruction':
            continue
        if i.name.strip().lower() == 'abdominal or thoracic surgery':
            continue
        if i.name.strip().lower() == 'lung resection':
            continue
        if i.name.strip().lower() == 'back surgery':
            continue
        if i.name.strip().lower() == 'abdomen；thoracic；extremity；head and trauma':
            continue
        parameters = [para.strip().title() for para in i.app.split(';')]
        # surgery_type
        names = [para.strip().title() for para in i.name.split(';')]

        if ';' in i.name and ';' not in i.app:
            for name in names:
                if name in surgeries:
                    update_data(res, i.app.strip().title(), surgery_type['Other Surgeries'], i.nums, surgery_type)
                else:
                    update_data(res, i.app.strip().title(), surgery_type[name], i.nums, surgery_type)
        elif ';' not in i.name and ';' in i.app:
            for para in parameters:
                if i.name in surgeries:
                    update_data(res, para, surgery_type['Other Surgeries'], i.nums, surgery_type)
                else:
                    update_data(res, para, surgery_type[i.name.strip().title()], i.nums, surgery_type)

        elif ';' in i.name and ';' in i.app:
            for name in names:
                for para in parameters:
                    if i.name in surgeries:
                        update_data(res, para, surgery_type['Other Surgeries'], i.nums, surgery_type)
                    else:
                        update_data(res, para, surgery_type[name], i.nums, surgery_type)
        else:
            if i.name in surgeries:
                update_data(res, i.app.strip().title(), surgery_type['Other Surgeries'], i.nums, surgery_type)
            else:
                update_data(res, i.app.strip().title(), surgery_type[i.name.strip().title()], i.nums, surgery_type)

    for re in res:
        para_array.append(re["name"])
    # print(res)
    return render(request, "analysis/analysis_di_polar.html",
                  {'x': json.dumps(x), "res": json.dumps(res), "type": json.dumps(para_array)})



def ana_regimens_pie(request):

    return render(request, "analysis/analysis_regimens_pie.html",
                  {'x': 0, "res": 0, "type": 0})