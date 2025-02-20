Pruebas Unitarias
=================

Las pruebas utilizan un archivo llamado `test.env`, que sirve para definir todas las variables de entorno
necesarias para ejecutar estas pruebas. Las pruebas se crearon para probar los ejemplos vistos previamente
en el capítulo `Ejemplos`.

Estas pruebas utilizan `unittest`, se ejecutan con el archivo `run.py`, y dependiendo de cómo se configure
`test.env`, se pueden omitir ciertas pruebas. Asegúrate de definir `CONTAFI_API_URL`, `CONTAFI_API_TOKEN`
y `CONTAFI_CONTRIBUYENTE_RUT` en `test.env`, o no podrás efectuar las pruebas.

Para ejecutar las pruebas unitarias, debes ejecutar el siguiente código en consola desde la raíz del proyecto:

.. code:: shell

    python3 tests/run.py

Si quieres ejecutar una prueba específica, deberás especificar el nombre y ruta:

.. code:: shell

    python3 tests/run.py client.bte.test_emitir_bhe.TestEmitirBte

Para ejecutar otros ejemplos, debes reemplazar `test_emitir_bte` por el nombre de alguna de las otras pruebas descritas posteriormente. Además, si quieres ejecutar un test dentro de otra carpeta, como por ejemplo en `bhe`, deberás ejecutar el siguiente comando:

.. code:: shell

    python3 tests/run.py client.bte.test_listar_bhes.TestListarBhes
