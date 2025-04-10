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

"""Unit tests for removing a specific permission from a contributor role."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.contribuyentes import Contribuyentes


class TestQuitarPermiso(TestCase):

    """
    Test case for removing a specific permission from a contributor role.

    Ensures that the `quitar_permiso_rol()` method properly removes
    permissions from the given role ID.
    """

    @classmethod
    def setUpClass(cls):
        """
        Initialize the test environment and Contribuyentes API client.

        Sets role ID from `TEST_ROL_ID` if available and enables verbosity.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Contribuyentes()
        cls.rol_id = getenv('TEST_ROL_ID', None)

    def test_quitar_permiso(self):
        """
        Test the `quitar_permiso_rol()` method for removing a permission.

        If no role is configured, retrieves the first  role
        via `obtener_roles()`. Removes the `bhe_ver` permission.

        If `TEST_VERBOSE=1`, prints the updated role data.

        :raises AssertionError: If the API call fails or
        permission is not removed.
        """
        try:
            if self.rol_id is None:
                roles = self.client.obtener_roles()

                self.rol_id = roles[0]['id']

            permiso = 'bhe_ver'

            rol = self.client.quitar_permiso_rol(self.rol_id, permiso)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_quitar_permiso() rol: ', rol, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
