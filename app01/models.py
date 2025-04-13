from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# class Pftd(models.Model):
#     id = models.IntegerField(primary_key=True)
#     pmid = models.IntegerField(blank=True, null=True)
#     iftp_subgroup = models.CharField(db_column='IFTP_subgroup', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     iftp = models.CharField(db_column='IFTP', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     group_name = models.CharField(max_length=255, blank=True, null=True)
#     grouping_criteria = models.TextField(db_column='Grouping_criteria', blank=True, null=True)  # Field name made lowercase.
#     year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
#     journal = models.CharField(db_column='Journal', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
#     study_design = models.CharField(db_column='Study_Design', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sample_size = models.IntegerField(db_column='Sample_Size', blank=True, null=True)  # Field name made lowercase.
#     race = models.CharField(db_column='Race', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     asa_physical_status = models.CharField(db_column='ASA_physical_status', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     weight = models.CharField(db_column='Weight', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bmi = models.CharField(db_column='BMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     disease = models.CharField(db_column='Disease', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     comorbidity = models.CharField(db_column='Comorbidity', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     surgical_approach = models.CharField(db_column='Surgical_approach', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     surgery_type = models.CharField(max_length=255, blank=True, null=True)
#     surgical_site = models.CharField(max_length=255, blank=True, null=True)
#     period_of_fluid_therapy1 = models.CharField(db_column='Period_of_fluid_therapy1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     preoperative_fluid_therapy_protocol = models.TextField(db_column='Preoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
#     intraoperative_fluid_therapy_protocol = models.TextField(db_column='Intraoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
#     postoperative_fluid_therapy_protocol = models.TextField(db_column='Postoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
#     other_info_fluid_therapy_protocol = models.TextField(db_column='Other_info_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
#     ft_decision_chart = models.CharField(db_column='FT_Decision_Chart', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fluid_therapy_concept = models.CharField(db_column='Fluid_Therapy_Concept', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     period_of_fluid_therapy2 = models.CharField(db_column='Period_of_fluid_therapy2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     parameter1 = models.CharField(db_column='Parameter1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classification_ft_assessment_factors1 = models.TextField(db_column='Classification_FT_assessment_factors1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     application1 = models.TextField(db_column='Application1', blank=True, null=True)  # Field name made lowercase.
#     condition1 = models.CharField(db_column='Condition1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter2 = models.CharField(db_column='Parameter2', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classification_ft_assessment_factors2 = models.TextField(db_column='Classification_FT_assessment_factors2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     application2 = models.TextField(db_column='Application2', blank=True, null=True)  # Field name made lowercase.
#     condition2 = models.CharField(db_column='Condition2', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter3 = models.CharField(db_column='Parameter3', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classification_ft_assessment_factors3 = models.TextField(db_column='Classification_FT_assessment_factors3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     application3 = models.TextField(db_column='Application3', blank=True, null=True)  # Field name made lowercase.
#     condition3 = models.CharField(db_column='Condition3', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter4 = models.CharField(db_column='Parameter4', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classification_ft_assessment_factors4 = models.TextField(db_column='Classification_FT_assessment_factors4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     application4 = models.TextField(db_column='Application4', blank=True, null=True)  # Field name made lowercase.
#     condition4 = models.CharField(db_column='Condition4', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter5 = models.CharField(db_column='Parameter5', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classification_ft_assessment_factors5 = models.TextField(db_column='Classification_FT_assessment_factors5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     application5 = models.TextField(db_column='Application5', blank=True, null=True)  # Field name made lowercase.
#     condition5 = models.CharField(db_column='Condition5', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     liquid_treatment = models.CharField(max_length=255, blank=True, null=True)
#     fluid_name = models.CharField(db_column='Fluid_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fluid_type = models.CharField(db_column='Fluid_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     dose = models.CharField(db_column='Dose', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     rate = models.CharField(db_column='Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     duration = models.CharField(db_column='Duration', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     monitoring = models.CharField(db_column='Monitoring', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     monitoring_parameters = models.CharField(db_column='Monitoring_Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     monitoring_frequency = models.CharField(db_column='Monitoring_frequency', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     use_of_vasopressors = models.TextField(db_column='Use_of_vasopressors', blank=True, null=True)  # Field name made lowercase.
#     blood_transfusion = models.CharField(db_column='Blood_transfusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     additional_information = models.TextField(db_column='Additional_information', blank=True, null=True)  # Field name made lowercase.
#     effect_comparison = models.TextField(db_column='Effect_comparison', blank=True, null=True)  # Field name made lowercase.
#     complications = models.CharField(db_column='Complications', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     result1 = models.CharField(db_column='Result1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     complications_name = models.CharField(db_column='Complications_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     statictics1 = models.TextField(db_column='Statictics1', blank=True, null=True)  # Field name made lowercase.
#     length_of_hospital_stay = models.CharField(max_length=255, blank=True, null=True)
#     result2 = models.CharField(db_column='Result2', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name1 = models.TextField(db_column='Outcome_name1', blank=True, null=True)  # Field name made lowercase.
#     statictics2 = models.TextField(db_column='Statictics2', blank=True, null=True)  # Field name made lowercase.
#     icu_occupancy = models.CharField(db_column='ICU_occupancy', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     result3 = models.CharField(db_column='Result3', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name2 = models.TextField(db_column='Outcome_name2', blank=True, null=True)  # Field name made lowercase.
#     statictics3 = models.TextField(db_column='Statictics3', blank=True, null=True)  # Field name made lowercase.
#     mortality = models.CharField(db_column='Mortality', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     result4 = models.CharField(db_column='Result4', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name3 = models.TextField(db_column='Outcome_name3', blank=True, null=True)  # Field name made lowercase.
#     statictics4 = models.TextField(db_column='Statictics4', blank=True, null=True)  # Field name made lowercase.
#     test_results = models.CharField(max_length=255, blank=True, null=True)
#     result5 = models.CharField(db_column='Result5', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name4 = models.TextField(db_column='Outcome_name4', blank=True, null=True)  # Field name made lowercase.
#     statictics5 = models.TextField(db_column='Statictics5', blank=True, null=True)  # Field name made lowercase.
#     vital_signs = models.CharField(max_length=255, blank=True, null=True)
#     result6 = models.CharField(db_column='Result6', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name5 = models.TextField(db_column='Outcome_name5', blank=True, null=True)  # Field name made lowercase.
#     statictics6 = models.TextField(db_column='Statictics6', blank=True, null=True)  # Field name made lowercase.
#     other_outomes = models.CharField(max_length=255, blank=True, null=True)
#     sub_classfication = models.CharField(max_length=255, blank=True, null=True)
#     result7 = models.CharField(db_column='Result7', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name6 = models.TextField(db_column='Outcome_name6', blank=True, null=True)  # Field name made lowercase.
#     statictics7 = models.TextField(db_column='Statictics7', blank=True, null=True)  # Field name made lowercase.
#     conclusion = models.TextField(db_column='Conclusion', blank=True, null=True)  # Field name made lowercase.
#     evidence_level = models.CharField(db_column='Evidence_level', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     strength_of_recommendation = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'pftd'
  #version 1.0
# class Pftd(models.Model):
#     id = models.IntegerField(primary_key=True)
#     pmid = models.IntegerField(blank=True, null=True)
#     group_name = models.CharField(max_length=255, blank=True, null=True)
#     grouping_criteria = models.TextField(db_column='Grouping_criteria', blank=True, null=True)  # Field name made lowercase.
#     year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
#     journal = models.CharField(db_column='Journal', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
#     study_design = models.CharField(db_column='Study_Design', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sample_size = models.IntegerField(db_column='Sample_Size', blank=True, null=True)  # Field name made lowercase.
#     race = models.CharField(db_column='Race', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     age_standard = models.CharField(db_column='Age_standard', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     asa_physical_status = models.CharField(db_column='ASA_physical_status', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     weight = models.CharField(db_column='Weight', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bmi = models.CharField(db_column='BMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bmi_standard = models.CharField(db_column='BMI_standard', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     disease = models.CharField(db_column='Disease', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     comorbidity = models.CharField(db_column='Comorbidity', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     surgical_approach = models.CharField(db_column='Surgical_approach', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     surgery_type = models.CharField(max_length=255, blank=True, null=True)
#     surgical_site = models.CharField(max_length=255, blank=True, null=True)
#     preoperative_fluid_therapy_protocol = models.TextField(db_column='Preoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
#     intraoperative_fluid_therapy_protocol = models.TextField(db_column='Intraoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
#     postoperative_fluid_therapy_protocol = models.TextField(db_column='Postoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
#     other_info_fluid_therapy_protocol = models.TextField(db_column='Other_info_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
#     ft_decision_chart = models.CharField(db_column='FT_Decision_Chart', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fluid_therapy_concept = models.CharField(db_column='Fluid Therapy Concept', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     period_of_fluid_therapy_protocol = models.CharField(db_column='Period_of_fluid_therapy_protocol', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter1 = models.CharField(db_column='Parameter1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classification_ft_assessment_factors = models.CharField(db_column='Classification_FT_ assessment_factors', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     application = models.CharField(db_column='Application', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     condition1 = models.CharField(db_column='Condition1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter2 = models.CharField(db_column='Parameter2', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     condition2 = models.CharField(db_column='Condition2', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter3 = models.CharField(db_column='Parameter3', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     condition3 = models.CharField(db_column='Condition3', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter4 = models.CharField(db_column='Parameter4', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     condition4 = models.CharField(db_column='Condition4', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameter5 = models.CharField(db_column='Parameter5', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     condition5 = models.CharField(db_column='Condition5', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     liquid_treatment = models.CharField(max_length=255, blank=True, null=True)
#     fluid_name = models.CharField(db_column='Fluid_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fluid_type = models.CharField(db_column='Fluid_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     dose = models.CharField(db_column='Dose', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     rate = models.CharField(db_column='Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     duration = models.CharField(db_column='Duration', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     monitoring = models.CharField(db_column='Monitoring', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     monitoring_parameters = models.CharField(db_column='Monitoring_Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     monitoring_frequency = models.CharField(db_column='Monitoring_frequency', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     use_of_vasopressors = models.TextField(db_column='Use_of_vasopressors', blank=True, null=True)  # Field name made lowercase.
#     blood_transfusion = models.CharField(db_column='Blood_transfusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     additional_information = models.TextField(db_column='Additional_information', blank=True, null=True)  # Field name made lowercase.
#     effect_comparison = models.TextField(db_column='Effect_comparison', blank=True, null=True)  # Field name made lowercase.
#     complications = models.CharField(db_column='Complications', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     result1 = models.CharField(db_column='Result1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     complications_name = models.CharField(db_column='Complications_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     statictics1 = models.TextField(db_column='Statictics1', blank=True, null=True)  # Field name made lowercase.
#     length_of_hospital_stay = models.CharField(max_length=255, blank=True, null=True)
#     result2 = models.CharField(db_column='Result2', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name1 = models.TextField(db_column='Outcome_name1', blank=True, null=True)  # Field name made lowercase.
#     statictics2 = models.TextField(db_column='Statictics2', blank=True, null=True)  # Field name made lowercase.
#     icu_occupancy = models.CharField(db_column='ICU_occupancy', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     result3 = models.CharField(db_column='Result3', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name2 = models.TextField(db_column='Outcome_name2', blank=True, null=True)  # Field name made lowercase.
#     statictics3 = models.TextField(db_column='Statictics3', blank=True, null=True)  # Field name made lowercase.
#     mortality = models.CharField(db_column='Mortality', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     result4 = models.CharField(db_column='Result4', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name3 = models.TextField(db_column='Outcome_name3', blank=True, null=True)  # Field name made lowercase.
#     statictics4 = models.TextField(db_column='Statictics4', blank=True, null=True)  # Field name made lowercase.
#     test_results = models.CharField(max_length=255, blank=True, null=True)
#     result5 = models.CharField(db_column='Result5', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name4 = models.TextField(db_column='Outcome_name4', blank=True, null=True)  # Field name made lowercase.
#     statictics5 = models.TextField(db_column='Statictics5', blank=True, null=True)  # Field name made lowercase.
#     vital_signs = models.CharField(max_length=255, blank=True, null=True)
#     result6 = models.CharField(db_column='Result6', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name5 = models.TextField(db_column='Outcome_name5', blank=True, null=True)  # Field name made lowercase.
#     statictics6 = models.TextField(db_column='Statictics6', blank=True, null=True)  # Field name made lowercase.
#     other_outomes = models.CharField(max_length=255, blank=True, null=True)
#     sub_classfication = models.CharField(max_length=255, blank=True, null=True)
#     result7 = models.CharField(db_column='Result7', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name6 = models.TextField(db_column='Outcome_name6', blank=True, null=True)  # Field name made lowercase.
#     statictics7 = models.TextField(db_column='Statictics7', blank=True, null=True)  # Field name made lowercase.
#     conclusion = models.TextField(db_column='Conclusion', blank=True, null=True)  # Field name made lowercase.
#     evidence_level = models.CharField(db_column='Evidence_level', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     strength_of_recommendation = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'pftd'


