from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from datetime import date

# Create your views here.

class NovaPendenciaForm(ModelForm):
    class Meta:
        model = Pendencia
        fields = [ 
            "numeroSolicitacao",
            "patrimonio",
            "equipamento",
            "descricao",
            "setor",
            "estado",
            "previsaoDeConclusao",
        ]

class AlterarEstadoPendenciaForm(ModelForm):
    class Meta:
        model = Pendencia
        fields = [
            "estado",
        ]

class NovaAtualizacaoForm(ModelForm):
    class Meta:
        model = Atualizacao
        fields = [ 
            "textoAtualizacao",
        ]

def verificaSetor(idSetor):
    match idSetor:
        case  1 : return "1º PAVIMENTO - HJV"
        case  2 : return "2º PAVIMENTO - HJV"
        case  3 : return "3º PAVIMENTO - HJV"
        case  4 : return "1º PAVIMENTO PEDIATRIA"
        case  5 : return "2º PAVIMENTO PEDIATRIA"
        case  6 : return "3º PAVIMENTO PEDIATRIA"
        case  7 : return "ASSISTÊNCIA DOMICILIAR"
        case  8 : return "CENTRO CIRÚRGICO - HJV"
        case  9 : return "CENTRO CIRÚRGICO - DAY"
        case  10 : return "CENTRO OBSTÉTRICO"
        case  11 : return "CLÍNICA MÉDICA"
        case  12 : return "CME - HJV"
        case  13 : return "CME - DAY"
        case  14 : return "ECO BIOIMAGEM"
        case  15 : return 'EMERGÊNCIA ADULTO'
        case  16 : return 'EMERGÊNCIA PEDIÁTRICA'
        case  17 : return 'HEMODINÂMICA - BIOIMAGEM'
        case  18 : return 'LACTÁRIO'
        case  19 : return "NUTRIÇÃO"
        case  20 : return "ONCOLOGIA"
        case  21 : return "PRONTO ATENDIMENTO"
        case  22 : return "RADIOLOGIA - PRONTO ATENDIMENTO"
        case  23 : return "RADIOLOGIA - HJV"
        case  24 : return "RADIOLOGIA PEDIATRIA"
        case  25 : return "RESSONÂNCIA MAGNÉTICA"
        case  26 : return "TOMOGRAFIA - BIOIMAGEM"
        case  27 : return "UTI ADULTO 1"
        case  28 : return "UTI ADULTO 2"
        case  29 : return "UTI PEDIÁTRICA"
        case  30 : return "UTI NEONATAL"
        case  31 : return "ULTRASSOM - BIOIMAGEM"





def home(request, template_name='home_user.html'):
    nPendenciasSetor = {}
    for n in range(1,32):
        x = str(n)
        nPendenciasSetor[x] = Pendencia.objects.filter(setor=x).exclude(estado="CONCLUÍDA").count()
    context = {"nPendenciasSetor": nPendenciasSetor, 'adm': "0" }
    return render(request, template_name, context)

def homeADM(request, template_name='home_adm.html'):
    nPendenciasSetor = {}
    for n in range(1,32):
        x = str(n)
        nPendenciasSetor[x] = Pendencia.objects.filter(setor=x).exclude(estado="CONCLUÍDA").count()
    context = {"nPendenciasSetor": nPendenciasSetor, 'button_contexto': "home_ADM", 'adm': "1"}
    return render(request, template_name, context,)



def pendenciaSetorVer(request, setor, template_name='pendencia_view_user.html'):
    setorAtual = verificaSetor(int(setor))
    pendencias = Pendencia.objects.filter(setor=setor).exclude(estado="CONCLUÍDA")
    context = {'pendencias': pendencias, 'setorAtual': setorAtual, 'idSetor': setor, 'button_contexto': "todas_pendencias_setor_pendentes", 'adm': "0"}
    return render(request, template_name, context)

