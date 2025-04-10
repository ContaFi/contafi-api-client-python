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

"""Unit tests for issuing a new BTE (Boleta de Terceros Electrónica)."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestEmitirBte(TestCase):

    """
    Test case for issuing a new BTE (Boleta de Terceros Electrónica).

    This test ensures that the `emitir()` method from the `Bte` client
    can correctly submit a document with required header and detail.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before executing test methods.

        Initializes:
        - the BTE API client.
        - verbosity mode based on `TEST_VERBOSE`.
        - the issuer RUT from the environment variable
          `CONTAFI_CONTRIBUYENTE_RUT`.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bte()
        cls.emisor = getenv('CONTAFI_CONTRIBUYENTE_RUT', '')

    def test_emitir_bte(self):
        """
        Test the `emitir()` method by submitting a valid BTE payload.

        Builds a BTE document with:
        - Header information (`FchEmis`, `RUTEmisor`, `RUTRecep`, etc.),
        - Two detail items with amounts.

        If the emission is successful, the test passes.
        If `TEST_VERBOSE=1`, the emitted BTE data is printed.

        :raises AssertionError: If the API call fails or response is invalid.
        """
        fecha_emis = datetime.now(UTC).strftime('%Y-%m-%d')

        datos_bte = {
            'Encabezado': {
                'IdDoc': {
                    'FchEmis' : fecha_emis,
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
            emitir = self.client.emitir(datos_bte)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_emitir_bte() boleta: ', emitir, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
