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

from .. import ApiBase

class Contribuyentes(ApiBase):
    '''
    Módulo que permite gestionar contribuyentes en ContaFi, junto con los
    roles y permisos disponibles.

    :param str api_token:
        Token de autenticación del usuario. Si no se proporciona, se
        intentará obtener de una variable de entorno.

    :param str api_url:
        URL base de la API. Si no se proporciona, se usará una URL por defecto.

    :param str api_version:
        Versión de la API. Si no se proporciona, se usará una versión
        por defecto.

    :param bool api_raise_for_status:
        Si se debe lanzar una excepción automáticamente para respuestas
        de error HTTP. Por defecto es True.
    '''

    def __init__(self):
        super().__init__()

    def estadisticas(self):
        '''
        Recurso que permite obtener la estadística de un contribuyente a
        partir de su RUT.

        :return:
            Respuesta JSON con las estadísticas.

        :rtype:
            dict
        '''
        url = '/contribuyentes/estadisticas'

        response = self.client.get(url)

        return response.json()

    def datos(self, rut):
        '''
        Recurso que permite obtener los datos de un contribuyente a
        partir de su RUT.

        :param str rut:
            RUT del contribuyente a consultar, sin puntos y con DV.

        :return:
            Respuesta JSON con los datos del contribuyente.

        :rtype:
            dict
        '''
        url = '/contribuyentes/%(rut)s' % {'rut': rut}

        response = self.client.get(url)

        return response.json()

    def sucursal(self, sucursal):
        '''
        Recurso que permite obtener los datos de una sucursal de un
        contribuyente a partir de su código.

        :param int sucursal:
            ID de la sucursal a consultar.

        :return:
            Respuesta JSON con los datos de la sucursal.

        :rtype:
            dict
        '''
        url = '/contribuyentes/sucursales/%(sucursal)s' % {
            'sucursal': sucursal
        }

        response = self.client.get(url)

        return response.json()

    def agregarUsuarioAutorizado(self, body):
        '''
        Recurso que permite autorizar un usuario con cierto rol en un
        contribuyente.

        :param dict body:
            Datos como el nombre de usuario y rol a asignar.

        :return:
            Respuesta JSON con la información del usuario autorizado.

        :rtype:
            dict
        '''
        url = '/contribuyentes/usuarios'

        response = self.client.put(url, body)

        return response.json()

    def quitarUsuarioAutorizado(self, usuario, rol):
        '''
        Recurso que permite quitar a un usuario con cierto rol en un
        contribuyente.

        :param str usuario:
            Nombre del usuario a remover.

        :param int rol:
            Rol del usuario.

        :return:
            Respuesta JSON con la información del usuario removido.

        :rtype: dict
        '''
        url = '/contribuyentes/usuarios/%(usuario)s/%(rol)s' % {
            'usuario': usuario,
            'rol': rol
        }

        response = self.client.delete(url)

        return response.json()

    def obtenerRoles(self):
        '''
        Recurso que entrega los roles de un contribuyente.

        :return:
            Respuesta JSON con el detalle de cada rol.

        :rtype:
            dict
        '''
        url = '/contribuyentes/roles'

        response = self.client.get(url)

        return response.json()

    def agregarPermisoRol(self, body):
        '''
        Recurso que permite agregar permisos a un rol.

        :param dict body:
            Datos que incluyen el rol a modificar y sus permisos.

        :return:
            Respuesta JSON con el rol modificado.

        :rtype:
            dict
        '''
        url = '/contribuyentes/roles'

        response = self.client.put(url, body)

        return response.json()

    def quitarPermisoRol(self, idRol, permiso):
        '''
        Recurso que permite quitar un permiso asociado a un rol de un
        contribuyente.

        :param int idRol:
            Identificador único del rol.

        :param str permiso:
            Permiso que se desea remover.

        :return:
            Respuesta JSON con el rol modificado.

        :rtype:
            dict
        '''
        url = '/contribuyentes/roles/%(rol)s/%(permiso)s' % {
            'rol': idRol,
            'permiso': permiso
        }

        response = self.client.delete(url)

        return response.json()
