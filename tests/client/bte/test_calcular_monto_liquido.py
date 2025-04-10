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

"""Unit tests for calculating the net amount from a gross amount."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestCalcularMontoLiquido(TestCase):

    """
    Test case for calculating the net amount (monto líquido).

    This test ensures that the BTE API correctly calculates the net
    value when given a gross amount and a valid period.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before executing test methods.

        Initializes:
        - the BTE API client.
        - verbosity setting from the `TEST_VERBOSE` environment variable.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bte()

    def test_calcular_monto_liquido(self):
        """
        Test the `calcular_monto_liquido()` method using a fixed gross amount.

        Uses a default gross amount of 10,000 and the current period
        (or value from `TEST_PERIODO`) to calculate the net amount.

        If `TEST_VERBOSE=1`, the calculated amount is printed.

        :raises AssertionError: If the API call fails or response is invalid.
        """
        bruto = 10000
        periodo = getenv('TEST_PERIODO', datetime.now(UTC).strftime('%Y%m'))

        try:
            monto_liquido = self.client.calcular_monto_liquido(bruto, periodo)

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_calcular_monto_liquido() monto liquido: ',
                    monto_liquido,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
