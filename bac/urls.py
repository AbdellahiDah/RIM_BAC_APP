from django.urls import path

from . import views

urlpatterns = [   
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('findresutls', views.findresutls, name='findresutls'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
     #--------------------------------@wilaya----------------------------------------------------------------

    path('wilaya/<int:pk>', views.WilayaView.as_view(), name='wilaya-detail-view'),
    path('wilaya/add', views.WilayaCreate.as_view(), name='wilaya-create-view'),
    path('wilaya/', views.WilayaList.as_view(), name='wilaya-list-view'),
    path('wilaya/update/<int:pk>', views.WilayaUpdate.as_view(), name='wilaya-update'),
    path('wilaya/delete/<int:pk>', views.WilayaDelete.as_view(), name='wilaya-delete'),

    #-------------------------------------@etablissement-------------------------------------------------------

    path('etablissement/add', views.EtablissementCreate.as_view(), name='etablissement-create-view'),
    path('etablissement/<slug:pk>', views.EtablissementView.as_view(), name='etablissement-detail-view'),
    path('etablissement/', views.EtablissementList.as_view(), name='etablissement-list-view'),
    path('etablissement/update/<slug:pk>', views.EtablissementUpdate.as_view(), name='etablissement-update'),
    path('etablissement/delete/<slug:pk>', views.EtablissementDelete.as_view(), name='etablissement-delete'),

    
    #--------------------------------------@CentreExam---------------------------------------------------

    path('CentreExam/add', views.CentreExamCreate.as_view(), name='CentreExam-create-view'),
    path('CentreExam/<slug:pk>', views.CentreExamView.as_view(), name='CentreExam-detail-view'),
    path('CentreExam/', views.CentreExamList.as_view(), name='CentreExam-list-view'),
    path('CentreExam/update/<slug:pk>', views.CentreExamUpdate.as_view(), name='CentreExam-update'),
    path('CentreExam/delete/<slug:pk>', views.CentreExamDelete.as_view(), name='CentreExam-delete'),


    #---------------------------------------@Exam---------------------------------------------------

    path('Exam/add', views.ExamCreate.as_view(), name='Exam-create-view'),
    path('Exam/<slug:pk>', views.ExamView.as_view(), name='Exam-detail-view'),
    path('Exam/', views.ExamList.as_view(), name='Exam-list-view'),
    path('Exam/update/<slug:pk>', views.ExamUpdate.as_view(), name='Exam-update'),
    path('Exam/delete/<slug:pk>', views.ExamDelete.as_view(), name='Exam-delete'),


    #----------------------------------------@Candidat----------------------------------------------

    path('Candidat/add', views.CandidatCreate.as_view(), name='Candidat-create-view'),
    path('Candidat/<int:pk>', views.CandidatView.as_view(), name='Candidat-detail-view'),
    path('Candidat/', views.CandidatList.as_view(), name='Candidat-list-view'),
    path('Candidat/update/<slug:pk>', views.CandidatUpdate.as_view(), name='Candidat-update'),
    path('Candidat/delete/<slug:pk>', views.CandidatDelete.as_view(), name='Candidat-delete'),


    #-----------------------------------------@Resultat-----------------------------------------------

    path('Resultat/add', views.ResultatCreate.as_view(), name='Resultat-create-view'),
    path('Resultat/<slug:pk>', views.ResultatView.as_view(), name='Resultat-detail-view'),
    path('Resultat/', views.ResultatList.as_view(), name='Resultat-list-view'),
    path('Resultat/update/<slug:pk>', views.ResultatUpdate.as_view(), name='Resultat-update'),
    path('Resultat/delete/<slug:pk>', views.ResultatDelete.as_view(), name='Resultat-delete'),




]

#CentreExam