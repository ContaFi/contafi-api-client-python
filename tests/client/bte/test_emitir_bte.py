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

class TestEmitirBte(TestCase):
    '''
    Clase de pruebas para emitir una BTE.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Bte()
        cls.emisor = getenv('CONTAFI_CONTRIBUYENTE_RUT', '')

    def testEmitirBte(self):
        '''
        Método de test para probar el recurso de emitir una BTE.
        '''

        fechaEmis = datetime('%Y-%m-%d')

        datosBte = {
            'Encabezado': {
                'IdDoc': {
                    'FchEmis' : fechaEmis,
                },
                'Emisor': {
                    'RUTEmisor' : self.emisor,
                },
                'Receptor': {
                    'RUTRecep' : '66666666-6',
                    'RznSocRecep' : 'Receptor generico',
                    'DirRecep' : 'Santa Cruz',
                    'CmnaRecep' : 'Santa Cruz',
                },
            },
            'Detalle': [
                {
                    'NmbItem' : 'Prueba integracion ContaFi 1',
                    'MontoItem' : 50,
                },
                {
                    'NmbItem' : 'Prueba integracion ContaFi 2',
                    'MontoItem' : 100,
                }
            ]
        }

        try:
            emitir = self.client.emitir(datosBte)

            self.assertTrue(True)

            if self.verbose:
                print('\ntestEmitirBte() boleta: ', emitir, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})