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

from os import getenv
from unittest import TestCase
from datetime import datetime
from contafi.api_client import ApiException
from contafi.api_client.client.facturacion import Facturacion

class TestListarDteCompras(TestCase):
    '''
    Clase de pruebas para listar DTEs de compras del contribuyente.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Facturacion()

    def testListarDteCompras(self):
        '''
        Método de test para probar el recurso de listar DTEs de compras
        del contribuyente.
        '''

        estados = [1, 2, 3, 4]
        filtros = {
            'periodo': getenv('TEST_PERIODO', datetime.now().strftime('%Y%m'))
        }

        try:
            for estado in estados:
                response = self.client.listarCompras(estado, filtros)

                self.assertTrue(True)

                if self.verbose:
                    print(
                        '\ntestListarDteCompras() Compras (%(est)s): ' % {
                            'est': estado
                        },
                        response,
                        '\n'
                    )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})