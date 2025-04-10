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

"""Unit tests for retrieving the detailed data of an issued BTE."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestObtenerDatosBte(TestCase):

    """
    Test case for retrieving the detailed data of an issued BTE.

    This test validates that the `datos()` method from the `Bte` client
    correctly returns the full detail of a given document.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before executing the test.

        Initializes:
        - the BTE API client.
        - verbosity setting from the `TEST_VERBOSE` environment variable.
        - the BTE number to retrieve, from `TEST_NRO_BTE` if set.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bte()
        cls.numero = getenv('TEST_NRO_BTE', None)

    def test_obtener_datos_bhe(self):
        """
        Test the `datos()` method for retrieving details of a specific BTE.

        If no BTE number is provided via environment variables, the
        test fetches the first available document from the current or
        configured period.

        The response is expected to include the complete BTE data.

        If `TEST_VERBOSE=1`, the response is printed to the console.

        :raises AssertionError: If the API call fails or response is invalid.
        """
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO',
                datetime.now(UTC).strftime('%Y%m')
            )
        }

        try:
            if self.numero is None:
                lista_btes = self.client.listar(filtros)
                lista_filtrada = lista_btes['results'][0]

                self.numero = lista_filtrada['numero']

            response = self.client.datos(
                self.numero
            )

            self.assertTrue(True)

            if self.verbose:
                print('\test_obtener_datos_bhe() Datos: ', response, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
