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

"""Unit tests for observing a received BHE document."""
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bhe import Bhe


class TestObservarBhe(TestCase):

    """
    Test case for observing a received BHE (Boleta de Honorarios Electrónica).

    This test ensures that the `observar()` method from the `Bhe` client
    correctly submits an observation for a received document.
    """

    @classmethod
    def setUpClass(cls):
        """
        Prepare test context before running tests.

        Initializes:
        - the `Bhe` API client.
        - the RUT of the issuer from `TEST_EMISOR`.
        - the BHE document number from `TEST_NRO_BHE`.
        - verbosity from `TEST_VERBOSE`.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bhe()
        cls.emisor = getenv('TEST_EMISOR', '')
        cls.numero = getenv('TEST_NRO_BHE', None)

    def test_observar_bhe(self):
        """
        Test the observation submission endpoint for a received BHE.

        If `TEST_NRO_BHE` and `TEST_EMISOR` are not provided via environment
        variables, the test fetches the first BHE for the given `periodo`
        (from `TEST_PERIODO`) to obtain a valid document to observe.

        It then calls `observar()` with a predefined cause (e.g., cause=1)
        and asserts that the request succeeds.

        If `TEST_VERBOSE=1`, the response is printed to the console.

        :raises AssertionError: If the observation fails or
        raises an exception.
        """
        data = {
            'causa': 1
        }
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO',
                datetime.now(UTC).strftime('%Y%m')
            )
        }

        try:
            if self.numero is None and self.emisor == '':
                lista_bhes = self.client.listar(filtros)
                lista_filtrada = lista_bhes['results'][0]

                emisor_rut = lista_filtrada['emisor']['contribuyente']['rut']
                emisor_dv = lista_filtrada['emisor']['contribuyente']['dv']
                self.numero = lista_filtrada['numero']

                self.emisor = '%(rut)s-%(dv)s' % {
                    'rut': emisor_rut,
                    'dv': emisor_dv
                }

            response = self.client.observar(
                self.emisor,
                self.numero,
                data
            )

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_observar_bhe() Bhe: ', response, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
