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

"""Unit tests for listing received BHE documents."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bhe import Bhe


class TestListarBhes(TestCase):

    """
    Test case for listing received BHEs (Boletas de Honorarios Electrónicas).

    This test validates that the `listar()` method of the `Bhe` client
    returns results when using a valid date period as a filter.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test environment before running the test suite.

        Initializes the BHE client and sets verbosity based on the
        `TEST_VERBOSE` environment variable.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bhe()

    def test_listar_bhes(self):
        """
        Test the BHE listing endpoint using a period filter.

        Retrieves the period from the `TEST_PERIODO` environment variable
        (or defaults to the current UTC year-month), calls the `listar()`
        method, and asserts the request succeeds.

        If `TEST_VERBOSE=1`, the output will include the response payload.

        :raises AssertionError: If the API call fails or throws an exception.
        """
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO', datetime.now(UTC).strftime('%Y%m')
            )
        }
        try:
            # List of BHEs.
            lista_bhes = self.client.listar(filtros)
            self.assertTrue(True)

            if self.verbose:
                print('\ntest_listar_bhes() boletas: ', lista_bhes, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
