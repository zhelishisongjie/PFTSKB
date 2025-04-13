"""
URL configuration for pftskb_py project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

from django.views.decorators.cache import cache_page

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("", views.home),
    path("home/", views.home),
    path("search/<int:id>", views.search),
    path("research/preview/", views.preview),
    path("research/publication/", views.publication),
    path("research/study/", views.study),

    path("research/study/study_details/<int:id>", views.study_details),

    path("baseline/patient/",views.patient),
    path("baseline/surgery/",views.surgery),
    path("baseline/disease/",views.disease),

    path("outcome/complication/",views.complication),
    path("outcome/hospital/", views.hospital),
    path("outcome/icu/", views.icu),
    path("outcome/mortality/", views.mortality),

    path("outcome/complication/details/<int:id>",views.outcome_details),
    path("outcome/hospital/details/<int:id>", views.outcome_details),
    path("outcome/icu/details/<int:id>", views.outcome_details),
    path("outcome/mortality/details/<int:id>", views.outcome_details),
    #从pftd表中获取数据，根据不同的应用场景，传入不同的tag，来获取不同的数据。
    path("get_pftd/<int:num>", views.get_pftd_data),
    path("tool/",views.tool),
    path("recommend/", views.recommend),
    path("analysis/", views.analysis),
    path("Contact_us/", views.contact),
    path("help/", views.help),
    path("home/getselect/<int:id>",views.home_select),
    path("search/getlist/<int:id>", views.getlist),
    # path("search/getlist/", cache_page(60*15)(views.getlist)),
    path("search/getdetail/<int:id>", views.getdetails),
    path("search/getdetails/<str:id>", views.getdetails_PID),
    path("search/getsearchdetails/<int:id>", views.getsearchdetails),

    path("search/getIFTPdetails/<str:IFTP>", views.getIFTPdetails),
    path("search/getIFTPsubdetails/<str:IFTP_subgroup>", views.getIFTPsubdetails),

    path("recommend/getSurgerySite/", views.getInfoBySurgeryType),
    path("recommend/initClass/", views.initClass),
    path("recommend/initPara/", views.initPara),
    path("recommend/lastscreeing/", views.LastScreening),

    path("analysis/publication_year/category_search/", views.category_search),
    path("analysis/publication_year/", views.publication_years),
    path("analysis/country_dis/", views.country_dis),
    path("analysis/country_dis/category_search/", views.category_search),
    path("analysis/country_dis/get_geodata/", views.get_geodata),
    path("analysis/sankey/category_search/", views.category_search),
    path("analysis/sankey/", views.ana_sankey),
    path("analysis/Pie/", views.ana_pie),
    path("analysis/graph/", views.ana_graph),
    path("analysis/line/", views.ana_sy_line),
    path("analysis/polar/", views.ana_di_polar),

    path("analysis/regimens_pie/", views.ana_regimens_pie),

]
