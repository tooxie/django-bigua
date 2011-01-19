from django.template import Library, Node, TemplateSyntaxError
from menu.models import Menu, Link
from string import lower

register = Library()

class MenuNode(Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        try:
            html = '<ul class="%s">' % (lower(self.menu_name))
            menu = Menu.objects.get(nombre=self.menu_name)
            for link in menu.links.filter(desactivar=False):
                html += '<li class="%(class)s_link"><a href="%(href)s" title="%(title)s">%(text)s</a></li>' % { 'class': lower(self.menu_name), 'href': link.get_href(), 'title': link.nombre, 'text': link.nombre }
            html += '</ul>'
        except:
            html = ""
        #context['menu'] = "a"
        return html

def render_menu(parser, token):
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, "render_menu solo recibe un argumento, el nombre del menu."
    return MenuNode(bits[1])

menu = register.tag(render_menu)
