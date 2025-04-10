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
"""
Run the tests for the ContaFi API client.

This script allows you to run specific tests or all tests in
the test directory.
It also loads environment variables from a test.env file in the
tests directory.

"""
import argparse
import os
import sys
import unittest

from dotenv import load_dotenv

# Modify the directory to include the repository in the Python PATH and
# find the contafi module without having to install it
app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, app_dir)

# Special class for test results
class CustomTestResult(unittest.TextTestResult):

    """
    Custom test result class for enhancing assertion failure reporting.

    Overrides the default `addFailure` behavior in `unittest.TextTestResult`
    to provide additional output for failed assertions.
    """

    def addFailure(self, test, err): # noqa: N802
        """
        Handle assertion failures with custom output formatting.

        If the failure is an `AssertionError`, it writes the test ID and
        error message directly to the output stream, then processes it as
        a standard error for consistent tracking.

        For all other exceptions, the method falls back to the default
        unittest behavior.

        :param test: The test case instance that failed.
        :type test: unittest.TestCase

        :param err: The exception info tuple (type, value, traceback).
        :type err: tuple
        """
        exception_type, value, traceback = err
        if exception_type is AssertionError:
            self.stream.write(f'\nFAIL: {test.id()}\n')
            self.stream.write(f'Assertion Error: {value}\n')
            self.stream.flush()
            self.addError(test, err)

        # Standard handling for other errors
        super().addFailure(test, err)

# Tests directory
tests_dir = os.path.dirname(os.path.abspath(__file__))

# Load environment variables for the tests
if os.path.exists(os.path.join(tests_dir, 'test.env')):
    load_dotenv(os.path.join(tests_dir, 'test.env'), override=True)

# Determine if a specific test was requested or all tests are executed
parser = argparse.ArgumentParser(
    description='Execution of the test cases'
)
parser.add_argument(
    'test_case',
    nargs = '?',
    default = None,
    help = 'Permite indicar un test a ejecutar (ej: "boletas.test_boletas")'
)
args = parser.parse_args()

# Load the requested test or all tests in the tests directory
loader = unittest.TestLoader()
if args.test_case:
    suite = loader.loadTestsFromName(args.test_case)
else:
    suite = loader.discover(tests_dir)

# Execute the tests
runner = unittest.TextTestRunner(failfast=True, resultclass=CustomTestResult)
try:
    runner.run(suite)
except KeyboardInterrupt:
    pass
