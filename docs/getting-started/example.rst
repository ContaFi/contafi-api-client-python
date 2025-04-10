Ejemplo
=======

Para utilizar el cliente de API de ContaFi, deberás tener definido el token de API y el RUT del emisor como variables de entorno.

.. seealso::

    Para más información sobre este paso, referirse al la guía en Configuración.

El siguiente es un ejemplo básico de cómo emitir una BTE utilizando el cliente de API.

.. code-block:: python

    # Importaciones del cliente de API de ContaFi.
    from datetime import datetime, UTC
    from contafi.api_client import ApiException
    from contafi.api_client.client.bte import Bte

    # Instancia de cliente.
    client = Bte()
    # RUT del emisor.
    rut_emisor = "12345678-9"
    # Fecha de emisión de BHE.
    fecha_emis = datetime.now().strftime('%Y-%m-%d')

    # Datos de la boleta a ser emitida.
    datos_bte = {
        'Encabezado': {
            'IdDoc': {
                'FchEmis' : fecha_emis,
            },
            'Emisor': {
                'RUTEmisor' : rut_emisor,
            },
            'Receptor': {
                'RUTRecep' : '66666666-6',
                'RznSocRecep' : 'Receptor generico',
                'DirRecep' : 'Santa Cruz',
                'CmnaRecep' : 'Santa Cruz',
            },
        },
        'Detalle': [
            {
                'NmbItem' : 'Prueba integracion ContaFi 1',
                'MontoItem' : 50,
            },
            {
                'NmbItem' : 'Prueba integracion ContaFi 2',
                'MontoItem' : 100,
            }
        ]
    }

    # Respuesta de solicitud HTTP (POST) de emisión de boleta.
    response =  client.emitir(datos_bte)

    # Despliegue del resultado.
    print("\nEMISION BOLETA: \n")
    print("\nEmitir BTE ejemplo: ", response, "\n")

.. seealso::
    Para saber más sobre los parámetros posibles y el cómo consumir las API, referirse a la `documentación de ContaFi. <https://developers.contafi.cl/>`_
