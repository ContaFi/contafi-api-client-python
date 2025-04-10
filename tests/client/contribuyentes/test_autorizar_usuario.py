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

"""Unit tests for authorizing a user for a contributor with a given role."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.contribuyentes import Contribuyentes


class TestAutorizarUsuario(TestCase):

    """Test case for authorizing a user for a contributor with a given role."""

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before executing the test.

        Initializes:
        - the Contribuyentes API client.
        - verbosity flag from the `TEST_VERBOSE` environment variable.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Contribuyentes()

    def test_autorizar_usuario(self):
        """
        Test the `agregar_usuario_autorizado()`.

        Method for assigning a user to a role.

        Uses the username from `TEST_USUARIO_AUT` and a fixed role ID (1).
        Asserts that the user is successfully authorized.

        If `TEST_VERBOSE=1`, the response is printed.

        :raises AssertionError: If the request fails or user is not authorized.
        """
        data = {
            'usuario_username': getenv('TEST_USUARIO_AUT', 'esteban'),
            'rol_id': 1
        }
        try:
            usuario = self.client.agregar_usuario_autorizado(data)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_autorizar_usuario() usuario: ', usuario, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
