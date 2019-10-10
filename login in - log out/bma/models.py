# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    idevento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)
    quantidade_gente_min = models.IntegerField(blank=True, null=True)
    quantidade_gente_max = models.IntegerField(blank=True, null=True)
    local = models.CharField(max_length=45, blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    horario_chegada = models.TimeField(blank=True, null=True)
    horario_inicio = models.TimeField(blank=True, null=True)
    horario_fim = models.TimeField(blank=True, null=True)
    tempo_espera_max = models.FloatField(blank=True, null=True)
    banner_link = models.CharField(unique=True, max_length=45, blank=True, null=True)
    evento_tipo_idevento_tipo = models.ForeignKey('EventoTipo', on_delete = models.CASCADE, db_column='evento_tipo_idevento_tipo', related_name='evento_idevento_tipo')
    organizador_idpessoa = models.ForeignKey('Pessoa', on_delete = models.CASCADE, db_column='organizador_idpessoa', related_name='evento_idorganizador')
    
    class Meta:
        managed = False
        db_table = 'evento'
        
    def __str__(self):
        return str(self.idevento) + ' - ' + self.nome


class EventoHasRegra(models.Model):
    evento_idevento = models.ForeignKey(Evento, on_delete = models.CASCADE, db_column='evento_idevento', related_name='eventohasregra_idevento')
    evento_regra_idevento_regra = models.ForeignKey('EventoRegra', on_delete = models.CASCADE, db_column='evento_regra_idevento_regra', related_name='eventohasregra_idevento_regra')

    class Meta:
        managed = False
        db_table = 'evento_has_regra'
        unique_together = (('evento_idevento', 'evento_regra_idevento_regra'),)


class EventoLista(models.Model):
    seq = models.AutoField(primary_key=True)
    evento_idevento = models.ForeignKey(Evento, on_delete = models.CASCADE, db_column='evento_idevento', related_name='eventolista_idevento')
    evento_lista_tipo_idevento_lista_tipo = models.ForeignKey('EventoListaTipo', on_delete = models.CASCADE, db_column='evento_lista_tipo_idevento_lista_tipo', related_name='eventolista_idevento_lista_tipo')
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)
    lista_level = models.IntegerField()
    item_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evento_lista'
        unique_together = (('seq', 'evento_idevento'),)
        
    def __str__(self):
        return str(self.evento_idevento) + '.' + str(self.seq) + ' - ' + self.nome


class EventoListaItem(models.Model):
    seq = models.AutoField(primary_key=True)
    evento_lista_seq = models.ForeignKey(EventoLista, on_delete = models.CASCADE, db_column='evento_lista_seq', related_name='eventolistaitem_lista_seq')
    evento_lista_evento_idevento = models.ForeignKey(EventoLista, on_delete = models.CASCADE, db_column='evento_lista_evento_idevento', related_name='eventolistaitem_idevento')
    descricao = models.CharField(max_length=45)
    quantidade_desejada_min = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evento_lista_item'
        unique_together = (('seq', 'evento_lista_seq', 'evento_lista_evento_idevento'),)
        
    def __str__(self):
        return str(self.evento_idevento) + '.' + str(self.evento_lista_seq) + '.' + str(self.seq)


class EventoListaTipo(models.Model):
    idevento_lista_tipo = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45)
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_lista_tipo'
        
    def __str__(self):
        return str(self.idevento_lista_tipo) + ' - ' + self.nome


class EventoOrganizacao(models.Model):
    evento_idevento = models.ForeignKey(Evento, on_delete = models.CASCADE, db_column='evento_idevento', related_name='eventoorganizacao_idevento')
    pessoa_idpessoa = models.ForeignKey('Pessoa', on_delete = models.CASCADE, db_column='pessoa_idpessoa', related_name='eventoorganizacao_idpessoa')
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evento_organizacao'
        unique_together = (('evento_idevento', 'pessoa_idpessoa'),)


