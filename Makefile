all: dist

dist:
	python3 setup.py sdist

upload: dist
	twine upload dist/*

install-dev:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

tests: install-dev
	python tests/run.py

tests-readonly:
	python3 tests/run.py client.bhe.test_listar_bhes.TestListarBhes
	python3 tests/run.py client.bte.test_listar_btes.TestListarBtes
	python3 tests/run.py client.bte.test_calcular_monto_bruto.TestCalcularMontoBruto
	python3 tests/run.py client.bte.test_calcular_monto_liquido.TestCalcularMontoLiquido
	python3 tests/run.py client.contribuyentes.test_obtener_estadisticas.TestObtenerEstadisticas
	python3 tests/run.py client.contribuyentes.test_obtener_datos.TestObtenerDatos
	python3 tests/run.py client.contribuyentes.test_obtener_roles.TestObtenerRoles
	python3 tests/run.py client.facturacion.test_listar_clientes.TestListarClientes
	python3 tests/run.py client.facturacion.test_listar_proveedores.TestListarProveedores
	python3 tests/run.py client.ingresos_egresos.test_listar_movimientos.TestListarMovimientos
	python3 tests/run.py client.remuneraciones.test_listar_remuneraciones.TestListarRemuneraciones

docs:
	sphinx-apidoc -o docs contafi && sphinx-build -b html docs docs/_build/html

clean:
	rm -rf dist bhexpress.egg-info bhexpress/__pycache__ bhexpress/*.pyc
