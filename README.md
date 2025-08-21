# IChing API

API para consultas del I Ching (Libro de las Mutaciones) construida con FastAPI.

## Características

- Consultas al oráculo con generación aleatoria de hexagramas
- Información completa de los 64 hexagramas
- Documentación automática con Swagger UI
- Preparada para despliegue en producción

## Instalación

1. Clona el repositorio
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la aplicación: `uvicorn app.main:app --reload`

## Uso

Accede a la documentación en: http://localhost:8000/docs

### Endpoints principales

- `GET /` - Página de inicio
- `GET /health` - Verificar estado del servicio
- `GET /api/v1/hexagrams/{number}` - Obtener hexagrama por número
- `POST /api/v1/consult` - Realizar consulta al oráculo

## Despliegue con Docker

1. Construye la imagen: `docker build -t iching-api .`
2. Ejecuta el contenedor: `docker run -p 8000:8000 iching-api`

O usa Docker Compose: `docker-compose up -d`