class EventoParticipante(models.Model):
    participante_idpessoa = models.ForeignKey('Pessoa', on_delete = models.CASCADE, db_column='participante_idpessoa', related_name='eventoparticipante_idparticipante')
    evento_idevento = models.ForeignKey(Evento, on_delete = models.CASCADE, db_column='evento_idevento', related_name='eventoparticipante_idevento')
    participacao_status_idparticipacao_status = models.ForeignKey('ParticipacaoStatus', on_delete = models.CASCADE, db_column='participacao_status_idparticipacao_status', related_name='eventoparticipante_idparticipacao_status')

    class Meta:
        managed = False
        db_table = 'evento_participante'
        unique_together = (('participante_idpessoa', 'evento_idevento'),)


class EventoRegra(models.Model):
    idevento_regra = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45)
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_regra'
        
    def __str__(self):
        return str(self.idevento_regra) + ' - ' + self.nome


class EventoTipo(models.Model):
    idevento_tipo = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45)
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_tipo'
        
    def __str__(self):
        return str(self.idevento_tipo) + ' - ' + self.nome


class ItemPorPessoa(models.Model):
    pessoa_idpessoa = models.ForeignKey('Pessoa', on_delete = models.CASCADE, db_column='pessoa_idpessoa', related_name='itemporpessoa_idpessoa')
    evento_lista_item_seq = models.ForeignKey(EventoListaItem, on_delete = models.CASCADE, db_column='evento_lista_item_seq', related_name='itemporpessoa_item_seq')
    evento_lista_item_evento_lista_seq = models.ForeignKey(EventoListaItem, on_delete = models.CASCADE, db_column='evento_lista_item_evento_lista_seq', related_name='itemporpessoa_lista_seq')
    evento_lista_item_evento_lista_evento_idevento = models.ForeignKey(EventoListaItem, on_delete = models.CASCADE, db_column='evento_lista_item_evento_lista_evento_idevento', related_name='itemporpessoa_idevento')
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_por_pessoa'
        unique_together = (('pessoa_idpessoa', 'evento_lista_item_seq', 'evento_lista_item_evento_lista_seq', 'evento_lista_item_evento_lista_evento_idevento'),)


class ParticipacaoCondicao(models.Model):
    idparticipacao_condicao = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45)
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participacao_condicao'
        
    def __str__(self):
        return str(self.idparticipacao_condicao) + ' - ' + self.nome


class ParticipacaoStatus(models.Model):
    idparticipacao_status = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45)
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participacao_status'
        
    def __str__(self):
        return str(self.idparticipacao_status) + ' - ' + self.nome


class ParticipanteHasCondicao(models.Model):
    participacao_condicao_idparticipacao_condicao = models.ForeignKey(ParticipacaoCondicao, on_delete = models.CASCADE, db_column='participacao_condicao_idparticipacao_condicao', related_name='participantehascondicao_idparticipacao_condicao')
    evento_participante_participante_idpessoa = models.ForeignKey(EventoParticipante, on_delete = models.CASCADE, db_column='evento_participante_participante_idpessoa', related_name='participantehascondicao_idpessoa')
    evento_participante_evento_idevento = models.ForeignKey(EventoParticipante, on_delete = models.CASCADE, db_column='evento_participante_evento_idevento', related_name='participantehascondicao_idevento')

    class Meta:
        managed = False
        db_table = 'participante_has_condicao'
        unique_together = (('participacao_condicao_idparticipacao_condicao', 'evento_participante_participante_idpessoa', 'evento_participante_evento_idevento'),)


class PessoaGeneroSexual(models.Model):
    idpessoa_genero_sexual = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45)
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoa_genero_sexual'
        
    def __str__(self):
        return self.nome
        

