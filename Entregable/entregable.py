# pip install requests
import requests

# Torrente, el brazo tonto de la ley
r = requests.get('https://www.filmaffinity.com/es/film334167.html')

html = r.text

diccionario = {}

espacio = '&nbsp;'
dd = '<dd>'
dd_c = '</dd>'
span = '<span>'
span_c = '</span>'
div_c = '</div>'


def titulo_original(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def anio(html):
    label = html[html.find('<dt>Año</dt>'):html.find(dd_c)]
    print(label)
    # anio = label[label.find(dd):].splitlines()[1]
    # print(anio)
    # anio = anio.lstrip().rstrip()
    # return anio

def duracion(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def pais(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def direccion(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def guion(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def musica(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def fotografia(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def reparto(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def productora(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def genero(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def sinopsis(html):
    label = html[html.find('<dt>Título original</dt>'):html.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

diccionario["titulo_original"] = titulo_original(html)
diccionario["año"] = anio(html)

# print(diccionario)