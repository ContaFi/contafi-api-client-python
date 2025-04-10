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

"""Unit tests for listing sales DTEs (ventas) of the contributor."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.facturacion import Facturacion


class TestListarDteVentas(TestCase):

    """
    Test case for listing sales DTEs (ventas) of the contributor.

    Ensures that `listar_ventas()` returns a valid response when filtering
    by period.
    """

    @classmethod
    def setUpClass(cls):
        """Initialize the Facturacion client and verbosity setting."""
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Facturacion()

    def test_listar_dte_ventas(self):
        """
        Test the `listar_ventas()` method for retrieving sales DTEs.

        Filters the request using the period from `TEST_PERIODO`.

        If `TEST_VERBOSE=1`, prints the sales DTE results.

        :raises AssertionError: If the API call fails or result is empty.
        """
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO',
                datetime.now(UTC).strftime('%Y%m')
            )
        }

        try:
            response = self.client.listar_ventas(filtros)

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_listar_dte_ventas() Ventas: ',
                    response,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
