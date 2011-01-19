============
django-bigua
============

It's a web application developed as part of a System Analysis course in the Programmer Analyst carrer of ORT University. That's why all the documentation is in spanish. Sorry to the non-spanish speakers =/

The website itself was translated into english though =)


==============
Proyecto Biguá
==============

Un sistema de reserva de canchas de tenis, enfocado en usabilidad.

--------
¿Qué es?
--------

Es una aplicación web desarrollada como tercer obligatorio para la materia Análisis de Sistemas de la carrera Analista Programador de la Universidad ORT, Uruguay.

**Docente**: Carlos Nieves

Para obtener una copia del código fuente del sistema basta con clonar los fuentes del repositorio:

git clone git@github.com:tooxie/django-bigua.git


----------
Requisitos
----------

* Si estoy en el medio de una transacción extensa, que guarde registros en caso de caída del sistema.
* Utilizar iconos, no solo texto.
* Colores amigables.
* Letra grande.
* Ayuda en línea.
* Idiomas.
* Estadísticas. Permitir filtrar los datos por variados parámetros.


---------------
Datos de prueba
---------------

Socio
-----

* Usuario: ana
* Password: ana

* Usuario: danny
* Password: danny

Administrador
-------------

* Usuario: alvaro
* Password: alvaro

Use con responsabilidad =)

---------------
Desarrolladores
---------------

* Alvaro Mouriño
* Daniel Alaniz


---------------
Características
---------------

Sitio desarrollado en python, sobre django. Puedes leer toda la documentación de django, este maravilloso framework para desarrollo web, en el sitio del proyecto donde además encontrarás una guía paso a paso de como instalarlo en tu sistema operativo preferido.

* Diseñado potenciando la usabilidad sin sacrificar accesibilidad.
* Todo el sitio es usable sin javascript.
* A partir de las 11:50 se habilita el alquiler para el día siguiente: Para esto chequea contra un servidor NTP la hora actual, si éste no responde, o no devuelve información comprensible se utiliza la hora del sistema (servidor).
* 100% traducido al inglés.
* 100% traducible a otros idiomas.
* XHTML 1.0 válido.
* Diseño testeado en IE, Gecko y KHTML.

Apps y bibliotecas de terceros
------------------------------

* django-menuse: Una app para crear menús muy sencilla y práctica.
* De toda la mágia de la traducción de contenidos se encarga django-multilingual.
* Todo el client-side eye-candy se lo debemos a jquery.
* Utiliza también behaviour para aplicar reglas de javascript.
* Los excelentes iconos son gracias al trabajo del Proyecto Tango Desktop.

------------
Bibliografía
------------

* "Don't make me think" Steve Krug. New Riders.
* "Designing Interfaces" Jenifer Tidwell. O'Reilly.

Ambos libros prestados por la biblioteca de la Universidad. El primero es realmente excelente, sumamente recomendable.
En fin...

Nosotros aprendimos mucho haciéndolo, esperamos que a vos también te sirva.


-----
FIXME
-----

Por alguna extraña razón solo funciona en Firefox, en un principio funcionaba también en Internet Exploiter 6 y Konqueror (¿podemos asumir que en Safari también?) pero behaviour tiene algúna incompatibilidad que rompe todo.


----
TODO
----

Reemplazar la funcionalidad que se utilizaba de behaviour por jquery.

:wq
