# TPfinal
## Coderhouse - Python - Comisión 23850
Gustavo Garcia Mazzetti, Gustavo Lizarraga, Francisco Vasta

La idea de este proyecto es crear un sitio web que sirva a una empresa como intranet en donde no solo los empleados puedan encontrarse y conectar, sino también ver puestos vacantes en otros sectores y postularse para los mismos. La motivación es poder generar un espacio de encuentro y desarrollo personal, en donde el crecimiento de los vínculos internos de la empresa dependa directamente de sus actores principales.
Este sitio fue desarrollado bajo el framework Django para desarrollo web y consta en esta primera instancia de una página de ingreso desde donde se puede realizar el registro de usuarios, cargando para esto sus datos personales y de contacto. Al realizar el registro nos redirige a la intranet desde donde se puede cargar nuevas búsquedas laborales o también completar sus datos para postularse a algún puesto vacante.

### Contenido

Este proyecto consta de una única rama principal donde se encuentra la estructura principal del proyecto y una aplicación llamada “Postulantes”. Dentro de esta se encuentra los archivos que constituyen el sitio web, como serían los templates y los archivos donde se configura la lógica interna.

### Puesta en marcha

Para poder probar este proyecto en tu PC deberás tener en cuenta los siguientes pasos:

- Para correr este sitio hay que tener previamente instalado [Python](https://www.python.org/) y una vez instalado este instalar [Django](https://docs.djangoproject.com/en/4.0/topics/install/). Luego hay que descargar y descomprimir el archivo .zip del proyecto.

- A continuación desde la consola del sistema pararse en la carpeta donde se encuentra el archivo manage.py y ejecutar:
```
python manage.py runserver
```

- Una vez hecho esto, la consola devolverá una url con un valor numérico. Copiar y pegar ésta en el navegador web y añadir a la misma:

```
/Postulante/ingreso
```
¡¡¡Ya debería poder navegar por el sitio web!!!

### Vista previa

Así debería verse la página de inicio del sitio web

![](/TPfinal/ingreso.PNG)
