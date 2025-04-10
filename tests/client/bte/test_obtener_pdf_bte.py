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

"""Unit tests for retrieving the PDF content of an issued BTE."""
import os
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte


class TestObtenerPdfBte(TestCase):

    """
    Test case for retrieving the PDF content of an issued BTE.

    This test verifies that the `pdf()` method from the `Bte` client
    returns a valid PDF file and that it is saved locally.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before executing the test method.

        Initializes:
        - the BTE API client.
        - verbosity setting from `TEST_VERBOSE`.
        - the BTE number to be retrieved, from `TEST_NRO_BTE` if available.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bte()
        cls.numero = getenv('TEST_NRO_BTE', None)

    def test_obtener_pdf_bte(self):
        """
        Test the `pdf()` method for retrieving the PDF content of a BTE.

        If no document number is configured via environment variables,
        the test retrieves the first available BTE from the current or
        configured period.

        The downloaded PDF is saved to `archivos/bte_emitidas_pdf/`
        with the name `CONTAFI_BTE_<numero>.pdf`.

        If `TEST_VERBOSE=1`, the file path is printed.

        :raises AssertionError: If no PDF content is returned.
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

            # Download data for the PDF.
            pdf = self.client.pdf(self.numero)

            # Go back two levels to exit 'client/bte'
            base_dir = os.path.dirname(
                os.path.dirname(os.path.dirname(__file__))
            )

            # Define the correct destination folder
            output_dir = os.path.join(base_dir, 'archivos', 'bte_emitidas_pdf')

            # Create the folder if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Create the file path and name with the following nomenclature:
            # CONTAFI_BTE_123.pdf
            filename = os.path.join(
                output_dir,
                'CONTAFI_BTE_%(numero)s.pdf' % {
                    'numero': self.numero
                }
            )

            # Create the PDF file using the path, name and data.
            with open(filename, 'wb') as f:
                f.write(pdf)

            self.assertIsNotNone(pdf)

            if self.verbose:
                print('\ntest_obtener_pdf_bte() filename: ', filename,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
