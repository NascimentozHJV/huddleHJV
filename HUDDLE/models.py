from django.db import models


class Pendencia(models.Model):
    numeroSolicitacao = models.CharField("Número da Solicitação", max_length=7, blank= True)
    patrimonio = models.CharField("Patrimônio", max_length=8)
    equipamento = models.CharField("Equipamento", max_length=30)
    descricao = models.TextField("Descrição do Problema")
    OPCOES_SETORES = [
        (1, "1º PAVIMENTO - HJV"),
        (2, "2º PAVIMENTO - HJV"),
        (3, "3º PAVIMENTO - HJV"),
        (4, "1º PAVIMENTO PEDIATRIA"),
        (5, "2º PAVIMENTO PEDIATRIA"),
        (6, "3º PAVIMENTO PEDIATRIA"),
        (7, "ASSISTÊNCIA DOMICILIAR"),
        (8, "CENTRO CIRÚRGICO - HJV"),
        (9, "CENTRO CIRÚRGICO - DAY"),
        (10, "CENTRO OBSTÉTRICO"),
        (11, "CLÍNICA MÉDICA"),
        (12, "CME - HJV"),
        (13, "CME - DAY"),
        (14,"ECO BIOIMAGEM"),
        (15, 'EMERGÊNCIA ADULTO'),
        (16, 'EMERGÊNCIA PEDIÁTRICA'),
        (17, 'HEMODINÂMICA - BIOIMAGEM'),
        (18, 'LACTÁRIO'),
        (19, "NUTRIÇÃO"),
        (20, "ONCOLOGIA"),
        (21, "PRONTO ATENDIMENTO"),
        (22, "RADIOLOGIA - PRONTO ATENDIMENTO"),
        (23, "RADIOLOGIA - HJV"),
        (24, "RADIOLOGIA PEDIATRIA"),
        (25, "RESSONÂNCIA MAGNÉTICA"),
        (26, "TOMOGRAFIA - BIOIMAGEM"),
        (27, "UTI ADULTO 1"),
        (28, "UTI ADULTO 2"),
        (29, "UTI PEDIÁTRICA"),
        (31, "UTI NEONATAL"),
        (32, "ULTRASSOM - BIOIMAGEM"),
    ]
    setor = models.IntegerField("Setor", choices=OPCOES_SETORES)
    OPCOES_ESTADO = [
        ("PENDENTE NO SETOR", "PENDENTE NO SETOR"),
        ("EM REPARO NA ENGENHARIA", "EM REPARO NA ENGENHARIA"),
        ("EM REPARO NA ASSISTÊNCIA", "EM REPARO NA ASSISTÊNCIA"),
        ("AGUARDANDO PROCESSO COMPRA", "AGUARDANDO PROCESSO COMPRA"),
        ("AGUARDANDO ATENDIMENTO DO FORNECEDOR", "AGUARDANDO ATENDIMENTO DO FORNECEDOR"),
        ("EM USO SENDO OBSERVADO", "EM USO SENDO OBSERVADO"),
        ("EM USO COM RESTRIÇÃO", "EM USO COM RESTRIÇÃO"),
        ("AGUARDANDO PERMISSÃO PARA ACESSAR O EQUIPAMENTO", "AGUARDANDO PERMISSÃO PARA ACESSAR O EQUIPAMENTO"),
        ("CONCLUÍDA", "CONCLUÍDA"),
    ]
    estado = models.CharField("Estado", max_length=50,choices=OPCOES_ESTADO)
    dataInicio = models.DateField("Data de Início", auto_now_add=True)
    previsaoDeConclusao = models.DateField("Previsão de Conclusão", auto_now_add=False)
    dataFim = models.DateField("Data de Fim", auto_now=False, auto_now_add=False, null=True)
    
    

    def __str__(self):
        return self.id
    
class Atualizacao(models.Model):
    textoAtualizacao = models.TextField("Atualização")
    idPendencia = models.ForeignKey(Pendencia, on_delete=models.CASCADE)
    dataAtualizacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id