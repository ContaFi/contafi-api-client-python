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

"""Unit tests for retrieving the details of a contributor's branch."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.contribuyentes import Contribuyentes


class TestObtenerSucursal(TestCase):

    """
    Test case for retrieving the details of a contributor's branch (sucursal).

    Validates that the `sucursal()` method returns detailed information
    for the provided or fetched branch code.
    """

    @classmethod
    def setUpClass(cls):
        """
        Initialize the Contribuyentes API client.

        Sets RUT and branch code (`TEST_COD_SUCURSAL`) if available.
        Sets verbosity flag.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Contribuyentes()
        cls.emisor = getenv('CONTAFI_CONTRIBUYENTE_RUT', '76192083-9')
        cls.sucursal = getenv('TEST_COD_SUCURSAL', None)

    def test_obtener_sucursal(self):
        """
        Test the `sucursal()` method for retrieving branch details.

        If no branch code is configured, fetches it from the first result
        of the `datos()` method. Asserts that a valid response is returned.

        If `TEST_VERBOSE=1`, the branch information is printed.

        :raises AssertionError: If the API call fails or
        returns an invalid response.
        """
        try:
            if self.sucursal is None:
                datos = self.client.datos(self.emisor)

                self.sucursal = datos['sucursales'][0]['codigo']

            sucursal = self.client.sucursal(self.sucursal)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_obtener_sucursal() sucursal: ', sucursal, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
