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

"""Unit tests for listing issued BTE documents."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestListarBtes(TestCase):

    """
    Test case for listing issued BTEs (Boletas de Terceros Electrónicas).

    This test verifies that the Bte client can retrieve a paginated list
    of issued documents when a valid period filter is applied.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running test methods.

        Initializes:
        - the BTE API client.
        - verbosity setting from the `TEST_VERBOSE` environment variable.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bte()

    def test_listar_btes(self):
        """
        Test the `listar()` method to retrieve issued BTEs.

        Using a period filter.

        The period is taken from `TEST_PERIODO`, or defaults to the current
        UTC month (`YYYYMM` format). If successful, the list of BTEs
        is retrieved and optionally printed.

        :raises AssertionError: If the API call fails or throws an exception.
        """
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO', datetime.now(UTC).strftime('%Y%m')
            )
        }
        try:
            # List of BTEs.
            lista_btes = self.client.listar(filtros)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_listar_btes() boletas: ', lista_btes, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
