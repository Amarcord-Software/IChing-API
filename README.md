# IChing-API 🌀

Una API moderna y elegante para consultar el I Ching (Libro de las Mutaciones), construida con FastAPI y Python. Ofrece un oráculo digital que genera hexagramas y sus interpretaciones según la tradición milenaria china.

## Características principales

- **Consultas al oráculo**: Genera hexagramas mediante el método tradicional de monedas
- **64 Hexagramas completos**: Información detallada de todos los hexagramas del I Ching
- **API RESTful**: Interfaz moderna y bien documentada
- **Interpretaciones auténticas**: Textos originales traducidos al español
- **Open Source**: Código abierto para la comunidad espiritual y tecnológica

## Tecnologías utilizadas

- **FastAPI** - Framework moderno y rápido para APIs con Python
- **Python 3.9+** - Lenguaje de programación principal
- **Pydantic** - Validación de datos y settings management
- **Uvicorn** - Servidor ASGI de alto rendimiento
- **Railway** - Plataforma de despliegue y hosting

## Uso rápido

```bash
# Obtener un hexagrama específico
curl https://iching-api.railway.app/api/v1/hexagrams/1

# Consultar al oráculo
curl -X POST https://iching-api.railway.app/api/v1/consult \
  -H "Content-Type: application/json" \
  -d '{"question":"¿Cuál es mi camino?"}'
```
# IChing-API
