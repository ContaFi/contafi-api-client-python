#
# ContaFi: Cliente de API en Python.
# Copyright (C) ContaFi <https://www.contafi.cl>
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo
# bajo los términos de la GNU Lesser General Public License (LGPL) publicada
# por la Fundación para el Software Libre, ya sea la versión 3 de la Licencia,
# o (a su elección) cualquier versión posterior de la misma.
#
# Este programa se distribuye con la esperanza de que sea útil, pero SIN
# GARANTÍA ALGUNA; ni siquiera la garantía implícita MERCANTIL o de APTITUD
# PARA UN PROPÓSITO DETERMINADO. Consulte los detalles de la GNU Lesser General
# Public License (LGPL) para obtener una información más detallada.
#
# Debería haber recibido una copia de la GNU Lesser General Public License
# (LGPL) junto a este programa. En caso contrario, consulte
# <http://www.gnu.org/licenses/lgpl.html>.
#

from .. import ApiBase
from urllib.parse import urlencode

class Bhe(ApiBase):
    '''
    Módulo que permite gestionar BHEs recibidas.

    :param str api_token:
        Token de autenticación del usuario. Si no se proporciona, se
        intentará obtener de una variable de entorno.

    :param str api_url:
        URL base de la API. Si no se proporciona, se usará una URL por defecto.

    :param str api_version:
        Versión de la API. Si no se proporciona, se usará una versión
        por defecto.

    :param bool api_raise_for_status:
        Si se debe lanzar una excepción automáticamente para respuestas
        de error HTTP. Por defecto es True.
    '''

    def __init__(self):
        super().__init__()

    def listar(self, filtros = {}):
        '''
        Recurso que permite obtener el listado paginado de boletas de
        honorarios electrónicas recibidas.

        :param dict filtros:
            Filtros de búsqueda.

        :return:
            Respuesta JSON con el listado de boletas emitidas.

        :rtype:
            dict
        '''
        url = '/bhe/boletas'
        query = {}

        if len(filtros) > 0:
            query_string = urlencode(query)
            url += '?%(query)s' % {'url': url, 'query': query_string}

        response = self.client.get(url)

        return response.json()

    def datos(self, emisor, numero):
        '''
        Recurso para obtener los datos de una boleta de honorarios
        electrónica recibida.

        :param string emisor:
            RUT del emisor de la BHE, sin puntos y con DV.

        :param int numero:
            Número de la BHE.

        :return:
            Respuesta JSON con los datos de la BHE consultada.

        :rtype:
            dict
        '''
        url = '/bhe/boletas/%(emisor)s/%(numero)s' % {
            'emisor': emisor, 'numero': numero
        }

        response = self.client.get(url)

        return response.json()

    def pdf(self, emisor, numero, filtros = {}):
        '''
        Recurso para obtener el PDF de una boleta de honorarios
        electrónica recibida.

        :param string emisor:
            RUT del emisor de la BHE, sin puntos y con DV.

        :param int numero:
            Número de la BHE.

        :param dict filtros:
            Filtros adicionales (opcional).

        :return:
            Respuesta JSON con los datos del PDF de la BHE consultada

        :rtype:
            bytes
        '''
        url = '/bhe/pdf/%(emisor)s/%(numero)s' % {
            'emisor': emisor, 'numero': numero
        }
        query = {}

        if len(filtros) > 0:
            query_string = urlencode(query)
            url += '?%(query)s' % {'url': url, 'query': query_string}

        response = self.client.get(url)

        return response.content

    def observar(self, emisor, numero, body):
        '''
        Recurso que permite observar una boleta de honorarios electrónica
        previamente recibida.

        :param string emisor:
            RUT del emisor de la BHE, sin puntos y con DV.

        :param int numero:
            Número de la BHE.

        :param dict body:
            Datos de la observación de la BHE (causa).

        :return:
            Respuesta JSON con la BHE observada

        :rtype:
            dict
        '''
        url = '/bhe/observar/%(emisor)s/%(numero)s' % {
            'emisor': emisor, 'numero': numero
        }

        response = self.client.post(url, body)

        return response.json()

    def listarEmisores(self, nuevos):
        '''
        Recurso que permite obtener el listado paginado de emisores asociados
        a las BHE.

        :param string nuevos:
            Emisores que ha emitido por primera vez una BHE en el
            período indicado.

        :return:
            Respuesta JSON con el listado de emisores.

        :rtype:
            dict
        '''
        url = '/bhe/emisores?nuevos=%(nuevos)s' % {
            'nuevos': nuevos
        }

        response = self.client.get(url)

        return response.json()
