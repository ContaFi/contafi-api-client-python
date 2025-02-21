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

import os
from os import getenv
from unittest import TestCase
from datetime import datetime
from contafi.api_client import ApiException
from contafi.api_client.client.bte import Bte

class TestObtenerPdfBte(TestCase):
    '''
    Clase de pruebas para obtener el detalle del PDF de una BTE emitida.
    '''
    @classmethod
    def setUpClass(cls):
        # Variables base
        cls.verbose = bool(int(getenv('TEST_VERBOSE', 0)))
        cls.client = Bte()
        cls.numero = getenv('TEST_NRO_BTE', None)

    def testObtenerPdfBte(self):
        '''
        Método de test para probar el recurso de obtener datos del PDF de una
        BTE emitida por el contribuyente.
        '''

        filtros = {
            'periodo': getenv('TEST_PERIODO', datetime.now().strftime('%Y%m'))
        }

        try:
            if self.numero is None:
                listaBtes = self.client.listar(filtros)
                listaFiltrada = listaBtes['results'][0]

                self.numero = listaFiltrada['numero']

            # Descarga de datos para el PDF.
            pdf = self.client.pdf(self.numero)

            # Retrocede dos niveles para salir de 'client/bte'
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

            # Define la carpeta de destino correcta
            output_dir = os.path.join(base_dir, 'archivos', 'bte_emitidas_pdf')

            # Crear la carpeta si no existe
            os.makedirs(output_dir, exist_ok=True)

            # Creación del la ruta generada y nombre del archivo con la siguiente
            # nomenclatura:
            # CONTAFI_BTE_123.pdf
            filename = os.path.join(
                output_dir,
                'CONTAFI_BTE_%(numero)s.pdf' % {
                    'numero': self.numero
                }
            )

            # Creación del archivo PDF usando la ruta, nombre y datos obtenidos.
            with open(filename, 'wb') as f:
                f.write(pdf)

            self.assertIsNotNone(pdf)

            if self.verbose:
                print('\ntestObtenerPdfBte() filename: ', filename,'\n')
        except ApiException as e:
            self.fail('ApiException: %(e)s' % {'e': e})