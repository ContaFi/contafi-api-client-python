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

"""Unit tests for listing BHE emitters."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bhe import Bhe


class TestListarEmisores(TestCase):

    """
    Test case for listing BHE issuers (emitted by third parties).

    This test verifies that the `listar_emisores()` method of the `Bhe` client
    returns a valid list of issuers associated with received BHEs.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running tests.

        Initializes the `Bhe` client and enables verbose logging if
        `TEST_VERBOSE=1` is set in the environment.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bhe()

    def test_listar_emisores(self):
        """
        Test the BHE issuer listing endpoint using a period parameter.

        This test:
        - Uses the `TEST_PERIODO` environment variable, or defaults to the
        current UTC month in `YYYYMM` format.
        - Calls `listar_emisores()` to retrieve issuer data.
        - Asserts that the call succeeds and prints the result if verbose mode
        is enabled.

        :raises AssertionError: If the API call fails or raises an exception.
        """
        nuevos = getenv('TEST_PERIODO', datetime.now(UTC).strftime('%Y%m'))

        try:
            # List of issuers.
            lista_emisores = self.client.listar_emisores(nuevos)

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_listar_emisores() Emisores: ',
                    lista_emisores,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
