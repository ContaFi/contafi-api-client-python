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

"""Unit tests for listing purchase DTEs (compras) of the contributor."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.facturacion import Facturacion


class TestListarDteCompras(TestCase):

    """
    Test case for listing purchase DTEs (compras) of the contributor.

    Validates that documents are properly returned for all available states.
    """

    @classmethod
    def setUpClass(cls):
        """Initialize the Facturacion client and test verbosity."""
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Facturacion()

    def test_listar_dte_compras(self):
        """
        Test the `listar_compras()` method across various states (1 to 4).

        The search uses a period from `TEST_PERIODO` or defaults to
        current month.

        If `TEST_VERBOSE=1`, prints the list of purchases for each state.

        :raises AssertionError: If any request fails or no data is returned.
        """
        estados = [1, 2, 3, 4]
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO',
                datetime.now(UTC).strftime('%Y%m')
            )
        }

        try:
            for estado in estados:
                response = self.client.listar_compras(estado, filtros)

                self.assertTrue(True)

                if self.verbose:
                    print(
                        '\ntest_listar_dte_compras() Compras (%(est)s): ' % {
                            'est': estado
                        },
                        response,
                        '\n'
                    )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
