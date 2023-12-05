from rest_framework import serializers

from .models import ProfissionalDeSaude, Vacina, ProfissionalSaudeEUSF, UnidadeSaudeFamiliar, HistoricoDeVacinas, Cuidador, CuidadorCrianca, Crianca, CrescimentoCrianca, Agendamento, Endereco, Consulta, Medico, CriancaVacina, Desenvolvimento, SinaisAlerta, CuidadosEspeciais, Aleitamento, LeiteArtificial, Aplicacao, TriagemNeonatal, ExameOcular, CuidadosEspeciais2, DesenvolvimentoInfantil

class CrescimentoCriancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrescimentoCrianca
        fields = '__all__'

class AleitamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aleitamento
        fields = '__all__'

class LeiteArtificialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeiteArtificial
        fields = '__all__'

class DesenvolvimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desenvolvimento
        fields = '__all__'

class SinaisAlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinaisAlerta
        fields = '__all__'

class CuidadosEspeciaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuidadosEspeciais
        fields = '__all__'

class CriancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crianca
        fields = '__all__'

class CuidadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuidador
        fields = '__all__'

class CuidadorCriancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuidadorCrianca
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class ProfissionalDeSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalDeSaude
        fields = '__all__'

class UnidadeSaudeFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeSaudeFamiliar
        fields = '__all__'

class ProfissionalSaudeEUSFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaudeEUSF
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = '__all__'

class HistoricoDeVacinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoDeVacinas
        fields = '__all__'

class CriancaVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriancaVacina
        fields = '__all__'

class AplicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicacao
        fields = '__all__'

class ApplicationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tipoVacina = serializers.CharField()
    lote = serializers.CharField()
    fabricante = serializers.CharField()
    dataFabricacao = serializers.DateField()
    nome = serializers.CharField()
    tipoProfissional = serializers.CharField()
    conselho = serializers.CharField()
    horaDaVacinacao = serializers.TimeField()
    dataDaVacinacao = serializers.DateField()
    status = serializers.CharField()

class ConsultationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome_crianca = serializers.CharField()
    tempo_consulta = serializers.CharField()
    nome_do_medico = serializers.CharField()
    data_da_vacinacao = serializers.DateField()
    tipo_da_consulta = serializers.CharField()
    status = serializers.CharField()

class TriagemNeonatalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriagemNeonatal
        fields = '__all__'    

class ExameOcularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExameOcular
        fields = '__all__'

    def to_representation(self, instance):
        representacao = super().to_representation(instance)
        for nome_campo, campo in self.fields.items():
            if nome_campo.endswith('_ocu'):
                representacao[nome_campo] = campo.choices.get(representacao[nome_campo])
        return representacao
    
class CuidadosEspeciais2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CuidadosEspeciais2
        fields = '__all__' 

class DesenvolvimentoInfantilSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesenvolvimentoInfantil
        fields = '__all__'