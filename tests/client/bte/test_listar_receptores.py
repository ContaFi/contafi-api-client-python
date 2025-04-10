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

"""Unit tests for listing BTE receivers."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestListarReceptores(TestCase):

    """
    Test case for listing receivers of issued BTEs.

    This test ensures that the `listar_receptores()` method from the
    `Bte` client successfully retrieves the list of associated receivers.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running the test.

        Initializes:
        - the BTE API client.
        - verbosity setting based on the `TEST_VERBOSE` environment variable.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bte()

    def test_listar_receptores(self):
        """
        Test the `listar_receptores()` method for retrieving BTE receivers.

        Verifies that the method executes without errors and retrieves
        a valid list of receivers.

        If `TEST_VERBOSE=1`, the result is printed to the console.

        :raises AssertionError: If the API call fails or the result is invalid.
        """
        try:
            # List of receivers.
            receptores = self.client.listar_receptores()

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_listar_receptores() receptores: ',
                    receptores,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
