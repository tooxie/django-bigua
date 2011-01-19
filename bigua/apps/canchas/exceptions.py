# coding=UTF-8
class CanchaNoDisponibleError(Exception):
    def __init__(self, message):
        self.message = message
        self.args = message

    def __unicode__(self):
        return self.message

class ReservaSuperpuestaError(Exception):
    def __init__(self, message):
        self.message = message
        self.args = message

    def __unicode__(self):
        return self.message

class ReservaAntesDeHorarioError(Exception):
    def __init__(self, message):
        self.message = message
        self.args = message

    def __unicode__(self):
        return self.message

class FichaMedicaVencidaError(Exception):
    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return self.message

class SocioSancionadoError(Exception):
    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return self.message

class SocioDeudorError(Exception):
    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return self.message

class SocioSancionadoError(Exception):
    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return self.message

class NTPInvalidResponseError(Exception):
    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return self.message

class NTPNoDataReturnedError(Exception):
    def __init__(self, message):
        self.message = message

    def __unicode__(self):
        return self.message