class PftdDecisionIndicator(models.Model):
    id = models.IntegerField(primary_key=True)
    pid = models.CharField(db_column='PID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pmid = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    journal = models.CharField(db_column='Journal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    surgery_type = models.CharField(max_length=255, blank=True, null=True)
    period_of_fluid_therapy = models.CharField(db_column='Period_of_fluid_therapy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parameters = models.CharField(db_column='Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classification_of_fluid_therapy_parameters = models.CharField(db_column='Classification_of_fluid_therapy_Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=255, blank=True, null=True)  # Field name made lowercase.
    study_design = models.CharField(db_column='Study_design', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    sample_size = models.CharField(db_column='Sample_Size', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asa_physical_status = models.TextField(db_column='ASA_Physical_Status', blank=True, null=True)  # Field name made lowercase.
    bmi = models.CharField(db_column='BMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgical_approach = models.CharField(db_column='Surgical_approach', max_length=255, blank=True, null=True)  # Field name made lowercase.
    defination = models.TextField(db_column='Defination', blank=True, null=True)  # Field name made lowercase.
    race = models.CharField(db_column='Race', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'app01'
        managed = True
        db_table = 'pftd_decision_indicator'

#
# class PftdDecisionIndicator(models.Model):
#     id = models.IntegerField(primary_key=True)
#     pmid = models.IntegerField(blank=True, null=True)
#     group_name = models.CharField(max_length=255, blank=True, null=True)
#     year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
#     reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     surgery_type = models.CharField(max_length=255, blank=True, null=True)
#     period_of_fluid_therapy = models.CharField(db_column='Period_of_fluid_therapy', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     parameters = models.CharField(db_column='Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classification_of_fluid_therapy_parameters = models.CharField(db_column='Classification_of_fluid_therapy_Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     application = models.CharField(db_column='Application', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     monitoring_parameters = models.CharField(db_column='Monitoring_Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     effect_comparison = models.TextField(db_column='Effect comparison', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     complications = models.CharField(db_column='Complications', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     result1 = models.CharField(db_column='Result1', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     complications_name = models.CharField(db_column='Complications_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     statictics1 = models.TextField(db_column='Statictics1', blank=True, null=True)  # Field name made lowercase.
#     mortality = models.CharField(db_column='Mortality', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     result2 = models.CharField(db_column='Result2', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     outcome_name = models.CharField(db_column='Outcome_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     statictics2 = models.TextField(db_column='Statictics2', blank=True, null=True)  # Field name made lowercase.
#     evidence_level = models.CharField(db_column='Evidence level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     strength_of_recommendation = models.CharField(db_column='strength of recommendation', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
#
#     class Meta:
#         app_label = 'app01'
#         managed = True
#         db_table = 'pftd_decision_indicator'




class Pftd(models.Model):
    id = models.AutoField(primary_key=True)
    pmid = models.IntegerField(null=True, blank=True)
    IFTP_subgroup = models.CharField(max_length=50, null=True, blank=True)
    IFTP = models.CharField(max_length=25, null=True, blank=True)
    group_name = models.CharField(max_length=255, null=True, blank=True)
    #Grouping_criteria = models.TextField(null=True, blank=True)
    Year = models.IntegerField(null=True, blank=True)
    Journal = models.CharField(max_length=255, null=True, blank=True)
    Reference = models.CharField(max_length=255, null=True, blank=True)
    Title = models.TextField(null=True, blank=True)
    Study_Design = models.CharField(max_length=255, null=True, blank=True)
    Region = models.CharField(max_length=255, null=True, blank=True)
    Sample_Size = models.IntegerField(null=True, blank=True)
    Race = models.CharField(max_length=255, null=True, blank=True)
    Gender = models.CharField(max_length=255, null=True, blank=True)
    Age = models.CharField(max_length=255, null=True, blank=True)
    ASA_physical_status = models.CharField(max_length=255, null=True, blank=True)
    # = models.CharField(max_length=50, null=True, blank=True)
    BMI = models.CharField(max_length=255, null=True, blank=True)
    Disease = models.CharField(max_length=255, null=True, blank=True)
    Comorbidity = models.TextField(null=True, blank=True)
    Surgical_approach = models.CharField(max_length=255, null=True, blank=True)
    surgery_type = models.CharField(max_length=255, null=True, blank=True)
    surgical_site = models.TextField(null=True, blank=True)
    Period_of_fluid_therapy = models.CharField(max_length=50, null=True, blank=True)
    Preoperative_fluid_therapy_protocol = models.TextField(null=True, blank=True)
    Intraoperative_fluid_therapy_protocol = models.TextField(null=True, blank=True)
    Postoperative_fluid_therapy_protocol = models.TextField(null=True, blank=True)
    Other_info_fluid_therapy_protocol = models.TextField(null=True, blank=True)
    #FT_Decision_Chart = models.CharField(max_length=255, null=True, blank=True)
    Fluid_Therapy_Concept = models.CharField(max_length=255, null=True, blank=True)
    #Period_of_fluid_therapy2 = models.CharField(max_length=50, null=True, blank=True)
    Parameter1 = models.CharField(max_length=255, null=True, blank=True)
    Classification_FT_assessment_factors1 = models.TextField(null=True, blank=True)
    Application1 = models.TextField(null=True, blank=True)
    Condition1 = models.CharField(max_length=255, null=True, blank=True)
    Parameter2 = models.CharField(max_length=255, null=True, blank=True)
    Classification_FT_assessment_factors2 = models.TextField(null=True, blank=True)
    Application2 = models.TextField(null=True, blank=True)
    Condition2 = models.CharField(max_length=255, null=True, blank=True)
    Parameter3 = models.CharField(max_length=255, null=True, blank=True)
    Classification_FT_assessment_factors3 = models.TextField(null=True, blank=True)
    Application3 = models.TextField(null=True, blank=True)
    Condition3 = models.CharField(max_length=255, null=True, blank=True)
    Parameter4 = models.CharField(max_length=255, null=True, blank=True)
    Classification_FT_assessment_factors4 = models.TextField(null=True, blank=True)
    Application4 = models.TextField(null=True, blank=True)
    Condition4 = models.CharField(max_length=255, null=True, blank=True)
    Parameter5 = models.CharField(max_length=255, null=True, blank=True)
    Classification_FT_assessment_factors5 = models.TextField(null=True, blank=True)
    Application5 = models.TextField(null=True, blank=True)
    Condition5 = models.CharField(max_length=255, null=True, blank=True)
    liquid_treatment = models.CharField(max_length=255, null=True, blank=True)
    Fluid_name = models.CharField(max_length=255, null=True, blank=True)
    Fluid_type = models.CharField(max_length=255, null=True, blank=True)
    Dose = models.CharField(max_length=255, null=True, blank=True)
    Rate = models.CharField(max_length=255, null=True, blank=True)
    Duration = models.CharField(max_length=255, null=True, blank=True)
    Monitoring = models.CharField(max_length=255, null=True, blank=True)
    Monitoring_Parameters = models.CharField(max_length=255, null=True, blank=True)
    Monitoring_frequency = models.CharField(max_length=255, null=True, blank=True)
    Use_of_vasopressors = models.TextField(null=True, blank=True)
    Blood_transfusion = models.TextField(null=True, blank=True)
    Additional_information = models.TextField(null=True, blank=True)
    Effect_comparison = models.TextField(null=True, blank=True)
    Complications = models.TextField(null=True, blank=True)
    Result1 = models.CharField(max_length=255, null=True, blank=True)
    Complications_name = models.TextField(null=True, blank=True)
    Statictics1 = models.TextField(null=True, blank=True)
    length_of_hospital_stay = models.CharField(max_length=255, null=True, blank=True)
    Result2 = models.CharField(max_length=255, null=True, blank=True)
    Outcome_name1 = models.TextField(null=True, blank=True)
    Statictics2 = models.TextField(null=True, blank=True)
    ICU_occupancy = models.CharField(max_length=255, null=True, blank=True)
    Result3 = models.CharField(max_length=255, null=True, blank=True)
    Outcome_name2 = models.TextField(null=True, blank=True)
    Statictics3 = models.TextField(null=True, blank=True)
    Mortality = models.CharField(max_length=255, null=True, blank=True)
    Result4 = models.CharField(max_length=255, null=True, blank=True)
    Outcome_name3 = models.TextField(null=True, blank=True)
    Statictics4 = models.TextField(null=True, blank=True)
    #test_results = models.CharField(max_length=255, null=True, blank=True)
    #Result5 = models.CharField(max_length=255, null=True, blank=True)
    #Outcome_name4 = models.TextField(null=True, blank=True)
    #Statictics5 = models.TextField(null=True, blank=True)
    #vital_signs = models.CharField(max_length=255, null=True, blank=True)
    #Result6 = models.CharField(max_length=255, null=True, blank=True)
    #Outcome_name5 = models.TextField(null=True, blank=True)
    #Statictics6 = models.TextField(null=True, blank=True)
    #other_outomes = models.CharField(max_length=255, null=True, blank=True)
    #sub_classfication = models.CharField(max_length=255, null=True, blank=True)
    #Result7 = models.CharField(max_length=255, null=True, blank=True)
    #Outcome_name6 = models.TextField(null=True, blank=True)
    #Statictics7 = models.TextField(null=True, blank=True)
    Key_points = models.TextField(null=True, blank=True)
    Grades_of_Evidence = models.CharField(max_length=255, null=True, blank=True)
    Levels_of_Recommendation = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        app_label = 'app01'
        managed = False
        db_table = 'pftd'