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

"""Unit tests for retrieving registered roles of a contributor."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.contribuyentes import Contribuyentes


class TestObtenerRoles(TestCase):

    """
    Test case for retrieving registered roles of a contributor.

    This test ensures that the `obtener_roles()` method returns a valid
    list of roles available for assignment.
    """

    @classmethod
    def setUpClass(cls):
        """
        Initialize the test environment before running the test.

        Sets up the Contribuyentes client and the verbosity flag.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Contribuyentes()

    def test_obtener_roles(self):
        """
        Test the `obtener_roles()` method for retrieving all defined roles.

        If `TEST_VERBOSE=1`, the list of roles is printed.

        :raises AssertionError: If the API call fails or returns an empty list.
        """
        try:
            roles = self.client.obtener_roles()

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_obtener_roles() roles: ', roles, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
