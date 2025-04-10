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

"""Unit tests for listing money movements (incomes and expenses)."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.ingresos_egresos import IngresosEgresos


class TestListarMovimientos(TestCase):

    """
    Test case for listing money movements (incomes and expenses).

    This test ensures that the `IngresosEgresos` API client can retrieve
    transactions for the contributor based on the selected period.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before executing test methods.

        Initializes:
        - the `IngresosEgresos` API client.
        - verbosity setting from the `TEST_VERBOSE` environment variable.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = IngresosEgresos()

    def test_listar_movimientos(self):
        """
        Test the `listar_movimientos()` method for listing financial movements.

        Fetches movements for a given period taken from `TEST_PERIODO`
        or defaults to the current UTC period (`YYYYMM` format).

        If `TEST_VERBOSE=1`, the retrieved data is printed to the console.

        :raises AssertionError: If the API call fails or
        returns an invalid response.
        """
        periodo = getenv('TEST_PERIODO', datetime.now(UTC).strftime('%Y%m'))


        try:
            ingresos_egresos = self.client.listar_movimientos(periodo)

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_listar_movimientos() Ingresos Egresos: ',
                    ingresos_egresos,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
