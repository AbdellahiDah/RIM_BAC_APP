from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Wilaya, Etablissement, CentreExam, Exam, Candidat, Resultat

#----------@CentreExam-----------------
class CentreExamView(DetailView):
    model = CentreExam 

class CentreExamCreate(CreateView):
    model = CentreExam
    fields = '__all__'

class CentreExamUpdate(UpdateView):
    model = CentreExam
    fields = '__all__'

class CentreExamDelete(DeleteView):
    model = CentreExam
    success_url = reverse_lazy('CentreExam-list-view')

class CentreExamList(ListView):
    model = CentreExam


#-------------@Wilaya-------------------
class WilayaView(DetailView):
    model = Wilaya

class WilayaCreate(CreateView):
    model = Wilaya
    fields = '__all__'

class WilayaUpdate(UpdateView):
    model = Wilaya
    fields = '__all__'

class WilayaDelete(DeleteView):
    model = Wilaya
    success_url = reverse_lazy('wilaya-list-view')

class WilayaList(ListView):
    model = Wilaya



#--------------------@Etablissement--------------
class EtablissementView(DetailView):
    model = Etablissement

class EtablissementCreate(CreateView):
    model = Etablissement
    fields = '__all__'

class EtablissementUpdate(UpdateView):
    model = Etablissement
    fields = '__all__'

class EtablissementDelete(DeleteView):
    model = Etablissement
    success_url = reverse_lazy('etablissement-list-view')

class EtablissementList(ListView):
    model = Etablissement


#---------------@Exam-------------------
class ExamView(DetailView):
    model = Exam

class ExamCreate(CreateView):
    model = Exam
    fields = '__all__'

class ExamUpdate(UpdateView):
    model = Exam
    fields = '__all__'

class ExamDelete(DeleteView):
    model = Exam
    success_url = reverse_lazy('Exam-list-view')

class ExamList(ListView):
    model = Exam



#---------------@Candidat-------------------
class CandidatView(DetailView):
    model = Candidat

class CandidatCreate(CreateView):
    model = Candidat
    fields = '__all__'

class CandidatUpdate(UpdateView):
    model = Candidat
    fields = '__all__'

class CandidatDelete(DeleteView):
    model = Candidat
    success_url = reverse_lazy('Candidat-list-view')

class CandidatList(ListView):
    model = Candidat


#---------------@Resultat-------------------
class ResultatView(DetailView):
    model = Resultat

class ResultatCreate(CreateView):
    model = Resultat
    fields = '__all__'

class ResultatUpdate(UpdateView):
    model = Resultat
    fields = '__all__'

class ResultatDelete(DeleteView):
    model = Resultat
    success_url = reverse_lazy('Resultat-list-view')

class ResultatList(ListView):
    model = Resultat





def Dashboard(request):
    return render(request, 'Dashboard.html',{})
    
def results(request):
    return render(request, 'results.html',{})

def findresutls(request):
    year, ndos = ('','')
    
    if 'year' in request.POST:
        year = request.POST['year']
    
    if 'num_dos' in request.POST:
        ndos = int(request.POST['num_dos'])
   
    cand = Candidat.objects.filter(num_dossier=ndos)[0]
    print(cand)
    res = Resultat.objects.filter(candidat=cand.id)[0]
    print(res)
    if res != []:
        found_c = True
        exam=res.examen.code
        cand = res.candidat.num_dossier
        moy=res.moyenne
        decis=res.decision
    
    else:
        found_c = False
        i=None
    return render(request,'results_detail.html', { 'Bac': exam, 'candidat': cand, 
        'moyenne': moy, 'decision': decis, 'found_c':found_c})



def index(request):
    return render(request, 'index.html', {})
    #return HttpResponse("Hello, world. You're at the rimbac app!")