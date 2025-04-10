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

"""Unit tests for calculating the gross amount from a net amount."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestCalcularMontoBruto(TestCase):

    """
    Test case for calculating the gross amount (monto bruto).

    This test verifies that the BTE API correctly returns the gross
    value when given a net amount and a valid period.
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

    def test_calcular_monto_bruto(self):
        """
        Test the `calcular_monto_bruto()` method using a fixed net amount.

        Uses a default net amount of 10,000 and the current period
        (or value from `TEST_PERIODO`) to calculate the gross amount.

        If `TEST_VERBOSE=1`, the result is printed to the console.

        :raises AssertionError: If the API call fails or returns an error.
        """
        liquido = 10000
        periodo = getenv('TEST_PERIODO', datetime.now(UTC).strftime('%Y%m'))

        try:
            monto_bruto = self.client.calcular_monto_bruto(liquido, periodo)

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_calcular_monto_bruto() monto bruto: ',
                    monto_bruto,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