class Regiao(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regiao'
        
    def __str__(self):
        return self.nome


class Estado(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigouf = models.IntegerField(db_column='CodigoUf')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.
    uf = models.CharField(db_column='Uf', max_length=2)  # Field name made lowercase.
    regiao = models.IntegerField(db_column='regiao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'
        
    def __str__(self):
        return self.nome + ' (' + self.uf + ')'
        

class Municipio(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    uf = models.CharField(db_column='Uf', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'municipio'
        
    def __str__(self):
        return '(' + self.uf + ') - ' + self.nome


class Bairro(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    uf = models.CharField(db_column='Uf', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bairro'
        
    def __str__(self):
        return self.nome


class Endereco(models.Model):
    idendereco = models.AutoField(primary_key=True)
    estado = models.ForeignKey('Estado', on_delete = models.CASCADE, db_column='estado_Id', related_name="endereco_estado_id", blank=True, null=True)  # Field name made lowercase.
    bairro = models.ForeignKey(Bairro, on_delete = models.CASCADE, db_column='bairro_Id', related_name="endereco_bairro_id", blank=True, null=True)  # Field name made lowercase.
    regiao = models.ForeignKey('Regiao', on_delete = models.CASCADE, db_column='regiao_Id', related_name='endereco_regiao_id', blank=True, null=True)  # Field name made lowercase.
    municipio = models.ForeignKey('Municipio', on_delete = models.CASCADE, db_column='municipio_Id', related_name='endereco_municipio_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'endereco'
    
    def __str__(self):
        endereco = ''
        #SOB_REFORMA
        '''if self.bairro != None:
            endereco += self.bairro.nome + '/'
        elif self.municipio != None:
            endereco += self.municipio.nome + '/'
        '''
        if self.municipio != None:
            endereco += self.municipio.nome + '/'
        if self.estado != None:
            endereco += self.estado.nome
        if endereco != '':
            return endereco
        return 'Brasil'


class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    idpessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    sobrenome = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    data_nascimento = models.DateField()
    email = models.CharField(unique=True, max_length=45)
    retrato_link = models.CharField(max_length=45, blank=True, null=True)
    pessoa_genero_sexual_idpessoa_genero_sexual = models.ForeignKey(PessoaGeneroSexual, on_delete = models.CASCADE, db_column='pessoa_genero_sexual_idpessoa_genero_sexual', related_name='pessoa_idpessoa_genero_sexual')
    endereco_idendereco = models.ForeignKey(Endereco, on_delete = models.CASCADE, db_column='endereco_idendereco', related_name='pessoa_idendereco')

    class Meta:
        managed = False
        db_table = 'pessoa'
    
    def getNomeCompleto(self):
        return self.nome + ' ' + self.sobrenome
        
    def getNickname(self):
        if self.nickname == None:
            return self.getNomeCompleto()
        return self.nickname
    
    def __str__(self):
        return str(self.idpessoa) + ' - ' + self.getNomeCompleto()
    
        
class PessoaAmizade(models.Model):
    pessoa_idpessoa1 = models.ForeignKey(Pessoa, on_delete = models.CASCADE, db_column='pessoa_idpessoa1', related_name='pessoaamizade_idpessoa1')
    pessoa_idpessoa2 = models.ForeignKey(Pessoa, on_delete = models.CASCADE, db_column='pessoa_idpessoa2', related_name='pessoaamizade_idpessoa2')
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pessoa_amizade'
        unique_together = (('pessoa_idpessoa1', 'pessoa_idpessoa2'),)


class TipoHasRegra(models.Model):
    evento_tipo_idevento_tipo = models.ForeignKey(EventoTipo, on_delete = models.CASCADE, db_column='evento_tipo_idevento_tipo', related_name='tipohasregra_idevento_tipo')
    evento_regra_idevento_regra = models.ForeignKey(EventoRegra, on_delete = models.CASCADE, db_column='evento_regra_idevento_regra', related_name='tipohasregra_idevento_regra')

    class Meta:
        managed = False
        db_table = 'tipo_has_regra'
        unique_together = (('evento_tipo_idevento_tipo', 'evento_regra_idevento_regra'),)

        
def is_not_new(self):
    #return Pessoa.objects.filter(user_id=self.id).exists()
    return Pessoa.objects.raw('SELECT idpessoa, count(idpessoa) AS pessoa_count FROM pessoa WHERE user_id = %s', [self.id])[0].pessoa_count > 0
    
User.add_to_class('is_not_new', is_not_new)
