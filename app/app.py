from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middlewares.jwt_middlewares import JWTMiddlewares
from .api.routes import api_router
from .database import platzi_db
from app.core.api_doc import api_description

app = FastAPI(**api_description)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.add_middleware(JWTMiddlewares)

app.include_router(api_router)


@app.on_event('startup')
async def startup_event():
    platzi_db.connect()


@app.on_event('shutdown')
async def shutdown_event():
    platzi_db.disconnect()
