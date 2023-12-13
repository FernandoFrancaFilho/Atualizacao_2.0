from django.db import models
from enum import Enum, auto

class Periodo(Enum):
    PRIMEIRA_SEMANA = 'primeira semana'
    UM_MES = '1 mês'   
    DOIS_MESES = '2 meses'  
    QUATRO_MESES = '4 meses'   
    SEIS_MESES = '6 meses' 
    NOVE_MESES = '9 meses' 
    DOZE_MESES = '12 meses'
    QUINZE_MESES = '15 meses'
    DEZOITO_MESES = '18 meses' 
    VINTE_QUATRO_MESES = '24 meses'
    TRINTA_MESES= '30 meses'
    TRINTA_SEIS_MESES= '36 meses' 
    QUARENTA_DOIS_MESES= '42 meses'
    
class Crianca(models.Model):
    nomeDaCrianca = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    nomeDaMae = models.CharField(max_length=150)
    cpfDaMae = models.CharField(max_length=14)
    idadeCrianca = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in Periodo])
    maternidade = models.CharField(max_length=150)
    tipoDoParto = models.CharField(max_length=150)
    idadeGestacional = models.CharField(max_length=150)


# Cuidador

class Cuidador(models.Model):
    nome = models.CharField(max_length=150)
    grauDeParentesco = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11, unique=True)


# Cuidador Criança

class CuidadorCrianca(models.Model):
    idCuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    idCrianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()


# Crescimento Crianca

class CrescimentoCrianca(models.Model):
    idCrianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    idadeCrianca = models.CharField(max_length=20)
    altura = models.FloatField()  # Altura em centímetros
    peso = models.FloatField()  # Peso em quilogramas
    perimetro = models.FloatField()
    imc = models.FloatField(null=True, blank=True)  # Campo para armazenar o IMC

    def calcular_imc(self):
        altura_metros = self.altura / 100  # Convertendo altura de centímetros para metros
        imc = self.peso / (altura_metros ** 2)
        return round(imc, 2)  # Arredonda o IMC para 2 casas decimais

    def save(self, *args, **kwargs):
        self.full_clean()  # Chama a função clean antes de salvar
        super(CrescimentoCrianca, self).save(*args, **kwargs)

    def clean(self):
        # Calcula o IMC antes de validar e salvar os dados no banco de dados
        self.imc = self.calcular_imc()
        super(CrescimentoCrianca, self).clean()


# Aleitamento

class Aleitamento(models.Model):
    aleitamento = models.CharField(max_length=30)

# Leite artificial

class LeiteArtificial(models.Model):
    parouAmamentar = models.CharField(max_length=10)
    idadeParou = models.CharField(max_length=150)
    alimentoCrianca = models.CharField(max_length=150)
    porcoesFrutasDia = models.IntegerField()
    alimentosIndustrializado = models.CharField(max_length=10)
    qualAlimentoIndust = models.CharField(max_length=150)


# Desenvolvimento

class Desenvolvimento(models.Model):
    idCrescimentoCrianca = models.ForeignKey(CrescimentoCrianca, on_delete=models.CASCADE)
    brincaEsconde = models.CharField(max_length=15)
    objetosMao = models.CharField(max_length=15)
    duplicaSilaba = models.CharField(max_length=15)
    senta = models.CharField(max_length=15)


# Sinais de alerta

class SinaisAlerta(models.Model):
    diarreia =  models.CharField(max_length=10)
    vomitos =  models.CharField(max_length=10)
    dificuldadeRespirar =  models.CharField(max_length=10)
    febre =  models.CharField(max_length=10)
    hipotermia =  models.CharField(max_length=10)
    sibilancias =  models.CharField(max_length=10)
    convulcoes =  models.CharField(max_length=10)


# Cuidados especiais

