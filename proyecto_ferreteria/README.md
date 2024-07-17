

Este proyecto es una aplicación web desarrollada con Django que permite gestionar usuarios, páginas de blogs, productos y clientes. Incluye funcionalidades de autenticación, visualización de listas y detalles de elementos, y gestión de perfiles de usuario.

Demostración: 

    ```bash
    git clone https://github.com/tu-usuario/tu-proyecto.git
    cd tu-proyecto
    ```

2. **Crea y activa un entorno virtual**:
    ```bash
    python -m venv env
    source env/bin/activate  
    ```

3. 
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la base de datos**:
    - Asegúrate de tener una base de datos configurada en `settings.py`. Este proyecto usa SQLite por defecto.

5.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Crea un superusuario** para acceder al panel de administración:
    ```bash
    python manage.py createsuperuser
    ```

7. **Inicia el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```

8. **Accede a la aplicación** en tu navegador en `http://localhost:8000`.

## Estructura del Proyecto

- **accounts**: Gestión de usuarios (registro, inicio de sesión, perfil).
- **about**: Página "Acerca de mí".
- **pages**: Gestión de páginas de blogs.
- **productos**: Gestión de productos.
- **clientes**: Gestión de clientes.

## Detalles de las Aplicaciones

### Aplicación `accounts`

- **Funcionalidades**:
  - Registro de usuarios.
  - Inicio de sesión.
  - Gestión de perfiles de usuario.

- **URLs**:
  - `/signup/`: Registro de usuarios.
  - `/login/`: Inicio de sesión.
  - `/profile/`: Gestión de perfil.

### Aplicación `about`

- **Funcionalidades**:
  - Página "Acerca de mí".

- **URLs**:
  - `/about/`: Página "Acerca de mí".

### Aplicación `pages`

- **Funcionalidades**:
  - Lista de blogs.
  - Detalles de cada blog.

- **URLs**:
  - `/pages/`: Lista de blogs.
  - `/pages/<int:page_id>/`: Detalles de cada blog.

### Aplicación `productos`

- **Funcionalidades**:
  - Lista de productos.
  - Detalles de cada producto.

- **URLs**:
  - `/productos/`: Lista de productos.
  - `/productos/<int:product_id>/`: Detalles de cada producto.

### Aplicación `clientes`

- **Funcionalidades**:
  - Lista de clientes.
  - Detalles de cada cliente.

- **URLs**:
  - `/clientes/`: Lista de clientes.
  - `/clientes/<int:client_id>/`: Detalles de cada cliente.

## Contacto

Si tienes alguna pregunta o sugerencia, por favor contacta a [alex-el-10@hotmail.com]

¡Gracias por utilizar este proyecto!


