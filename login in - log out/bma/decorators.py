from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .models import Pessoa, Evento

def anonymous_required( view_function, redirect_to = None ):
    return AnonymousRequired( view_function, redirect_to )

class AnonymousRequired( object ):
    def __init__( self, view_function, redirect_to ):
        if redirect_to is None:
            from django.conf import settings
            redirect_to = settings.LOGIN_REDIRECT_URL
        self.view_function = view_function
        self.redirect_to = redirect_to

    def __call__( self, request, *args, **kwargs ):
        if request.user is not None and request.user.is_authenticated():
            return HttpResponseRedirect( self.redirect_to ) 
        return self.view_function( request, *args, **kwargs )
    
def user_is_not_new(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_not_new():
            return function(request, *args, **kwargs)
        elif user.is_superuser:
            return redirect('home')
        else:
            return redirect('usuario_registro', pk=user.id)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
        
def user_is_new(function):
    def wrap(request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs['pk'])
        except:
            raise Http404('(┛◉Д◉)┛彡┻━┻')
        if not request.user.is_superuser and user.id == request.user.id and Pessoa.objects.raw('SELECT idpessoa, COUNT(idpessoa) AS pessoa_count FROM pessoa WHERE user_id = %s', [user.id])[0].pessoa_count == 0:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_is_pessoa(function):
    def wrap(request, *args, **kwargs):
        try:
            user_id = Pessoa.objects.raw('SELECT * FROM pessoa WHERE idpessoa = %s', [kwargs['pk']])[0].user_id
        except:
            raise Http404('(ノಥ,_｣ಥ)ノ彡┻━┻')
        if user_id == request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
    
def user_has_access(function):
    def wrap(request, *args, **kwargs):
        try:
            user_id = Pessoa.objects.raw('SELECT * FROM pessoa WHERE idpessoa = %s', [kwargs['pk']])[0].user_id
        except:
            raise Http404('(ノಥ,_｣ಥ)ノ彡┻━┻')
        if request.user.is_superuser or user_id == request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_is_organizer(function):
    def wrap(request, *args, **kwargs):
        try:
            organizador_id = Pessoa.objects.raw('SELECT pessoa.* FROM pessoa, evento WHERE evento.idevento = %s AND evento.organizador_idpessoa = pessoa.idpessoa', [kwargs['pk']])[0].user_id
        except:
            raise Http404('(┛ಸ_ಸ)┛彡┻━┻')
        if request.user.is_superuser or organizador_id == request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_can_invite(function):
    def wrap(request, *args, **kwargs):
        try:
            organizador_id = Pessoa.objects.raw('SELECT pessoa.* FROM pessoa, evento WHERE evento.idevento = %s AND evento.organizador_idpessoa = pessoa.idpessoa', [kwargs['pk']])[0].user_id
        except:
            raise Http404('┻━┻ ︵﻿ ¯\(ツ)/¯ ︵ ┻━┻')
        participantes = Pessoa.objects.raw('SELECT pessoa.* FROM pessoa, evento_participante, evento, participacao_status WHERE evento.idevento=%s AND evento.idevento=evento_participante.evento_idevento AND evento_participante.participante_idpessoa=pessoa.idpessoa AND evento_participante.participacao_status_idparticipacao_status=participacao_status.idparticipacao_status AND participacao_status.codigo=%s', [kwargs['pk'], 'status_participante'])
        try:
            visitante = Pessoa.objects.raw('SELECT * FROM pessoa WHERE user_id=%s', [request.user.id])[0]
        except:
            visitante = None
        if visitante in participantes or organizador_id == request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap