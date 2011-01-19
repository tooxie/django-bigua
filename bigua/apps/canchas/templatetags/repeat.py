from django.template import Library, Node

register = Library()

class RepeatNode(Node):
    def __init__(self, repeated_string):
        self.repeated_string = repeated_string

    def render(self, context):
        return self.repeated_string

def repeat(parser, token):
    bits = token.contents.split()
    if len(bits) != 3:
        raise TemplateSyntaxError, "repeat recibe dos argumentos, el texto a repetir y la cantidad de veces."
    repeated_string = ''
    x = 0
    while x < int(bits[2]):
        repeated_string += bits[1]
        x = x + 1
    return RepeatNode(repeated_string)

rep = register.tag(repeat)
