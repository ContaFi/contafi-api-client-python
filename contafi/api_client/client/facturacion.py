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

class Facturacion(ApiBase):
    '''
    Módulo que permite gestionar proveeedores, compras y ventas con
    facturación (DTE).

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

    def resumenVentasSinDetalle(self, periodo):
        '''
        Recurso que permite obtener el listado paginado de resumenes asociados
        a ventas.

        :param str periodo:
            Periodo donde obtener el listado de resumen de ventas.

        :return:
            Respuesta JSON con el listado paginado de ventas.

        :rtype:
            dict
        '''
        url = '/dte/ventas/resumen?periodo=%(periodo)s' % {'periodo': periodo}

        response = self.client.get(url)

        return response.json()

    def listarVentas(self, filtros = {}):
        '''
        Recurso que permite obtener el listado paginado de documentos
        tributarios electrónicos asociados a ventas

        :param dict filtros:
            Filtros de búsqueda.

        :return:
            Respuesta JSON con el listado paginado de DTEs de ventas,
            con detalle.

        :rtype:
            dict
        '''
        url = '/dte/ventas'

        if len(filtros) > 0:
            query_string = urlencode(filtros)
            url += '?%(query)s' % {'url': url, 'query': query_string}

        response = self.client.get(url)

        return response.json()

    def listarCompras(self, estado, filtros):
        '''
        Recurso que permite obtener el listado paginado de documentos
        tributarios electrónicos asociados a compras.

        :param int estado:
            Estado del documento en el registro de compras.

        :param dict filtros:
            Filtros de búsqueda.

        :return:
            Respuesta JSON con el listado paginado de DTEs de compras, con
            detalle.

        :rtype:
            dict
        '''
        url = '/dte/compras?estado=%(estado)s' % {
            'estado': estado
        }

        if len(filtros) > 0:
            query_string = urlencode(filtros)
            url += '&%(query)s' % {'url': url, 'query': query_string}

        response = self.client.get(url)

        return response.json()

    def listarClientes(self):
        '''
        Recurso que permite obtener el listado paginado de clientes
        asociados a ventas.

        :return:
            Respuesta JSON con el listado de clientes de ventas.

        :rtype:
            dict
        '''
        url = '/dte/clientes'

        response = self.client.get(url)

        return response.json()

    def listarProveedores(self):
        '''
        Recurso que permite obtener el listado paginado de proveedores
        asociados a compras.

        :return:
            Respuesta JSON con el listado de proveedores de compras.

        :rtype:
            dict
        '''
        url = '/dte/proveedores'

        response = self.client.get(url)

        return response.json()
