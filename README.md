# TPfinal
## Coderhouse - Python - Comisión 23850
Gustavo Garcia Mazzetti, Gustavo Lizarraga, Francisco Vasta

La idea de este proyecto es crear un sitio web que sirva a una empresa como intranet en donde no solo los empleados puedan encontrarse y conectar, sino también ver puestos vacantes en otros sectores y postularse para los mismos. La motivación es poder generar un espacio de encuentro y desarrollo personal, en donde el crecimiento de los vínculos internos de la empresa dependa directamente de sus actores principales.
Este sitio fue desarrollado bajo el framework Django para desarrollo web y consta en esta primera instancia de una página de ingreso desde donde se puede realizar el registro de usuarios, cargando para esto sus datos personales y de contacto. Al realizar el registro nos redirige a la intranet desde donde se puede cargar nuevas búsquedas laborales o también completar sus datos para postularse a algún puesto vacante.

La programación del proyecto, se realizó de la siguiente manera:

Francisco Vasta:  
      - Aplicación Requeridos: CRUD de puestos requeridos con visualización de lista y detalle de éstos con los postulantes correspondientes.
      - Aplicación Postulantes: CRUD de postulantes con conexión a puesto requerido, a usuario y a Avatar. Modelo y creación de mensajes y vista de postulaciones particulares del usuario.
      - Aplicación Perfiles: visualización de perfil, carga de Avatar y visualización de mensajes por lista de puesto requerido y detalle.
      - Logout
      
Gustavo Garcia Mazzetti:
      - Aplicación Login: Registro de usuarios, página de ingreso, página de inicio con login requerido. Sección About, con descripción de participantes. CRUD sección Novedades, donde se puede realizar avisos internos.
      - Aplicación Perfiles: Formulario para la edición de usuario, contraseña y mail de la persona.
      - Estética: Corrección y edición de archivo css y html, para pequeños cambios estéticos.
### Contenido

Este proyecto consta de una única rama principal donde se encuentra la estructura principal del proyecto y las aplicaciones, Login, Postulantes, Requeridos, Perfiles y Registro. Cada aplicación está orientada a un conjunto de procesos en particular, los cuales componen la página. El objetivo de esto, es que fuera mas sencillo a la hora de escribir el código, y el mismo quedara ordenada, y agrupado según funciones, y así evitar grandes cantidades de código, en una sola aplicación. En cuanto a la carpeta static, y los archivos que la componen, se utilizó solo una, ya que los cambios en la misma fueron pocos, tales como algunas imágenes y retoques en el archivo style. Por último, dentro de la carpeta que contiene todos los archivos, junto con el readme, se adjuntó el excel con las pruebas que se realizaron. 


### Puesta en marcha

Para poder probar este proyecto en tu PC deberás tener en cuenta los siguientes pasos:

- Para correr este sitio hay que tener previamente instalado [Python](https://www.python.org/) y una vez instalado este instalar [Django](https://docs.djangoproject.com/en/4.0/topics/install/). Luego hay que descargar y descomprimir el archivo .zip del proyecto.

- A continuación desde la consola del sistema pararse en la carpeta donde se encuentra el archivo manage.py y ejecutar:
```
python manage.py runserver
```

- Una vez hecho esto, la consola devolverá una url con un valor numérico. Desde la url, se podrá ingresar directamente a la página.


¡¡¡Ya debería poder navegar por el sitio web!!!

### Vista previa

Así debería verse la página de inicio del sitio web

![Ingreso GGL](https://user-images.githubusercontent.com/94941251/149009867-4747eccc-4a5a-4220-a907-0f665c6f4066.jpg)


Desde esta página de Ingreso, se puede crear un usuario, o loguearse con uno ya existente, para poder navegar en el sitio. Es requisito para poder ingresar al sitio, estar registrado. En el caso que se quiera ir a la página Inicio, sin estar logueado, no se podrá acceder. Es posible acceder a la sección About, para leer sobre GGL SOLUCIONES, sin estar logueado, pero solo permitirá volver a loguearse.
