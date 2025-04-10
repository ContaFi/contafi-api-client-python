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

"""Unit tests for retrieving the PDF file of a BHE."""
import os
from datetime import UTC, datetime
from os import getenv
from unittest import TestCase

from contafi.api_client import ApiException
from contafi.api_client.client.bhe import Bhe


class TestObtenerPdfBhe(TestCase):

    """
    Test case for retrieving the PDF data of a received BHE.

    This test ensures that the `pdf()` method from the `Bhe` client
    successfully returns a PDF file for a valid document, and that the
    file is saved locally using a standardized naming convention.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment before running the tests.

        Initializes:
        - a `Bhe` API client instance.
        - the document number (`TEST_NRO_BHE`) and issuer RUT (`TEST_EMISOR`)
        from environment variables.
        - the verbosity flag from `TEST_VERBOSE`.
        """
        # Base variables.
        cls.verbose = bool(int(getenv('TEST_VERBOSE', "0")))
        cls.client = Bhe()
        cls.emisor = getenv('TEST_EMISOR', '')
        cls.numero = getenv('TEST_NRO_BHE', None)

    def test_obtener_pdf_bhe(self):
        """
        Test the PDF retrieval and export process for a received BHE.

        If no issuer or document number is provided, the test fetches the
        first BHE from the current period (from `TEST_PERIODO`) to use it
        as input for the `pdf()` method.

        The returned PDF is written to a file in the
        `archivos/bhe_recibidas_pdf/` directory using the naming pattern:
        `CONTAFI_<emisor>_<numero>.pdf`.

        The test asserts that a valid binary PDF is returned.

        If `TEST_VERBOSE=1`, the output path is printed to the console.

        :raises AssertionError: If the API call fails or no PDF is returned.
        """
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

            # Download data for the PDF.
            pdf = self.client.pdf(self.emisor, self.numero)

            # Go back two levels to exit 'client/bhe'
            base_dir = os.path.dirname(
                os.path.dirname(os.path.dirname(__file__))
            )

            # Define the correct destination folder
            output_dir = os.path.join(
                base_dir,
                'archivos',
                'bhe_recibidas_pdf'
            )

            # Create the folder if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Create the file path and name with the following nomenclature:
            # CONTAFI_12345678-9_123.pdf
            filename = os.path.join(
                output_dir,
                'CONTAFI_%(emisor)s_%(numero)s.pdf' % {
                    'emisor': self.emisor,
                    'numero': self.numero
                }
            )

            # Create the PDF file using the path, name and data.
            with open(filename, 'wb') as f:
                f.write(pdf)

            self.assertIsNotNone(pdf)

            if self.verbose:
                print('\ntest_obtener_pdf_bhe() filename: ', filename,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})
