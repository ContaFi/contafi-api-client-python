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

"""Unit tests for retrieving BHE document details."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bhe import Bhe


class TestObtenerDatosBhe(TestCase):

    """
    Test case for retrieving the details of a received BHE.

    This test validates that the `datos()` method from the `Bhe` client
    returns detailed information about a given BHE issued to the taxpayer.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running the tests.

        Initializes:
        - a `Bhe` API client,
        - the issuer RUT from the `TEST_EMISOR` environment variable,
        - the BHE number from `TEST_NRO_BHE`,
        - and enables verbose output if `TEST_VERBOSE=1`.
        """
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bhe()
        cls.emisor = getenv('TEST_EMISOR', '')
        cls.numero = getenv('TEST_NRO_BHE', None)

    def test_obtener_datos_bhe(self):
        """
        Test the endpoint that returns detailed data for a specific BHE.

        If the document number or issuer is not provided via environment
        variables, the method fetches a list of BHEs for the given period
        (from `TEST_PERIODO`) and selects the first one available.

        Then it calls the `datos()` method using the selected issuer and
        document number, and asserts that the API response is valid.

        If `TEST_VERBOSE=1`, the full response is printed to stdout.

        :raises AssertionError: If the API call fails or throws an exception.
        """
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO',
                datetime.now(UTC).strftime('%Y%m')
            )
        }

        try:
            if self.numero is None and self.emisor == '':
                lista_bhes = self.client.listar(filtros)
                lista_filtrada = lista_bhes['results'][0]

                emisor_rut = lista_filtrada['emisor']['contribuyente']['rut']
                emisor_dv = lista_filtrada['emisor']['contribuyente']['dv']
                self.numero = lista_filtrada['numero']

                self.emisor = '%(rut)s-%(dv)s' % {
                    'rut': emisor_rut,
                    'dv': emisor_dv
                }

            response = self.client.datos(
                self.emisor,
                self.numero
            )

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_obtener_datos_bhe() Datos: ', response, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
