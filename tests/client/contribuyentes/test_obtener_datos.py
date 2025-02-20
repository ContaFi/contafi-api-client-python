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
from contafi.api_client.client.contribuyentes import Contribuyentes

class TestObtenerDatos(TestCase):
    '''
    Clase de pruebas para listar BHEs emitidas.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Contribuyentes()
        cls.rut = getenv('CONTAFI_CONTRIBUYENTE_RUT', '76192083-9')

    def testObtenerEstadisticas(self):
        '''
        Método de test para probar el recurso de listar BHEs recibidas, y
        filtrarlas usando un periodo.
        '''

        try:
            # Listado de BHEs.
            datos = self.client.datos(self.rut)

            self.assertTrue(True)

            if self.verbose:
                print('\ntestObtenerDatos() datos: ', datos, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})