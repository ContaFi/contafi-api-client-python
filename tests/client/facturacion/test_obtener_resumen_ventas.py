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

"""Unit tests for retrieving a sales summary (without detailed items)."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.facturacion import Facturacion


class TestObtenerResumenVentas(TestCase):

    """
    Test case for retrieving a sales summary (without detailed items).

    Validates that the `resumen_ventas_sin_detalle()` method returns
    an aggregated summary of sales for the given period.
    """

    @classmethod
    def setUpClass(cls):
        """Initialize the Facturacion client and configure verbosity."""
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Facturacion()

    def test_obtener_resumen_ventas(self):
        """
        Test the `resumen_ventas_sin_detalle()` method for a given period.

        Uses `TEST_PERIODO` or defaults to the current month (`YYYYMM`).

        If `TEST_VERBOSE=1`, the summary is printed.

        :raises AssertionError: If the response is invalid or the call fails.
        """
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO',
                datetime.now(UTC).strftime('%Y%m')
            )
        }

        try:
            response = self.client.resumen_ventas_sin_detalle(filtros)

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_obtener_resumen_ventas() Resumen: ',
                    response,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
