# CreditApp - Sistema de Gestión de Créditos

CreditApp es un sistema completo de gestión de ventas, inventario y créditos desarrollado con Flask (Python) para pequeñas y medianas empresas. Permite administrar clientes, productos, ventas, créditos, abonos y cajas en una interfaz sencilla y amigable.

## Características Principales

- **Autenticación y Roles**: Niveles de acceso diferenciados para administradores, vendedores y cobradores.
- **Dashboard**: Resumen visual de la actividad del negocio.
- **Gestión de Clientes**: Registro completo de clientes con historial de compras y créditos.
- **Inventario**: Control de productos con alertas de stock bajo.
- **Ventas**: Registro de ventas al contado y a crédito.
- **Créditos y Abonos**: Seguimiento de créditos y registro de pagos parciales.
- **Cajas**: Control de diferentes formas de pago (efectivo, Nequi, Daviplata, etc.).
- **Comisiones**: Cálculo automático de comisiones por ventas y abonos.
- **Reportes**: Exportación en CSV.
- **Facturas**: Generación de PDFs para ventas y abonos, con opción de compartir por WhatsApp.

## Requisitos del Sistema

- Python 3.8 o superior
- PostgreSQL (recomendado para producción) o SQLite (para desarrollo)
- Bibliotecas Python detalladas en requirements.txt

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/Creditapp_railway.git
   cd Creditapp_railway
   ```
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configurar variables de entorno**: crea un archivo `.env` (opcional) o define `SECRET_KEY` y `DATABASE_URL` en tu entorno.
4. **Ejecutar la aplicación** en modo desarrollo:
   ```bash
   python run.py
   ```

## Despliegue en Railway

1. Crea un proyecto en [Railway](https://railway.app) y añade un plugin de PostgreSQL.
2. Copia la URL de la base de datos y configúrala como variable `DATABASE_URL`.
   Railway expone variables como `PGUSER`, `PGPASSWORD`, `PGHOST`, `PGPORT` y `PGDATABASE`.
   Una cadena típica sería:
   `postgresql://${PGUSER}:${PGPASSWORD}@${PGHOST}:${PGPORT}/${PGDATABASE}`.
   También puedes usar `DATABASE_PUBLIC_URL` si tu plugin la expone con ese nombre.
3. Agrega también una `SECRET_KEY` para Flask.
4. Al desplegar, Railway instalará las dependencias indicadas en `requirements.txt` y ejecutará el comando del `Procfile`.

El archivo `railway.json` ya define el comando de inicio con Gunicorn para producción.
