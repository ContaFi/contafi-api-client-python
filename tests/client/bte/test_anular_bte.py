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

class TestAnularBte(TestCase):
    '''
    Clase de pruebas para anular una BTE emitida.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Bte()
        cls.numero = getenv('TEST_NRO_BTE', None)

    def testAnularBte(self):
        '''
        Método de test para probar el recurso de anular una BTE emitida
        específica.
        '''

        data = {
            'causa': 3
        }
        filtros = {
            'periodo': getenv('TEST_PERIODO', datetime.now().strftime('%Y%m'))
        }
        try:
            # Listado de BTEs (si numero está definido, se omite el if).
            if self.numero is None:
                listaBhes = self.client.listar(filtros)
                listaFiltrada = listaBhes['results'][0]

                self.numero = listaFiltrada['numero']

            anular = self.client.anular(self.numero, data)

            self.assertTrue(True)

            if self.verbose:
                print('\ntestAnularBte() boleta: ', anular, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})