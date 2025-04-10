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

"""Unit tests for listing remunerations (salaries) of the contributor."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.remuneraciones import Remuneraciones


class TestListarRemuneraciones(TestCase):

    """
    Test case for listing remunerations (salaries) of the contributor.

    This test validates that the `Remuneraciones` API client successfully
    retrieves salary records for the given taxpayer.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running the test method.

        Initializes:
        - the `Remuneraciones` API client.
        - verbosity flag using the `TEST_VERBOSE` environment variable.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Remuneraciones()

    def test_listar_remuneraciones(self):
        """
        Test the `listar_remuneraciones()` method using a given period.

        Uses the `TEST_PERIODO` environment variable or defaults to thecurrent
        UTC month (`YYYYMM`). Verifies that a valid response is returned.

        If `TEST_VERBOSE=1`, the retrieved list of remunerations is printed.

        :raises AssertionError: If the API call fails or returns an
        invalid result.
        """
        periodo = getenv('TEST_PERIODO', datetime.now(UTC).strftime('%Y%m'))

        try:
            remuneraciones = self.client.listar_remuneraciones(periodo)

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\test_listar_remuneraciones() Remuneraciones: ',
                    remuneraciones,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
