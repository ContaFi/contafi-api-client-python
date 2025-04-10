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

"""Unit tests for retrieving the HTML content of an issued BTE."""
import os
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestObtenerHtmlBte(TestCase):

    """
    Test case for retrieving the HTML content of an issued BTE.

    This test ensures that the `html()` method from the `Bte` client
    returns a valid HTML representation and that it is saved correctly
    to disk.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running the test.

        Initializes:
        - the BTE API client.
        - verbosity setting from the `TEST_VERBOSE` environment variable.
        - the BTE number to retrieve, from `TEST_NRO_BTE` if set.
        """
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bte()
        cls.numero = getenv('TEST_NRO_BTE', None)

    def test_obtener_html_bte(self):
        """
        Test the `html()` method for retrieving HTML content of a BTE.

        If no document number is set, fetches the first available one for
        the specified or current period.

        The HTML content is saved under `archivos/bte_emitidas_html/`
        with a filename formatted as `CONTAFI_BTE_<numero>.html`.

        If `TEST_VERBOSE=1`, the output filename is printed.

        :raises AssertionError: If HTML content is not returned.
        """
        filtros = {
            'periodo': getenv(
                'TEST_PERIODO',
                datetime.now(UTC).strftime('%Y%m')
            )
        }

        try:
            if self.numero is None:
                lista_btes = self.client.listar(filtros)
                lista_filtrada = lista_btes['results'][0]

                self.numero = lista_filtrada['numero']

            # Download data for the HTML.
            html = self.client.html(self.numero)

            # Go back two levels to exit 'client/bte'
            base_dir = os.path.dirname(
                os.path.dirname(os.path.dirname(__file__))
            )

            # Define the correct destination folder
            output_dir = os.path.join(
                base_dir,
                'archivos',
                'bte_emitidas_html'
            )

            # Create the folder if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Create the file path and name with the following nomenclature:
            # CONTAFI_BTE_123.html
            filename = os.path.join(
                output_dir,
                'CONTAFI_BTE_%(numero)s.html' % {
                    'numero': self.numero
                }
            )

            # Create the HTML file using the path, name and data.
            with open(filename, 'wb') as f:
                f.write(html)

            self.assertIsNotNone(html)

            if self.verbose:
                print('\ntest_obtener_html_bte() filename: ', filename,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
