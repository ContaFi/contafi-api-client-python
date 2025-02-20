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

class Bte(ApiBase):
    '''
    Módulo que permite gestionar BTEs emitidas.

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

    def emitir(self, body):
        '''
        Recurso que permite emitir una BTE.

        :param dict body:
            Datos de la BTE a emitir.

        :return:
            Respuesta JSON con la BTE emitida.

        :rtype:
            dict
        '''
        url = '/bte/emitir'

        response = self.client.post(url, body)

        return response.json()

    def listar(self, filtros = {}):
        '''
        Recurso que permite obtener el listado paginado de boletas de terceros
        electrónicas emitidas.

        :param dict filtros:
            Filtros adicionales (opcional).

        :return:
            Respuesta JSON con el listado de BTEs emitidas.

        :rtype:
            dict
        '''
        url = '/bte/boletas'
        query = {}

        if len(filtros) > 0:
            query_string = urlencode(query)
            url += '?%(query)s' % {'url': url, 'query': query_string}

        response = self.client.get(url)

        return response.json()

    def datos(self, numero):
        '''
        Recurso para obtener los datos de una boleta de terceros electrónica
        emitida.

        :param int numero:
            Número de la BTE a consultar.

        :return:
            Respuesta JSON con los datos de la BTE.

        :rtype:
            dict
        '''
        url = '/bte/boletas/%(numero)s' % {'numero': numero}

        response = self.client.get(url)

        return response.json()

    def html(self, numero):
        '''
        Recurso para obtener el HTML de una boleta de terceros electrónica
        emitida.

        :param int numero:
            Número de la BTE a consultar.

        :return:
            Respuesta con el contenido del HTML de la BTE en bytes.

        :rtype:
            bytes
        '''
        url = '/bte/html/%(numero)s' % {'numero': numero}

        response = self.client.get(url)

        return response.content

    def pdf(self, numero):
        '''
        Recurso para obtener el PDF de una boleta de terceros electrónica
        emitida.

        :param int numero:
            Número de la BTE a consultar.

        :return:
            Respuesta con el contenido del PDF de la BTE en bytes.

        :rtype:
            bytes
        '''
        url = '/bte/pdf/%(numero)s' % {'numero': numero}

        response = self.client.get(url)

        return response.content

    def anular(self, numero, body):
        '''
        Recurso que permite anular una boleta de terceros electrónica
        previamente emitida.

        :param int numero:
            Número de la BTE a anular.

        :param dict body:
            Datos a entregar (causa de anulación).

        :return:
            Respuesta JSON con el contenido la BTE anulada.

        :rtype:
            dict
        '''
        url = '/bte/anular/%(numero)s' % {'numero': numero}

        response = self.client.post(url, body)

        return response.json()

    def calcularMontoLiquido(self, bruto, periodo):
        '''
        Recurso que permite calcular el monto líquido a partir del monto bruto.

        :param int bruto:
            Monto bruto a convertir.

        :param str periodo:
            Periodo a considerar para la conversión.

        :return:
            Respuesta JSON con el valor líquido calculado.

        :rtype:
            dict
        '''
        url = '/bte/liquido/%(bruto)s/%(periodo)s' % {
            'bruto': bruto,
            'periodo': periodo
        }

        response = self.client.get(url)

        return response.json()

    def calcularMontoBruto(self, liquido, periodo):
        '''
        Recurso que permite calcular el monto bruto a partir del monto líquido.

        :param int bruto:
            Monto líquido a convertir.

        :param str periodo:
            Periodo a considerar para la conversión.

        :return:
            Respuesta JSON con el valor bruto calculado.

        :rtype:
            dict
        '''
        url = '/bte/bruto/%(liquido)s/%(periodo)s' % {
            'liquido': liquido,
            'periodo': periodo
        }

        response = self.client.get(url)

        return response.json()

    def listarReceptores(self):
        '''
        Recurso que permite obtener el listado paginado de receptores
        asociados a las BTE.

        :return:
            Respuesta JSON con los receptores asociados a las BTE.

        :rtype:
            dict
        '''
        url = '/bte/receptores'

        response = self.client.get(url)

        return response.json()
