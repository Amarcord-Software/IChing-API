from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.endpoints import hexagrams, consultation

app = FastAPI(
    title="IChing API",
    description="API para consultas del I Ching (Libro de las Mutaciones)",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(
    hexagrams,
    prefix=settings.API_V1_STR,
    tags=["hexagrams"]
)
app.include_router(
    consultation,
    prefix=settings.API_V1_STR,
    tags=["consultation"]
)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API del I Ching"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}