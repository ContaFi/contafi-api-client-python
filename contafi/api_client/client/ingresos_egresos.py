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

class IngresosEgresos(ApiBase):
    '''
    Módulo que permite manejar y listar los movimientos de dinero efectuados.

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

    def listarMovimientos(self, periodo):
        '''
        Recurso que permite obtener el listado paginado de movimientos
        (otros ingresos/egresos) del contribuyente.

        :param str periodo:
            Periodo por el cual consultar los movimientos.

        :return:
            Respuesta JSON con el listado de movimientos efectuados y recibidos.

        :rtype:
            dict
        '''
        url = '/movimientos?periodo=%(periodo)s' % {'periodo': periodo}

        response = self.client.get(url)

        return response.json()
