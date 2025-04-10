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

"""Unit tests for retrieving contributor statistics."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.contribuyentes import Contribuyentes


class TestObtenerEstadisticas(TestCase):

    """Test case for retrieving contributor statistics."""

    @classmethod
    def setUpClass(cls):
        """
        Prepare the test environment for running statistics queries.

        Initializes:
        - the Contribuyentes API client.
        - verbosity from environment variables.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Contribuyentes()

    def test_obtener_estadisticas(self):
        """
        Test the `estadisticas()` method to retrieve contributor statistics.

        Asserts that valid statistics data is returned.

        If `TEST_VERBOSE=1`, the output is printed.

        :raises AssertionError: If the request fails or response is invalid.
        """
        try:
            estadisticas = self.client.estadisticas()

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_obtener_estadisticas() estadisticas: ',
                    estadisticas,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
