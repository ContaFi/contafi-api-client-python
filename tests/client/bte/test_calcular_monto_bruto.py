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
from contafi.api_client.client.bte import Bte

class TestCalcularMontoBruto(TestCase):
    '''
    Clase de pruebas para calcular el monto bruto.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Bte()

    def testCalcularMontoBruto(self):
        '''
        Método de test para probar el recurso de calcular el monto bruto a
        partir de un monto líquido.
        '''
        liquido = 10000
        periodo = getenv('TEST_PERIODO', datetime.now().strftime('%Y%m'))

        try:
            montoBruto = self.client.calcularMontoBruto(liquido, periodo)

            self.assertTrue(True)

            if self.verbose:
                print('\ntestCalcularMontoBruto() monto bruto: ', montoBruto, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})