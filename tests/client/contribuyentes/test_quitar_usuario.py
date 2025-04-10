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

"""Unit tests for removing a user's authorization from a contributor."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.contribuyentes import Contribuyentes


class TestQuitarUsuario(TestCase):

    """
    Test case for removing a user's authorization from a contributor.

    This test ensures that the `quitar_usuario_autorizado()` method
    correctly revokes user access from a role.
    """

    @classmethod
    def setUpClass(cls):
        """
        Initialize the test environment and Contribuyentes API client.

        Sets verbosity from the `TEST_VERBOSE` environment variable.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Contribuyentes()

    def test_quitar_usuario(self):
        """
        Test the `quitar_usuario_autorizado()` method for removing user access.

        Retrieves the username from `TEST_USUARIO_AUT` and uses role ID 1
        for removal.

        If `TEST_VERBOSE=1`, prints the response.

        :raises AssertionError: If the user could not be removed.
        """
        usuario = getenv('TEST_USUARIO_AUT', 'esteban')
        rol_id = 1
        try:
            usuario = self.client.quitar_usuario_autorizado(usuario, rol_id)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_quitar_usuario() usuario: ', usuario, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
