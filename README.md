# De la barra al código

Blog personal hecho con Django para la entrega final del curso de Python de Coderhouse.

Trabajo de barman y estoy aprendiendo a programar, así que el blog va de eso: lo que voy aprendiendo por el camino. Es la evolución de las pre-entregas del curso. Los posts que en la pre-entrega 2 eran una lista de diccionarios en memoria ahora se guardan en una base de datos, tienen autor e imagen y se gestionan desde la web.

## Tecnologías

- Python 3 (desarrollado con Python 3.14)
- Django 6.0
- SQLite, la base de datos que trae Django por defecto
- Pillow, para los campos de imagen
- python-decouple, para leer la configuración desde un archivo `.env`
- Bootstrap 5 (por CDN) y un poco de CSS propio

## Funcionalidades

- Listado de publicaciones, de la más nueva a la más antigua y con 6 por página, y detalle de cada una.
- Crear, editar y eliminar publicaciones desde la web, no solo desde el admin.
- Imagen de portada opcional. Si un post no tiene, en su lugar se ve un fondo de color.
- Registro, inicio y cierre de sesión.
- Perfil de usuario con avatar y biografía, los dos editables.
- Buscador por título o contenido, que avisa cuando no encuentra nada.
- Rutas protegidas: crear, editar y eliminar posts y editar el perfil piden sesión iniciada (`LoginRequiredMixin` en las vistas basadas en clases y `@login_required` en las de función). Además, solo el autor de un post puede editarlo o eliminarlo; si lo intenta otro usuario, recibe un 403.
- Panel de administración de Django con los posts y los perfiles.

## Instalación

Hace falta Git y Python 3.12 o superior (es lo que pide Django 6.0).

1. Clonar el repositorio y entrar en la carpeta:

   ```bash
   git clone https://github.com/MimixGuy/entrega-final-blog-django.git
   cd entrega-final-blog-django
   ```

2. Crear el entorno virtual y activarlo:

   ```bash
   python -m venv venv
   ```

   - Windows (CMD o PowerShell): `venv\Scripts\activate`
   - Windows con Git Bash: `source venv/Scripts/activate`
   - macOS o Linux: `source venv/bin/activate` (si no existe el comando `python`, usar `python3`)

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crear el archivo `.env` copiando el de ejemplo:

   ```bash
   cp .env.example .env
   ```

   En el CMD de Windows es `copy .env.example .env`. Con los valores del ejemplo el proyecto ya funciona en local. Para usar una clave propia se puede generar una con:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

   y pegarla en `SECRET_KEY`. `DEBUG` tiene que quedar en `True` para desarrollo, porque con `DEBUG=False` Django deja de servir las imágenes subidas.

5. Aplicar las migraciones:

   ```bash
   python manage.py migrate
   ```

6. (Opcional) Crear un superusuario para entrar al panel de administración en `/admin/`:

   ```bash
   python manage.py createsuperuser
   ```

7. Arrancar el servidor:

   ```bash
   python manage.py runserver
   ```

   El blog queda en http://127.0.0.1:8000/

## Cómo probarlo desde cero

El repositorio no incluye `db.sqlite3` ni la carpeta `media/` (están en el `.gitignore`), así que el blog arranca vacío. Para probarlo todo:

1. Entrar en **Crear cuenta** y registrarse. Al terminar, la sesión queda iniciada.
2. Ir a **Escribir un post** y publicar uno con imagen y otro sin imagen.
3. Abrir un post propio: aparecen los botones **Editar** y **Eliminar**.
4. Usar el buscador de la barra con una palabra del título o del contenido, y después con una que no esté en ningún post.
5. Entrar en **Mi perfil**, editarlo y subir un avatar.
6. **Cerrar sesión** e intentar abrir `/posts/nuevo/` o `/usuarios/perfil/`: redirige al login.
7. Crear un segundo usuario e intentar editar un post del primero desde la URL (`/posts/<id>/editar/`): devuelve un 403.

Las imágenes se guardan en `media/posts/` y `media/avatares/`. La carpeta `media/` se crea sola al subir la primera imagen.

## Rutas principales

| Ruta | Qué hace | ¿Pide sesión? |
|------|----------|---------------|
| `/` | Listado de posts | No |
| `/posts/<id>/` | Detalle de un post | No |
| `/buscar/?q=...` | Buscador | No |
| `/posts/nuevo/` | Crear un post | Sí |
| `/posts/<id>/editar/` | Editar un post | Sí, y ser el autor |
| `/posts/<id>/eliminar/` | Eliminar un post | Sí, y ser el autor |
| `/usuarios/registro/` | Crear una cuenta | No |
| `/usuarios/login/` | Iniciar sesión | No |
| `/usuarios/logout/` | Cerrar sesión (solo por POST, desde el botón de la barra) | Sí |
| `/usuarios/perfil/` | Mi perfil y mis posts | Sí |
| `/usuarios/perfil/editar/` | Editar el perfil y el avatar | Sí |
| `/admin/` | Panel de administración | Sí, con un superusuario |

## Estructura del proyecto

```
entrega-final-blog-django/
├── proyecto_blog/   # configuración del proyecto (settings.py, urls.py)
├── blog/            # app de los posts: modelo, formulario, vistas, urls y plantillas
├── usuarios/        # app de registro, login, logout y perfil
├── templates/       # base.html, el formulario reutilizable y la página 403
├── static/css/      # estilos propios
├── .env.example     # variables de entorno que necesita el proyecto
├── manage.py
└── requirements.txt
```

## Autor

**Adrian Burai**, barman y estudiante de programación.

GitHub: [MimixGuy](https://github.com/MimixGuy)
