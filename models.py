# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Pftd(models.Model):
    id = models.IntegerField(primary_key=True)
    pmid = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    grouping_criteria = models.TextField(db_column='Grouping_criteria', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    journal = models.CharField(db_column='Journal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    study_design = models.CharField(db_column='Study_Design', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sample_size = models.IntegerField(db_column='Sample_Size', blank=True, null=True)  # Field name made lowercase.
    race = models.CharField(db_column='Race', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age_standard = models.CharField(db_column='Age_standard', max_length=30, blank=True, null=True)  # Field name made lowercase.
    asa_physical_status = models.CharField(db_column='ASA_physical_status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bmi = models.CharField(db_column='BMI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bmi_standard = models.CharField(db_column='BMI_standard', max_length=30, blank=True, null=True)  # Field name made lowercase.
    disease = models.CharField(db_column='Disease', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comorbidity = models.CharField(db_column='Comorbidity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgical_approach = models.CharField(db_column='Surgical_approach', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgery_type = models.CharField(max_length=255, blank=True, null=True)
    surgical_site = models.CharField(max_length=255, blank=True, null=True)
    preoperative_fluid_therapy_protocol = models.TextField(db_column='Preoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
    intraoperative_fluid_therapy_protocol = models.TextField(db_column='Intraoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
    postoperative_fluid_therapy_protocol = models.TextField(db_column='Postoperative_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
    other_info_fluid_therapy_protocol = models.TextField(db_column='Other_info_fluid_therapy_protocol', blank=True, null=True)  # Field name made lowercase.
    ft_decision_chart = models.CharField(db_column='FT_Decision_Chart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fluid_therapy_concept = models.CharField(db_column='Fluid Therapy Concept', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_of_fluid_therapy_protocol = models.CharField(db_column='Period_of_fluid_therapy_protocol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parameter1 = models.CharField(db_column='Parameter1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classification_ft_assessment_factors = models.CharField(db_column='Classification_FT_ assessment_factors', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    application = models.CharField(db_column='Application', max_length=50, blank=True, null=True)  # Field name made lowercase.
    condition1 = models.CharField(db_column='Condition1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parameter2 = models.CharField(db_column='Parameter2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    condition2 = models.CharField(db_column='Condition2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parameter3 = models.CharField(db_column='Parameter3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    condition3 = models.CharField(db_column='Condition3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parameter4 = models.CharField(db_column='Parameter4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    condition4 = models.CharField(db_column='Condition4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parameter5 = models.CharField(db_column='Parameter5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    condition5 = models.CharField(db_column='Condition5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    liquid_treatment = models.CharField(max_length=255, blank=True, null=True)
    fluid_name = models.CharField(db_column='Fluid_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fluid_type = models.CharField(db_column='Fluid_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dose = models.CharField(db_column='Dose', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    monitoring = models.CharField(db_column='Monitoring', max_length=255, blank=True, null=True)  # Field name made lowercase.
    monitoring_parameters = models.CharField(db_column='Monitoring_Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
    monitoring_frequency = models.CharField(db_column='Monitoring_frequency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    use_of_vasopressors = models.TextField(db_column='Use_of_vasopressors', blank=True, null=True)  # Field name made lowercase.
    blood_transfusion = models.CharField(db_column='Blood_transfusion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    additional_information = models.TextField(db_column='Additional_information', blank=True, null=True)  # Field name made lowercase.
    effect_comparison = models.TextField(db_column='Effect_comparison', blank=True, null=True)  # Field name made lowercase.
    complications = models.CharField(db_column='Complications', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result1 = models.CharField(db_column='Result1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    complications_name = models.CharField(db_column='Complications_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statictics1 = models.TextField(db_column='Statictics1', blank=True, null=True)  # Field name made lowercase.
    length_of_hospital_stay = models.CharField(max_length=255, blank=True, null=True)
    result2 = models.CharField(db_column='Result2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outcome_name1 = models.TextField(db_column='Outcome_name1', blank=True, null=True)  # Field name made lowercase.
    statictics2 = models.TextField(db_column='Statictics2', blank=True, null=True)  # Field name made lowercase.
    icu_occupancy = models.CharField(db_column='ICU_occupancy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result3 = models.CharField(db_column='Result3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outcome_name2 = models.TextField(db_column='Outcome_name2', blank=True, null=True)  # Field name made lowercase.
    statictics3 = models.TextField(db_column='Statictics3', blank=True, null=True)  # Field name made lowercase.
    mortality = models.CharField(db_column='Mortality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result4 = models.CharField(db_column='Result4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outcome_name3 = models.TextField(db_column='Outcome_name3', blank=True, null=True)  # Field name made lowercase.
    statictics4 = models.TextField(db_column='Statictics4', blank=True, null=True)  # Field name made lowercase.
    test_results = models.CharField(max_length=255, blank=True, null=True)
    result5 = models.CharField(db_column='Result5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outcome_name4 = models.TextField(db_column='Outcome_name4', blank=True, null=True)  # Field name made lowercase.
    statictics5 = models.TextField(db_column='Statictics5', blank=True, null=True)  # Field name made lowercase.
    vital_signs = models.CharField(max_length=255, blank=True, null=True)
    result6 = models.CharField(db_column='Result6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outcome_name5 = models.TextField(db_column='Outcome_name5', blank=True, null=True)  # Field name made lowercase.
    statictics6 = models.TextField(db_column='Statictics6', blank=True, null=True)  # Field name made lowercase.
    other_outomes = models.CharField(max_length=255, blank=True, null=True)
    sub_classfication = models.CharField(max_length=255, blank=True, null=True)
    result7 = models.CharField(db_column='Result7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outcome_name6 = models.TextField(db_column='Outcome_name6', blank=True, null=True)  # Field name made lowercase.
    statictics7 = models.TextField(db_column='Statictics7', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.TextField(db_column='Conclusion', blank=True, null=True)  # Field name made lowercase.
    evidence_level = models.CharField(db_column='Evidence_level', max_length=255, blank=True, null=True)  # Field name made lowercase.
    strength_of_recommendation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pftd'


class PftdDecisionIndicator(models.Model):
    id = models.IntegerField(primary_key=True)
    pmid = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surgery_type = models.CharField(max_length=255, blank=True, null=True)
    period_of_fluid_therapy = models.CharField(db_column='Period_of_fluid_therapy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parameters = models.CharField(db_column='Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classification_of_fluid_therapy_parameters = models.CharField(db_column='Classification_of_fluid_therapy_Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=255, blank=True, null=True)  # Field name made lowercase.
    monitoring_parameters = models.CharField(db_column='Monitoring_Parameters', max_length=255, blank=True, null=True)  # Field name made lowercase.
    effect_comparison = models.TextField(db_column='Effect comparison', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    complications = models.CharField(db_column='Complications', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result1 = models.CharField(db_column='Result1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    complications_name = models.CharField(db_column='Complications_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statictics1 = models.TextField(db_column='Statictics1', blank=True, null=True)  # Field name made lowercase.
    mortality = models.CharField(db_column='Mortality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result2 = models.CharField(db_column='Result2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outcome_name = models.CharField(db_column='Outcome_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statictics2 = models.TextField(db_column='Statictics2', blank=True, null=True)  # Field name made lowercase.
    evidence_level = models.CharField(db_column='Evidence level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    strength_of_recommendation = models.CharField(db_column='strength of recommendation', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'pftd_decision_indicator'
