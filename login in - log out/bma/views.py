from django.shortcuts import render, redirect
from django.http import Http404
from django.db import connection
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .decorators import *
from .enciclopedia import *


# Create your views here.
def main(request):
    eventos = []
    data_hoje = getTodayDate()
    hora_agora = getTimeNow()
    total_img = 8
    for e in Evento.objects.raw('SELECT * FROM evento WHERE (data_inicio > %s) OR (data_inicio = %s AND (horario_fim >= %s OR horario_fim IS NULL)) ORDER BY data_inicio ASC LIMIT %s', [data_hoje, data_hoje, hora_agora, total_img]):
        eventos.append(e)
    return render(request, 'bma/main.html', {'eventos': eventos})

@login_required
@user_is_not_new
def login_feito(request):
    return redirect('home')

@anonymous_required
def usuario_auth(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('usuario_registro', pk=user.id)
    else:
        user_form = UserCreationForm()
    titulo_inicial = 'Cadastre-se!!!'
    return render(request, 'bma/form_user.html', {'user_form': user_form, 'titulo_inicial': titulo_inicial})

@login_required
@user_is_new
def usuario_registro(request, pk):
    if request.method == "POST":
        pessoa_form = PessoaForm(request.POST)
        if pessoa_form.is_valid():
            if request.FILES.get('img_upload', False):
                imagem = request.FILES['img_upload']
                retrato_link = uploadToImgur(imagem, 'usuario_foto')
            else:
                retrato_link = None
            nome = pessoa_form.cleaned_data['nome']
            sobrenome = pessoa_form.cleaned_data['sobrenome']
            nickname = pessoa_form.cleaned_data['nickname']
            data_nascimento = pessoa_form.cleaned_data['data_nascimento']
            email = pessoa_form.cleaned_data['email']
            genero_id = pessoa_form.data['pessoa_genero_sexual_idpessoa_genero_sexual']
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO endereco () VALUES ()')
                cursor.execute('INSERT INTO pessoa (user_id, nome, sobrenome, nickname, data_nascimento, email, retrato_link, pessoa_genero_sexual_idpessoa_genero_sexual, endereco_idendereco) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', [pk, nome, sobrenome, nickname, data_nascimento, email, retrato_link, genero_id, cursor.lastrowid])
                return redirect('usuario_edicao_estado', pk=cursor.lastrowid)
    else:
        pessoa_form = PessoaForm()
    titulo_inicial = 'Preencha seus dados para continuar!'
    mensagem_imagem = 'Carregue sua imagem de perfil!'
    generos = []
    for g in PessoaGeneroSexual.objects.raw('SELECT * FROM pessoa_genero_sexual'):
        generos.append(g)
    return render(request, 'bma/form_pessoa.html', {'pessoa_form': pessoa_form, 'titulo_inicial': titulo_inicial, 'mensagem_imagem': mensagem_imagem, 'generos': generos})

@login_required
@user_has_access
def usuario_edicao(request, pk):
    try:
        p_inst = Pessoa.objects.raw('SELECT * FROM pessoa WHERE idpessoa=%s', [pk])[0]
    except:
        raise Http404('(╯ರ ~ ರ）╯︵ ┻━┻')
    if request.method == "POST":
        pessoa_form = PessoaForm(request.POST, instance=p_inst)
        if pessoa_form.is_valid():
            if request.FILES.get('img_upload', False):
                imagem = request.FILES['img_upload']
                retrato_link = uploadToImgur(imagem, 'usuario_foto')
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE pessoa SET retrato_link=%s WHERE idpessoa=%s', [retrato_link, pk])
            nome = pessoa_form.cleaned_data['nome']
            sobrenome = pessoa_form.cleaned_data['sobrenome']
            nickname = pessoa_form.cleaned_data['nickname']
            data_nascimento = pessoa_form.cleaned_data['data_nascimento']
            email = pessoa_form.cleaned_data['email']
            genero_id = pessoa_form.data['pessoa_genero_sexual_idpessoa_genero_sexual']
            with connection.cursor() as cursor:
                cursor.execute('UPDATE pessoa SET nome=%s, sobrenome=%s, nickname=%s, data_nascimento=%s, email=%s, pessoa_genero_sexual_idpessoa_genero_sexual=%s WHERE idpessoa=%s', [nome, sobrenome, nickname, data_nascimento, email, genero_id, pk])
                return redirect('usuario_perfil', pk=pk)
    else:
        pessoa_form = PessoaForm(instance=p_inst)
    titulo_inicial = 'Edite seu perfil'
    mensagem_imagem = 'Altere sua imagem de perfil!'
    generos = []
    for g in PessoaGeneroSexual.objects.raw('SELECT * FROM pessoa_genero_sexual'):
        generos.append(g)
    return render(request, 'bma/form_pessoa.html', {'pessoa_form': pessoa_form, 'titulo_inicial': titulo_inicial, 'mensagem_imagem': mensagem_imagem, 'generos': generos})

@login_required
@user_has_access
def usuario_edicao_estado(request, pk):
    endereco_id = Endereco.objects.raw('SELECT endereco.idendereco FROM endereco, pessoa WHERE pessoa.idpessoa = %s AND pessoa.endereco_idendereco = endereco.idendereco', [pk])[0].idendereco
    if request.method == "POST":
        id = request.POST.get('Estado')
        with connection.cursor() as cursor:
            if id == '0':
                cursor.execute('UPDATE endereco SET estado_Id = %s, municipio_Id =%s, bairro_Id=%s WHERE idendereco = %s', [None, None, None, endereco_id])
                return redirect('usuario_perfil', pk=pk)
            else:
                cursor.execute('UPDATE endereco SET estado_Id = %s WHERE idendereco = %s', [id, endereco_id])
                return redirect('usuario_edicao_municipio', pk=pk)
    estados = []
    inst_id = None
    try:
        inst_id = Estado.objects.raw('SELECT estado.Id FROM estado, endereco WHERE endereco.idendereco = %s AND endereco.estado_Id = estado.Id', [endereco_id])[0].id
    except: pass
    for e in Estado.objects.raw('SELECT * FROM estado ORDER BY nome'):
        estados.append(e)
    return render(request, 'bma/form_estado.html', {'estados': estados, 'inst_id': inst_id, 'pk': pk})

@login_required
@user_has_access
def usuario_edicao_municipio(request, pk):
    endereco_id = Endereco.objects.raw('SELECT endereco.idendereco FROM endereco, pessoa WHERE pessoa.idpessoa = %s AND pessoa.endereco_idendereco = endereco.idendereco', [pk])[0].idendereco
    if request.method == "POST":
        id = request.POST.get('Municipio')
        with connection.cursor() as cursor:
            if id == '0':
                cursor.execute('UPDATE endereco SET municipio_Id =%s, bairro_Id=%s WHERE idendereco = %s', [None, None, endereco_id])
                return redirect('usuario_perfil', pk=pk)
            else:
                cursor.execute('UPDATE endereco SET Municipio_Id = %s WHERE idendereco = %s', [id, endereco_id])
                #SOB_REFORMA return redirect('usuario_edicao_bairro', pk=pk)
                return redirect('usuario_perfil', pk=pk)
    municipios = []
    inst_id = None
    try:
        inst_id = Municipio.objects.raw('SELECT municipio.Id FROM municipio, endereco WHERE endereco.idendereco = %s AND endereco.municipio_Id = municipio.Id', [endereco_id])[0].id
    except: pass
    uf = Estado.objects.raw('SELECT estado.* FROM estado, endereco WHERE endereco.idendereco = %s AND endereco.estado_Id = estado.Id', [endereco_id])[0].uf
    for m in Municipio.objects.raw('SELECT * FROM municipio WHERE uf = %s ORDER BY nome', [uf]):
        municipios.append(m)
    return render(request, 'bma/form_municipio.html', {'municipios': municipios, 'inst_id': inst_id, 'pk': pk})
'''
@login_required
@user_has_access
def usuario_edicao_bairro(request, pk):
    endereco_id = Endereco.objects.raw('SELECT endereco.idendereco FROM endereco, pessoa WHERE pessoa.idpessoa = %s AND pessoa.endereco_idendereco = endereco.idendereco', [pk])[0].idendereco
    if request.method == "POST":
        id = request.POST.get('Bairro')
        if id == '0': id = None
        with connection.cursor() as cursor:
            cursor.execute('UPDATE endereco SET bairro_Id = %s WHERE idendereco = %s', [id, endereco_id])
            return redirect('usuario_perfil', pk=pk)
    bairros = []
    inst_id = None
    try:
        inst_id = Bairro.objects.raw('SELECT bairro.Id FROM bairro, endereco WHERE endereco.idendereco = %s AND endereco.bairro_Id = bairro.Id', [endereco_id])[0].id
    except: pass
    mun_cod = Municipio.objects.raw('SELECT municipio.* FROM municipio, endereco WHERE endereco.idendereco = %s AND endereco.municipio_Id = municipio.Id', [endereco_id])[0].codigo
    mun_cod_left = mun_cod * 1000
    mun_cod_right = (mun_cod+1) * 1000
    for b in Bairro.objects.raw('SELECT * FROM bairro WHERE codigo > %s AND codigo < %s  ORDER BY nome', [mun_cod_left, mun_cod_right]):
        bairros.append(b)
    return render(request, 'bma/form_bairro.html', {'bairros': bairros, 'inst_id': inst_id, 'pk': pk})
'''
@login_required
@user_is_not_new
def usuario_profile(request, pk):
    id_pessoa = Pessoa.objects.raw('SELECT idpessoa FROM pessoa WHERE user_id=%s', [pk])[0].idpessoa
    return redirect('usuario_perfil', pk = id_pessoa)
    
def usuario_perfil(request, pk):
    try:
        perfil = Pessoa.objects.raw('SELECT *, YEAR(CURDATE())-YEAR(data_nascimento)-IF(MONTH(CURDATE())*32+DAY(CURDATE())<MONTH(data_nascimento)*32+DAY(data_nascimento),1,0) AS idade FROM pessoa WHERE idpessoa=%s', [pk])[0]
    except:
        raise Http404('(┛✧Д✧))┛彡┻━┻')
    try:
        visitante = Pessoa.objects.raw('SELECT * FROM pessoa WHERE user_id=%s', [request.user.id])[0]
        id_visitante = visitante.idpessoa
    except:
        visitante = None
        id_visitante = None
    if request.method == "POST":
        tipo = request.POST.get('botao_amizade')
        with connection.cursor() as cursor:
            if (tipo == 'adicionar'):
                cursor.execute('INSERT INTO pessoa_amizade (pessoa_idpessoa1, pessoa_idpessoa2, status) VALUES (%s, %s, %s)', [id_visitante, pk, False])
            elif (tipo == 'aceitar'):
                cursor.execute('UPDATE pessoa_amizade SET status=%s WHERE pessoa_idpessoa1=%s AND pessoa_idpessoa2=%s', [True, pk, id_visitante])
            elif (tipo == 'desfazer'):
                cursor.execute('DELETE FROM pessoa_amizade WHERE (pessoa_idpessoa1=%s AND pessoa_idpessoa2=%s) OR (pessoa_idpessoa2=%s AND pessoa_idpessoa1=%s)', [pk, id_visitante, pk, id_visitante])
            elif (tipo == 'cancelar'):
                cursor.execute('DELETE FROM pessoa_amizade WHERE pessoa_idpessoa1=%s AND pessoa_idpessoa2=%s', [id_visitante, pk])
            elif (tipo == 'recusar'):
                cursor.execute('DELETE FROM pessoa_amizade WHERE pessoa_idpessoa1=%s AND pessoa_idpessoa2=%s', [pk, id_visitante])
            elif (tipo == 'excluir'):
                user_id = Pessoa.objects.raw('SELECT * FROM pessoa WHERE idpessoa=%s', [pk])[0].user_id
                cursor.execute('DELETE FROM pessoa WHERE idpessoa=%s', [pk])
                u = User.objects.get(id = user_id)
                u.delete()
                return redirect('logout')
            return redirect('usuario_perfil', pk=pk)
    perfil.lista_amigos = []
    for amigo in Pessoa.objects.raw('SELECT pessoa.*, pessoa_amizade.* FROM pessoa, pessoa_amizade WHERE (pessoa_amizade.pessoa_idpessoa1=%s AND pessoa_amizade.pessoa_idpessoa2=pessoa.idpessoa) OR (pessoa_amizade.pessoa_idpessoa2=%s AND pessoa_amizade.pessoa_idpessoa1=pessoa.idpessoa) ORDER BY CASE WHEN pessoa.idpessoa=%s THEN 1 ELSE 2 END, pessoa.idpessoa', [pk, pk, id_visitante]):
        perfil.lista_amigos.append(amigo)
    perfil.lista_eventos_org = []
    perfil.lista_eventos_org_old = []
    perfil.lista_eventos = []
    perfil.lista_eventos_old = []
    data_hoje = getTodayDate()
    hora_agora = getTimeNow()
    for evento in Evento.objects.raw('SELECT DISTINCT evento.*, ((data_inicio > %s) OR (data_inicio = %s AND (horario_fim >= %s OR horario_fim IS NULL))) as is_not_old FROM evento, evento_participante, participacao_status WHERE (evento.organizador_idpessoa=%s) OR (evento_participante.participante_idpessoa=%s AND evento_participante.participacao_status_idparticipacao_status = participacao_status.idparticipacao_status AND participacao_status.codigo=%s AND evento_participante.evento_idevento = evento.idevento) ORDER BY evento.data_inicio', [data_hoje, data_hoje, hora_agora, pk, pk, 'status_participante']):
        if evento.is_not_old:
            if evento.organizador_idpessoa.idpessoa == int(pk):
                perfil.lista_eventos_org.append(evento)
            else:
                perfil.lista_eventos.append(evento)
        else:
            if evento.organizador_idpessoa.idpessoa == int(pk):
                perfil.lista_eventos_org_old.append(evento)
            else:
                perfil.lista_eventos_old.append(evento)
    convites_de_evento_count = Evento.objects.raw('SELECT evento.idevento, COUNT(evento.idevento) AS convites_count FROM evento, evento_participante, participacao_status WHERE evento_participante.participante_idpessoa=%s AND evento_participante.participacao_status_idparticipacao_status = participacao_status.idparticipacao_status AND participacao_status.codigo=%s AND evento_participante.evento_idevento = evento.idevento', [pk, 'status_convidado'])[0].convites_count
    pedidos_de_amizade_count = Pessoa.objects.raw('SELECT pessoa.idpessoa, COUNT(pessoa.idpessoa) AS pedidos_count FROM pessoa, pessoa_amizade WHERE pessoa.idpessoa = pessoa_amizade.pessoa_idpessoa1 AND pessoa_amizade.pessoa_idpessoa2=%s AND pessoa_amizade.status=%s', [pk, False])[0].pedidos_count
    notificacoes_count = convites_de_evento_count + pedidos_de_amizade_count
    return render(request, 'bma/usuario_perfil.html', {'perfil': perfil, 'visitante': visitante, 'notificacoes_count': notificacoes_count})
    
@login_required
@user_is_pessoa
def usuario_notificacoes(request, pk):
    convites_de_evento = Evento.objects.raw('SELECT evento.* FROM evento, evento_participante, participacao_status WHERE evento_participante.participante_idpessoa=%s AND evento_participante.participacao_status_idparticipacao_status = participacao_status.idparticipacao_status AND participacao_status.codigo=%s AND evento_participante.evento_idevento = evento.idevento', [pk, 'status_convidado'])
    pedidos_de_amizade = Pessoa.objects.raw('SELECT pessoa.* FROM pessoa, pessoa_amizade WHERE pessoa.idpessoa = pessoa_amizade.pessoa_idpessoa1 AND pessoa_amizade.pessoa_idpessoa2=%s AND pessoa_amizade.status=%s', [pk, False])
    return render(request, 'bma/usuario_notificacoes.html', {'convites_de_evento': convites_de_evento, 'pedidos_de_amizade': pedidos_de_amizade})
    
def listar_usuarios(request):
    pessoas = []
    for p in Pessoa.objects.raw('SELECT *, YEAR(CURDATE())-YEAR(data_nascimento)-IF(MONTH(CURDATE())*32+DAY(CURDATE())<MONTH(data_nascimento)*32+DAY(data_nascimento),1,0) AS idade FROM pessoa ORDER BY IFNULL(nickname, nome)'):
        pessoas.append(p)
    return render(request, 'bma/usuario_lista.html', {'pessoas': pessoas})

@login_required
@user_is_not_new
def evento_registro(request):
    if request.method == "POST":
        evento_form = EventoForm(request.POST)
        if evento_form.is_valid():
            if request.FILES.get('img_upload', False):
                imagem = request.FILES['img_upload']
                banner_link = uploadToImgur(imagem, 'evento_banner')
            else:
                banner_link = None
            nome = evento_form.cleaned_data['nome']
            data_inicio = evento_form.cleaned_data['data_inicio']
            data_fim = data_inicio
            horario_inicio = evento_form.cleaned_data['horario_inicio']
            if horario_inicio == None:
                horario_inicio = '00:00'
            horario_fim = evento_form.cleaned_data['horario_fim']
            if horario_fim == None:
                horario_fim = '23:59'
            local = evento_form.cleaned_data['local']
            evento_tipo_idevento_tipo = evento_form.data['evento_tipo_idevento_tipo']
            organizador_idpessoa = Pessoa.objects.raw('SELECT idpessoa from pessoa WHERE user_id = %s', [request.user.id])[0].idpessoa
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO evento (nome, data_inicio, data_fim, horario_inicio, horario_fim, local, banner_link, evento_tipo_idevento_tipo, organizador_idpessoa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', [nome, data_inicio, data_fim, horario_inicio, horario_fim, local, banner_link, evento_tipo_idevento_tipo, organizador_idpessoa])
                evento_id = cursor.lastrowid
                cursor.execute('INSERT INTO evento_has_regra (evento_idevento, evento_regra_idevento_regra) SELECT evento.idevento, evento_regra.idevento_regra FROM evento, evento_regra WHERE evento.idevento=%s AND evento_regra.codigo=%s', [evento_id, 'visib_publico'])
                return redirect('evento_perfil', pk=evento_id)
    else:
        evento_form = EventoForm()
    titulo_inicial = 'Registre seu evento!'
    mensagem_imagem = 'Carregue uma imagem de banner!'
    tipos = []
    for t in EventoTipo.objects.raw('SELECT * FROM evento_tipo'):
        tipos.append(t)
    return render(request, 'bma/form_evento.html', {'evento_form': evento_form, 'titulo_inicial': titulo_inicial, 'mensagem_imagem': mensagem_imagem, 'tipos': tipos})

@login_required
@user_is_organizer
def evento_edicao(request, pk):
    try:
        e_inst = Evento.objects.raw('SELECT * FROM evento WHERE idevento=%s', [pk])[0]
    except:
        raise Http404('(ﾉ´･ω･)ﾉ ﾐ ┸━┸')
    if request.method == "POST":
        evento_form = EventoForm(request.POST, instance=e_inst)
        if evento_form.is_valid():
            if request.FILES.get('img_upload', False):
                imagem = request.FILES['img_upload']
                banner_link = uploadToImgur(imagem, 'evento_banner')
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE evento SET banner_link=%s WHERE idevento=%s', [banner_link, pk])
            nome = evento_form.cleaned_data['nome']
            data_inicio = evento_form.cleaned_data['data_inicio']
            horario_inicio = evento_form.cleaned_data['horario_inicio']
            if horario_inicio == None:
                horario_inicio = '00:00'
            horario_fim = evento_form.cleaned_data['horario_fim']
            if horario_fim == None:
                horario_fim = '23:59'
            local = evento_form.cleaned_data['local']
            evento_tipo_idevento_tipo = evento_form.data['evento_tipo_idevento_tipo']
            with connection.cursor() as cursor:
                cursor.execute('UPDATE evento SET nome=%s, data_inicio=%s, horario_inicio=%s, horario_fim=%s, local=%s, evento_tipo_idevento_tipo=%s WHERE idevento=%s', [nome, data_inicio, horario_inicio, horario_fim, local, evento_tipo_idevento_tipo, pk])
                return redirect('evento_perfil', pk=pk)
    else:
        evento_form = EventoForm(instance=e_inst)
    titulo_inicial = 'Edite seu evento'
    mensagem_imagem = 'Altere o banner do evento!'
    tipos = []
    for t in EventoTipo.objects.raw('SELECT * FROM evento_tipo'):
        tipos.append(t)
    return render(request, 'bma/form_evento.html', {'evento_form': evento_form, 'titulo_inicial': titulo_inicial, 'mensagem_imagem': mensagem_imagem, 'tipos': tipos})
    
def evento_perfil(request, pk):
    data_hoje = getTodayDate()
    hora_agora = getTimeNow()
    try:
        perfil = Evento.objects.raw('SELECT *, ((data_inicio > %s) OR (data_inicio = %s AND (horario_fim >= %s OR horario_fim IS NULL))) AS is_not_old, (data_inicio=%s AND (horario_inicio <= %s OR horario_inicio IS NULL) AND (horario_fim <= %s OR horario_fim IS NULL)) AS is_now FROM evento WHERE idevento=%s', [data_hoje, data_hoje, hora_agora, data_hoje, hora_agora, hora_agora, pk])[0]
    except:
        raise Http404('(╯°□°）╯︵ ┻━┻')
    try:
        visitante = Pessoa.objects.raw('SELECT * FROM pessoa WHERE user_id=%s', [request.user.id])[0]
        id_visitante = visitante.idpessoa
    except:
        visitante = None
        id_visitante = None
    perfil.lista_membros = []
    for membro in Pessoa.objects.raw('SELECT pessoa.*, participacao_status.codigo AS codigo FROM pessoa, evento, evento_participante, participacao_status WHERE evento.idevento=%s AND evento.idevento = evento_participante.evento_idevento AND evento_participante.participante_idpessoa = pessoa.idpessoa AND evento_participante.participacao_status_idparticipacao_status = participacao_status.idparticipacao_status ORDER BY CASE WHEN pessoa.idpessoa=%s THEN 1 ELSE 2 END, pessoa.idpessoa', [pk, id_visitante]):
        perfil.lista_membros.append(membro)
    perfil.ativos_count = 0
    if (len(perfil.lista_membros) > 0):
        perfil.convidados_count = 0
        perfil.participantes_count = 0
        perfil.membros_count = ParticipacaoStatus.objects.raw('SELECT participacao_status.*, COUNT(participacao_status.idparticipacao_status) AS status_total FROM evento, evento_participante, participacao_status WHERE evento.idevento=%s AND evento.idevento = evento_participante.evento_idevento AND evento_participante.participacao_status_idparticipacao_status = participacao_status.idparticipacao_status GROUP BY participacao_status.idparticipacao_status', [pk])
        for count in perfil.membros_count:
            if (count.codigo == 'status_convidado'):
                perfil.convidados_count += count.status_total
                perfil.ativos_count += perfil.convidados_count
            elif (count.codigo == 'status_participante'):
                perfil.participantes_count += count.status_total
                perfil.ativos_count += perfil.participantes_count
        if (perfil.ativos_count > 0):
            perfil.convidados_per = (perfil.convidados_count * 100)//perfil.ativos_count
            perfil.participantes_per = (perfil.participantes_count * 100)//perfil.ativos_count
    perfil.lista_membros.append(Pessoa.objects.raw('SELECT pessoa.* FROM pessoa, evento WHERE evento.idevento=%s AND evento.organizador_idpessoa=pessoa.idpessoa', [pk])[0])
    if request.method == "POST":
        tipo = request.POST.get('botao_evento')
        with connection.cursor() as cursor:
            if (tipo == 'convidar'):
                return redirect('evento_convidar', pk=pk)
            if (tipo == 'participar'):
                if (visitante in perfil.lista_membros):
                    cursor.execute('UPDATE evento_participante SET participacao_status_idparticipacao_status=(SELECT idparticipacao_status FROM participacao_status WHERE codigo=%s) WHERE evento_participante.evento_idevento=%s AND evento_participante.participante_idpessoa=%s;', ['status_participante', pk, id_visitante])
                else:
                    cursor.execute('INSERT INTO evento_participante (participante_idpessoa, evento_idevento, participacao_status_idparticipacao_status) VALUES (%s, %s, (SELECT idparticipacao_status FROM participacao_status WHERE codigo=%s))', [id_visitante, pk, 'status_participante'])
            elif (tipo == 'aceitar'):
                cursor.execute('UPDATE evento_participante SET participacao_status_idparticipacao_status=(SELECT idparticipacao_status FROM participacao_status WHERE codigo=%s) WHERE evento_participante.evento_idevento=%s AND evento_participante.participante_idpessoa=%s;', ['status_participante', pk, id_visitante])
            elif (tipo == 'recusar'):
                cursor.execute('UPDATE evento_participante SET participacao_status_idparticipacao_status=(SELECT idparticipacao_status FROM participacao_status WHERE codigo=%s) WHERE evento_participante.evento_idevento=%s AND evento_participante.participante_idpessoa=%s;', ['status_recusado', pk, id_visitante])
            elif (tipo == 'sair'):
                cursor.execute('UPDATE evento_participante SET participacao_status_idparticipacao_status=(SELECT idparticipacao_status FROM participacao_status WHERE codigo=%s) WHERE evento_participante.evento_idevento=%s AND evento_participante.participante_idpessoa=%s;', ['status_recusado', pk, id_visitante])
            elif (tipo == 'excluir'):
                cursor.execute('DELETE FROM evento WHERE idevento=%s', [pk])
                return redirect('home')
            return redirect('evento_perfil', pk=pk)
    med_idade = Pessoa.objects.raw('SELECT idpessoa, ROUND(AVG(YEAR(CURDATE())-YEAR(data_nascimento)-IF(MONTH(CURDATE())*32+DAY(CURDATE())<MONTH(data_nascimento)*32+DAY(data_nascimento),1,0))) AS med_idade FROM evento, evento_participante, participacao_status, pessoa WHERE evento.idevento = %s AND evento.idevento = evento_participante.evento_idevento AND evento_participante.participacao_status_idparticipacao_status = participacao_status.idparticipacao_status AND participacao_status.codigo = %s AND evento_participante.participante_idpessoa = pessoa.idpessoa', [pk, 'status_participante'])[0].med_idade
    return render(request, 'bma/evento_perfil.html', {'perfil': perfil, 'visitante': visitante, 'med_idade': med_idade})

def listar_eventos(request):
    eventos = []
    eventos_old = []
    horario_agora = getDateTimeNow()
    for p in Evento.objects.raw('SELECT evento.*, TIMESTAMP(evento.data_inicio, evento.horario_inicio) AS inicio, TIMESTAMP(evento.data_fim, evento.horario_fim) AS final, EXTRACT(YEAR FROM evento.data_inicio) AS AnoEvento, EXTRACT(MONTH FROM evento.data_inicio) AS MesEvento, (SELECT COUNT(evento_participante.participante_idpessoa) FROM evento_participante, participacao_status WHERE evento_participante.evento_idevento=evento.idevento AND evento_participante.participacao_status_idparticipacao_status = participacao_status.idparticipacao_status AND participacao_status.codigo=%s) AS participantes_count FROM evento ORDER BY evento.data_inicio ASC', ['status_participante']):
        if (str(p.final) > horario_agora):
            eventos.append(p)
        else:
            eventos_old.append(p)
    return render(request, 'bma/evento_lista.html', {'eventos': eventos, 'eventos_old': eventos_old})

@login_required
@user_can_invite
def evento_convidar(request, pk):
    try:
        perfil = Evento.objects.raw('SELECT * FROM evento WHERE idevento=%s', [pk])[0]
    except:
        raise Http404('┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻')
    if request.method == "POST":
        convidados = request.POST.getlist('amigo')
        with connection.cursor() as cursor:
            for convidado in convidados:
                cursor.execute('INSERT INTO evento_participante (participante_idpessoa, evento_idevento, participacao_status_idparticipacao_status) VALUES (%s, %s, (SELECT idparticipacao_status FROM participacao_status WHERE codigo=%s))', [convidado, pk, 'status_convidado'])
            return redirect('evento_perfil', pk=pk)
    visitante = Pessoa.objects.raw('SELECT * FROM pessoa WHERE user_id=%s', [request.user.id])[0]
    lista_amigos = []
    for amigo in Pessoa.objects.raw('SELECT DISTINCT pessoa.* FROM pessoa, pessoa_amizade, evento, evento_participante WHERE (pessoa.idpessoa NOT IN (SELECT participante_idpessoa FROM evento_participante WHERE evento_idevento=%s)) AND (pessoa.idpessoa NOT IN (SELECT organizador_idpessoa FROM evento WHERE idevento=%s)) AND (pessoa_amizade.status = %s) AND ((pessoa_amizade.pessoa_idpessoa1=%s AND pessoa_amizade.pessoa_idpessoa2=pessoa.idpessoa) OR (pessoa_amizade.pessoa_idpessoa2=%s AND pessoa_amizade.pessoa_idpessoa1=pessoa.idpessoa)) ORDER BY pessoa.nome', [pk, pk, True, visitante.idpessoa, visitante.idpessoa]):
        lista_amigos.append(amigo)
    return render(request, 'bma/evento_convidar.html', {'perfil': perfil, 'lista_amigos': lista_amigos})
