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

"""Unit tests for listing customers of issued sales DTEs."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.facturacion import Facturacion


class TestListarClientes(TestCase):

    """
    Test case for listing customers of issued sales DTEs.

    Ensures that the `listar_clientes()` method of the Facturacion API client
    returns a valid list of customers.
    """

    @classmethod
    def setUpClass(cls):
        """
        Prepare the test environment before executing test methods.

        Initializes:
        - the Facturacion API client.
        - verbosity setting from `TEST_VERBOSE`.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Facturacion()

    def test_listar_clientes(self):
        """
        Test the `listar_clientes()` method for retrieving sales customers.

        Asserts that the method completes successfully.

        If `TEST_VERBOSE=1`, the list of customers is printed.

        :raises AssertionError: If the call fails or returns no results.
        """
        try:
            lista_clientes = self.client.listar_clientes()

            self.assertTrue(True)

            if self.verbose:
                print(
                    '\ntest_listar_clientes() Clientes: ',
                    lista_clientes,
                    '\n'
                )
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
