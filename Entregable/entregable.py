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

def anyo(html):
    label = html[html.find("<dt>Año</dt>"):]
    anyo = label[label.find("datePublished"):label.find(dd_c)]
    anyo = anyo[anyo.find(">") + 1:]
    return anyo

def duracion(html):
    label = html[html.find("<dt>Duración</dt>"):]
    duracion = label[label.find("duration"):label.find(dd_c)]
    duracion = duracion[duracion.find(">") + 1:]
    return duracion

def pais(html):
    label = html[html.find("<dt>País</dt>"):]
    pais = label[label.find(dd):label.find(dd_c)]
    pais = pais[pais.find(span_c):]
    pais = pais[pais.find(";") + 1:]
    return pais

def direccion(html):
    label = html[html.find("<dt>Dirección</dt>"):]
    directors = label[label.find("directors"):label.find(dd_c)]
    directors = directors[directors.find("credits"):directors.find(div_c)]
    directors = directors[directors.find("director"):directors.find(span_c)]
    directors = directors[directors.find("Santiago Segura"):directors.find("</a>")]
    directors = directors[directors.find("name"):directors.find(span_c)]
    directors = directors[directors.find(">") + 1:]
    return directors

def guion(html):
    label = html[html.find("<dt>Guion</dt>"):]
    guion = label[label.find("credits"):label.find(div_c)]
    guion = guion[guion.find("nb"):guion.find(span_c)]
    guion = guion[guion.find(span):]
    guion = guion[guion.find(">") + 1:]
    return guion

def musica(html):
    label = html[html.find("<dt>Música</dt>"):]
    musica = label[label.find("credits"):label.find(div_c)]
    musica = musica[musica.find("nb"):musica.find(span_c)]
    musica = musica[musica.find(span):]
    musica = musica[musica.find(">") + 1:]
    return musica

def fotografia(html):
    label = html[html.find("<dt>Fotografía</dt>"):]
    foto = label[label.find("credits"):label.find(div_c)]
    foto = foto[foto.find("nb"):foto.find(span_c)]
    foto = foto[foto.find(span):]
    foto = foto[foto.find(">") + 1:]
    return foto

def reparto(html):
    label = html[html.find("<dt>Reparto</dt>"):]
    reparto = label[label.find("card-cast"):label.find(dd_c)]
    reparto = reparto[reparto.find("credits"):reparto.find(div_c)]
    reparto = reparto[reparto.find("nb"):reparto.find(span_c)]

def sinopsis(html):
    label = html[html.find("<dt>Sinopsis</dt>"):]
    sinopsis = label[label.find("description"):label.find(dd_c)]
    sinopsis = sinopsis[sinopsis.find(">") + 1:]
    return sinopsis


diccionario["titulo_original"] = titulo_original(html)
diccionario["año"] = anyo(html)
diccionario["duracion"] = duracion(html)
diccionario["pais"] = pais(html)
diccionario["direccion"] = direccion(html)
diccionario["guion"] = guion(html)
diccionario["musica"] = musica(html)
diccionario["fotografia"] = fotografia(html)
# diccionario["reparto"] = reparto(html)
# diccionario["productora"] = productora(html)
# diccionario["genero"] = genero(html)
diccionario["sinopsis"] = sinopsis(html)

print(diccionario)