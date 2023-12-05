from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import ProfissionalDeSaude, Vacina, ProfissionalSaudeEUSF, UnidadeSaudeFamiliar, HistoricoDeVacinas, Cuidador, CuidadorCrianca, Crianca, CrescimentoCrianca, Agendamento, Endereco, Consulta, Medico, CriancaVacina, Desenvolvimento, SinaisAlerta, CuidadosEspeciais, Aleitamento, LeiteArtificial, Aplicacao, TriagemNeonatal, ExameOcular, CuidadosEspeciais2, DesenvolvimentoInfantil

from .serializers import ProfissionalDeSaudeSerializer, VacinaSerializer, ProfissionalSaudeEUSFSerializer, UnidadeSaudeFamiliarSerializer, HistoricoDeVacinasSerializer, CuidadorSerializer, CuidadorCriancaSerializer, CriancaSerializer, CrescimentoCriancaSerializer, AgendamentoSerializer, EnderecoSerializer, ConsultaSerializer, MedicoSerializer, CriancaVacinaSerializer, DesenvolvimentoSerializer, SinaisAlertaSerializer, CuidadosEspeciaisSerializer, AleitamentoSerializer, LeiteArtificialSerializer, AplicacaoSerializer, ApplicationSerializer, ConsultationSerializer, TriagemNeonatalSerializer, ExameOcularSerializer, CuidadosEspeciais2Serializer, DesenvolvimentoInfantilSerializer

class CrescimentoCriancaViewset(viewsets.ModelViewSet):
    queryset = CrescimentoCrianca.objects.all()
    serializer_class = CrescimentoCriancaSerializer

class AleitamentoViewset(viewsets.ModelViewSet):
    queryset = Aleitamento.objects.all()
    serializer_class = AleitamentoSerializer

class LeiteArtificialViewset(viewsets.ModelViewSet):
    queryset = LeiteArtificial.objects.all()
    serializer_class = LeiteArtificialSerializer

class DesenvolvimentoViewset(viewsets.ModelViewSet):
    queryset = Desenvolvimento.objects.all()
    serializer_class = DesenvolvimentoSerializer

class SinaisAlertaViewset(viewsets.ModelViewSet):
    queryset = SinaisAlerta.objects.all()
    serializer_class = SinaisAlertaSerializer

class CuidadosEspeciaisViewset(viewsets.ModelViewSet):
    queryset = CuidadosEspeciais.objects.all()
    serializer_class = CuidadosEspeciaisSerializer

class CriancaViewset(viewsets.ModelViewSet):
    queryset = Crianca.objects.all()
    serializer_class = CriancaSerializer

class CuidadorViewset(viewsets.ModelViewSet):
    queryset = Cuidador.objects.all()
    serializer_class = CuidadorSerializer

class CuidadorCriancaViewset(viewsets.ModelViewSet):
    queryset = CuidadorCrianca.objects.all()
    serializer_class = CuidadorCriancaSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ProfissionalDeSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalDeSaude.objects.all()
    serializer_class = ProfissionalDeSaudeSerializer

class UnidadeSaudeFamiliarViewset(viewsets.ModelViewSet):
    queryset = UnidadeSaudeFamiliar.objects.all()
    serializer_class = UnidadeSaudeFamiliarSerializer

class ProfissionalSaudeEUSFViewset(viewsets.ModelViewSet):
    queryset = ProfissionalSaudeEUSF.objects.all()
    serializer_class = ProfissionalSaudeEUSFSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer

class HistoricoDeVacinasViewset(viewsets.ModelViewSet):
    queryset = HistoricoDeVacinas.objects.all()
    serializer_class = HistoricoDeVacinasSerializer

class CriancaVacinaViewSet(viewsets.ModelViewSet):
    queryset = CriancaVacina.objects.all()
    serializer_class = CriancaVacinaSerializer

class AplicacaoViewSet(viewsets.ModelViewSet):
    queryset = Aplicacao.objects.all()
    serializer_class = AplicacaoSerializer

class CriancaViewSet(viewsets.ModelViewSet):
    queryset = Crianca.objects.select_related('userapp_vacina').all()
    serializer_class = CriancaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)

def test():
    print("Testing")

# Inner Join

class InnderJoinCreateView(APIView):
   
    serializer_class = ApplicationSerializer
    
    def get(self, request, id, format=None):
        queryset = Aplicacao.objects.filter(crianca_id=id).select_related(
            'idVacina',
            'profissional',  #Apenas Chaves Estrangeiras
            'idAgendamento',
        )

        data_list = []
        for instance in queryset:
            data = {
                'id': instance.id,
                'tipoVacina': instance.idVacina.tipoVacina,
                'lote': instance.idVacina.lote,
                'fabricante': instance.idVacina.fabricante,
                'dataFabricacao': instance.idVacina.dataFabricacao,
                'nome': instance.profissional.nome,
                'tipoProfissional': instance.profissional.tipoProfissional,
                'conselho': instance.profissional.conselho,
                'horaDaVacinacao': instance.idAgendamento.horaDaVacinacao,
                'dataDaVacinacao': instance.idAgendamento.dataDaVacinacao,
                'status': instance.status,
            }
            data_list.append(data)

        serializer = ApplicationSerializer(data=data_list, many=True)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
# Inner Join 2


class InnderJoinCreateView2(APIView):

    serializer_class = ConsultationSerializer
    
    def get(self, request, id, format=None):
        queryset = Consulta.objects.filter(id_crianca=id).select_related(
            'idMedico',
            'idAgendamento', 
        )

        data_list = []
        for instance in queryset:
            data = {
                'id': instance.id,
                'nome_crianca': instance.id_crianca.nomeDaCrianca,
                'tempo_consulta': instance.tempoConsulta,
                'nome_do_medico': instance.idMedico.NomeDoMedico,
                'data_da_vacinacao': instance.idAgendamento.dataDaVacinacao,
                'tipo_da_consulta': instance.tipoDaConsulta,
                'status': instance.status,
            }
            data_list.append(data)

        serializer = ConsultationSerializer(data=data_list, many=True)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class TriagemNeonatalViewSet(viewsets.ModelViewSet):
    queryset = TriagemNeonatal.objects.all()
    serializer_class = TriagemNeonatalSerializer

class ExameOcularViewSet(viewsets.ModelViewSet):
    queryset = ExameOcular.objects.all()
    serializer_class = ExameOcularSerializer

class CuidadosEspeciais2ViewSet(viewsets.ModelViewSet):
    queryset = CuidadosEspeciais2.objects.all()
    serializer_class = CuidadosEspeciais2Serializer

class DesenvolvimentoInfantilViewSet(viewsets.ModelViewSet):
    queryset = DesenvolvimentoInfantil.objects.all()
    serializer_class = DesenvolvimentoInfantilSerializer