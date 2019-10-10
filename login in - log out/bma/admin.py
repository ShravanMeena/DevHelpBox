from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Evento)
admin.site.register(EventoLista)
admin.site.register(EventoListaItem)
admin.site.register(EventoListaTipo)
admin.site.register(EventoRegra)
admin.site.register(EventoTipo)
admin.site.register(ParticipacaoCondicao)
admin.site.register(ParticipacaoStatus)
admin.site.register(PessoaGeneroSexual)
admin.site.register(Pessoa)
admin.site.register(Endereco)
