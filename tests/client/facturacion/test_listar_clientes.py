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
from contafi.api_client import ApiException
from contafi.api_client.client.facturacion import Facturacion

class TestListarClientes(TestCase):
    '''
    Clase de pruebas para listar clientes de ventas efectuadas.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Facturacion()

    def testListarClientes(self):
        '''
        Método de test para probar el recurso de listar clientes de ventas
        ya efectuadas por el contribuyente.
        '''

        try:
            listaClientes = self.client.listarClientes()

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntestListarClientes() Clientes: ',
                    listaClientes,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})