class CuidadosEspeciais(models.Model):
    ferro =  models.CharField(max_length=10)
    micronutrientes =  models.CharField(max_length=10)
    vitaminaA =  models.CharField(max_length=10)
    odonto =  models.CharField(max_length=10)
    acidentesDomesticos =  models.CharField(max_length=10)
    negligencias =  models.CharField(max_length=10)


# Endereço

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100)
    nomeUSF = models.CharField(max_length=100, default='USF')
    

# Profissional de Saude

class ProfissionalDeSaude(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11, unique=True)
    tipoProfissional = models.CharField(max_length=150)
    conselho = models.CharField(max_length=150)

    # def __str__(self):
    #     return self.nome

    
# Unidade Saude Familiar

class UnidadeSaudeFamiliar(models.Model):
    idCuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    idCrianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    idProfissionalDeSaude = models.ForeignKey(ProfissionalDeSaude, on_delete=models.CASCADE)
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()


# ProfissionalSaudeEUSF

class ProfissionalSaudeEUSF(models.Model):
    idUSF = models.ForeignKey(UnidadeSaudeFamiliar, on_delete=models.CASCADE)
    idProfissionalDeSaude = models.ForeignKey(ProfissionalDeSaude, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()
    

# Médico

class Medico(models.Model):
    NomeDoMedico = models.CharField(max_length=100)
    Conselho = models.CharField(max_length=100)
    Escilidade = models.CharField(max_length=100)
    NumeroDeInscricao = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Telefone =  models.CharField(max_length=11)
    

# Agendamento

class Agendamento(models.Model):
    horaDaVacinacao = models.TimeField()
    dataDaVacinacao = models.DateField()


# Consulta

class Consulta (models.Model):
    idMedico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    tipoDaConsulta = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    idAgendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    tempoConsulta = models.CharField(max_length=20) #Colocar meses
    id_crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    data = models.CharField(max_length=255)


# Vacina

class Vacina(models.Model):
    tipoVacina = models.CharField(max_length=150)
    lote = models.CharField(max_length=150)
    fabricante = models.CharField(max_length=150)
    dataFabricacao = models.DateField()


# Historico de Vacinas

class HistoricoDeVacinas(models.Model):
    idVacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    idAgendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()


# Criança Vacina

class CriancaVacina(models.Model):
    idVacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    idCrianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    criadoEmDiaMesAno = models.DateField()


# Aplicação 

class Aplicacao(models.Model):
    idVacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    idAgendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalDeSaude, related_name='vacinas', on_delete=models.CASCADE)
    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, default='agendado')


# Tabela Triagem: 

class EscolhasSimNaoTalvez(Enum):
    SIM = 'SIM'
    NAO = 'NAO'
    TALVEZ = 'TALVEZ'

class EscolhasNormalAlterado(Enum):
    NORMAL = 'NORMAL'
    ALTERADO = 'ALTERADO'

class EscolhasRealizadoNaoRealizado(Enum):
    REALIZADO = 'REALIZADO'
    NAOREALIZADO = 'NAOREALIZADO'

class EscolhasAuditiva(Enum):
    EMISSAO = 'EMISSAO'
    POTENCIAL = 'POTENCIAL'

class TriagemNeonatal(models.Model):   
    olhinho = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasRealizadoNaoRealizado])
    data1 = models.DateField()
    olhodireito = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado])
    olhoesquedo = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado])
    obs1 = models.CharField(max_length=150)
    cardiopata = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasRealizadoNaoRealizado])
    data2 = models.DateField() 
    resultado = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado])
    obs2 = models.CharField(max_length=150)
    auditiva = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasRealizadoNaoRealizado])
    data3 = models.DateField()
    testes = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in  EscolhasAuditiva])
    ouvidodireito = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado])
    ouvidoesquerdo = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado])
    obs3 = models.CharField(max_length=150)
    pezinho = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasRealizadoNaoRealizado])
    data4 = models.DateField()
    reteste = models.DateField()

    pezinhoresultado1 = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasSimNaoTalvez])  
    pezinhoresultado2 = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado], blank=True, null=True)
    orelhinharesultado = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasSimNaoTalvez])
    orelhinharesultado2 = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado], blank=True, null=True)
    exameauditoresultado = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasSimNaoTalvez])
    exameauditoresultado2 = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado], blank=True, null=True)
    olhinhoresultado = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasSimNaoTalvez]) 
    olhinhoresultado2 = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado], blank=True, null=True)
    coracaozinhoresultado = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasSimNaoTalvez]) 
    coracaozinhoresultado2 = models.CharField(max_length=30, choices=[(choice.value, choice.value) for choice in EscolhasNormalAlterado], blank=True, null=True)
    