def pendenciaSetorVerADM(request, setor, template_name='pendencia_view_adm.html'):
    setorAtual = verificaSetor(int(setor))
    pendencias = Pendencia.objects.filter(setor=setor).exclude(estado="CONCLUÍDA")
    context = {'pendencias': pendencias, 'setorAtual': setorAtual, 'idSetor': setor, 'button_contexto': "todas_pendencias_setor_pendentes", 'adm': "1"}
    return render(request, template_name, context)




def pendeciasConcluidasVer(request, setor, template_name='pendencia_view_user.html'):
    setorAtual = verificaSetor(int(setor))
    pendencias = Pendencia.objects.filter(setor=setor, estado="CONCLUÍDA")
    context = {'pendencias': pendencias, 'setorAtual': setorAtual, 'idSetor': setor, 'button_contexto': "todas_pendencias_setor_concluidas", 'adm': "0"}
    return render(request, template_name, context)


def pendeciasConcluidasVerADM(request, setor, template_name='pendencia_view_adm.html'):
    setorAtual = verificaSetor(int(setor))
    pendencias = Pendencia.objects.filter(setor=setor, estado="CONCLUÍDA")
    context = {'pendencias': pendencias, 'setorAtual': setorAtual, 'idSetor': setor, 'button_contexto': "todas_pendencias_setor_concluidas", 'adm': "1"}
    return render(request, template_name, context)






def pendenciaCadastrarADM(request, template_name='pendencia_form.html'):
    form = NovaPendenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_adm')
    return render(request, template_name, {'form': form})







def atualizacaoSetorVer(request, id, template_name='atualizacao_view_user.html'):
    setorAtual = []
    atualizacoes = Atualizacao.objects.filter(idPendencia=id)
    pendencia = Pendencia.objects.filter(id=id)
    pendencia = pendencia[0]
    setorAtual = verificaSetor(pendencia.setor)
    idSetor = pendencia.setor
    context = {'pendencia': pendencia, 'atualizacoes': atualizacoes, 'setorAtual': setorAtual, 'idSetor': idSetor, 'button_contexto': "", 'adm': "0"}
    return render(request, template_name, context)

def atualizacaoSetorVerADM(request, id, template_name='atualizacao_view_adm.html'):
    setorAtual = []
    atualizacoes = Atualizacao.objects.filter(idPendencia=id)
    pendencia = Pendencia.objects.filter(id=id)
    pendencia = pendencia[0]
    setorAtual = verificaSetor(pendencia.setor)
    idSetor = pendencia.setor
    context = {'pendencia': pendencia, 'atualizacoes': atualizacoes, 'setorAtual': setorAtual, 'idSetor': idSetor, 'button_contexto': "pendencia_detalhes", 'adm': "1"}
    return render(request, template_name, context)



def atualizacaoCadastrarADM(request, id, template_name='atualizacao_form.html'):
    form = NovaAtualizacaoForm(request.POST or None)
    if form.is_valid():
        atualizacao = form.save(commit=False)
        objetoPendencia = Pendencia.objects.filter(id=id)
        for p in objetoPendencia:
            chaveIDPendencia = p    
        atualizacao.idPendencia = chaveIDPendencia
        atualizacao.save()
        return redirect('/adm/atualizacaoSetor/' + id)
    return render(request, template_name, {'form': form})



def pendenciaEstadoAtualizarADM(request, id, template_name='atualizacao_status.html'):
    atualizacoes = Atualizacao.objects.filter(idPendencia=id)
    pendencia = Pendencia.objects.filter(id=id)
    pendencia = pendencia[0]
    setorAtual = verificaSetor(pendencia.setor)
    form = AlterarEstadoPendenciaForm(request.POST or None, instance=pendencia)
    if form.is_valid():
        if form.cleaned_data['estado'] == "CONCLUÍDA":
            pendencia = form.save(commit=False)
            pendencia.dataFim = date.today()
        else:
            pendencia = form.save(commit=False)
            pendencia.dataFim = None
        pendencia.save()
        return redirect('/adm/atualizacaoSetor/' + id)
    context = {'pendencia': pendencia, 'atualizacoes': atualizacoes, 'setorAtual': setorAtual, 'form': form, 'adm': "1"}
    return render(request, template_name, context)