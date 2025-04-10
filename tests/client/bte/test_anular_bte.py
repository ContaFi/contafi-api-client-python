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

"""Unit tests for annulling an issued BTE document."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestAnularBte(TestCase):

    """
    Test case for canceling an issued BTE (Boleta de Terceros Electrónica).

    This test ensures that the `anular()` method from the `Bte` client
    can successfully cancel an issued BTE when a valid document number
    and reason are provided.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before executing test methods.

        Initializes:
        - the BTE API client.
        - verbosity based on `TEST_VERBOSE` environment variable.
        - the BTE number to cancel, if specified in `TEST_NRO_BTE`.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bte()
        cls.numero = getenv('TEST_NRO_BTE', None)

    def test_anular_bte(self):
        """
        Test the `anular()` method for canceling a specific BTE.

        If `TEST_NRO_BTE` is not defined, the test fetches a list of BTEs
        for the given period (`TEST_PERIODO`) and selects the first one.

        The test then attempts to cancel the selected BTE using `causa = 3`.

        If `TEST_VERBOSE=1`, the result is printed to the console.

        :raises AssertionError: If the API call fails or returns an error.
        """
        data = {
            'causa': 3
        }
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO',
                datetime.now(UTC).strftime('%Y%m')
            )
        }
        try:
            # List of BTEs (if `numero` is defined, the if is skipped).
            if self.numero is None:
                lista_bhes = self.client.listar(filtros)
                lista_filtrada = lista_bhes['results'][0]

                self.numero = lista_filtrada['numero']

            anular = self.client.anular(self.numero, data)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_anular_bte() boleta: ', anular, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
