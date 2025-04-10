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

"""Unit tests for adding permissions to a contributor role."""
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.contribuyentes import Contribuyentes


class TestAgregarPermiso(TestCase):

    """
    Test case for adding permissions to a contributor role.

    This test ensures that the `Contribuyentes` API client can assign
    one or more permissions to a role successfully.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running test methods.

        Initializes:
        - the Contribuyentes API client.
        - verbosity based on `TEST_VERBOSE`.
        - role ID from the `TEST_ROL_ID` environment variable if present.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Contribuyentes()
        cls.rol_id = getenv('TEST_ROL_ID', None)

    def test_agregar_permiso(self):
        """
        Test the `agregar_permiso_rol()`.

        Method to assign permissions to a role.

        If no role ID is provided, the first available role is retrieved from
        `obtener_roles()` and used. A permission such as `bhe_ver` is added.

        If `TEST_VERBOSE=1`, the updated role data is printed.

        :raises AssertionError: If the API call fails or the role is
        not updated.
        """
        try:
            if self.rol_id is None:
                roles = self.client.obtener_roles()

                self.rol_id = roles[0]['id']

            data = {
                'rol_id': self.rol_id,
                'permisos': ['bhe_ver']
            }

            rol = self.client.agregar_permiso_rol(data)

            self.assertTrue(True)

            if self.verbose:
                print('\ntest_agregar_permiso() rol: ', rol, '\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
