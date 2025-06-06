# gunicorn_config.py
workers = 2  # Reduce el número de workers para consumir menos memoria
worker_class = 'gevent'  # Usar workers asíncronos más eficientes
worker_connections = 1000
timeout = 120  # Aumenta el timeout para operaciones largas
keep_alive = 5
threads = 2  # Usar threading para mejor manejo de conexiones
max_requests = 200  # Reciclar workers después de cierto número de requests
max_requests_jitter = 50  # Agregar jitter para evitar reciclar todos a la vez
import os

# Vincular Gunicorn al puerto proporcionado por Railway
bind = f"0.0.0.0:{os.getenv('PORT', '10000')}"