#Exame ocular

class ExameOcular(models.Model):
    class TamanhoOcular(models.TextChoices):
        NORMAL = 'normal', 'Normal'
        ANORMAL = 'anormal', 'Anormal'

    globo_ocular = models.CharField(
        max_length=10,
        choices=TamanhoOcular.choices,
        default=TamanhoOcular.NORMAL,
    )

    class Pupilas(models.TextChoices):
        NORMAL = 'normal', 'Normal'
        ANORMAL = 'anormal', 'Anormal'

    pupilas = models.CharField(
        max_length=10,
        choices=Pupilas.choices,
        default=Pupilas.NORMAL,
    )

    class Estrabismo(models.TextChoices):
        NAO = 'nao', 'Não'
        SIM = 'sim', 'Sim'

    estrabismo = models.CharField(
        max_length=5,
        choices=Estrabismo.choices,
        default=Estrabismo.NAO,
    )

    class SecrecaoOcular(models.TextChoices):
        NAO = 'nao', 'Não'
        SIM = 'sim', 'Sim'

    secrecao_ocular = models.CharField(
        max_length=5,
        choices=SecrecaoOcular.choices,
        default=SecrecaoOcular.NAO,
    )

class PosicaoSono(Enum):
    NAO = auto()
    SIM = auto()

class FuncionamentoIntestino(Enum):
    PRESERVADO = auto()
    NAO_PRESERVADO = auto()

class HigieneCuidadosGerais(Enum):
    PRESERVADO = auto()
    NAO_PRESERVADO = auto()

class SinaisViolencias(Enum):
    PRESENTE = auto()
    AUSENTE = auto()

class AcidentesDomiciliares(Enum):
    NAO = auto()
    SIM = auto()

class CuidadosEspeciais2(models.Model):
    tempo_sono_24_horas = models.CharField(max_length=255, blank=True, null=True)
    posicao_sono_berco = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in PosicaoSono], default=PosicaoSono.NAO.name)
    funcionamento_intestino_colicas = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in FuncionamentoIntestino], default=FuncionamentoIntestino.PRESERVADO.name)
    higiene_cuidados_gerais = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in HigieneCuidadosGerais], default=HigieneCuidadosGerais.PRESERVADO.name)
    sinais_violencias_negligencias = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in SinaisViolencias], default=SinaisViolencias.AUSENTE.name)
    acidentes_domiciliares = models.CharField(max_length=50, choices=[(tag.name, tag.name.replace('_', ' ')) for tag in AcidentesDomiciliares], default=AcidentesDomiciliares.NAO.name)

    # Desevolvimento infantil

class DesenvolvimentoInfantil(models.Model):
    MORO_REFLEX_CHOICES = [
        ('P', 'Presente'),
        ('A', 'Ausente'),
        ('NV', 'Não Verificado'),
    ]

    crianca = models.ForeignKey(Crianca, on_delete=models.CASCADE)
    reflexo_moro = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    reflexo_cocleo_palpebral = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    reflexo_succao = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    bracos_pernas_flexionados = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    postura_cabeca_lateralizada = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    observa_rosto = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    reage_som = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)
    eleva_cabeca = models.CharField(max_length=2, choices=MORO_REFLEX_CHOICES, blank=True)

    def __str__(self):
        return f"Desenvolvimento Infantil - {self.crianca} - {self.pk}"
