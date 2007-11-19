class CanchaNoDisponibleError(Exception):
    pass

class ReservaSuperpuestaError(Exception):
    pass

class FichaMedicaVencidaError(Exception):
    def __init__(self, message):
        self.message = message

class SocioDeudorError(Exception):
    def __init__(self, message):
        self.message = message

class SocioSancionadoError(Exception):
    def __init__(self, message):
        self.message = message
