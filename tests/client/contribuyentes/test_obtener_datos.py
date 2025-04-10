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

"""Unit tests for retrieving detailed information about a contributor."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.contribuyentes import Contribuyentes


class TestObtenerDatos(TestCase):

    """Test case for retrieving detailed information about a contributor."""

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running the test.

        Initializes:
        - the Contribuyentes API client.
        - verbosity setting.
        - contributor RUT from `CONTAFI_CONTRIBUYENTE_RUT` or a fallback.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Contribuyentes()
        cls.rut = getenv('CONTAFI_CONTRIBUYENTE_RUT', '76192083-9')

    def test_obtener_datos(self):
        """
        Test the `datos()` method for retrieving data for a specific RUT.

        Validates that a valid contributor response is returned.

        If `TEST_VERBOSE=1`, the data is printed.

        :raises AssertionError: If the contributor data is not
        found or an error occurs.
        """
        try:
            datos = self.client.datos(self.rut)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_obtener_datos() datos: ', datos, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
