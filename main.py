from django.apps import apps
from django.conf import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server import django_settings
from server.urls import router

try:
    settings.configure(django_settings)
except RuntimeError:  # Avoid: "Settings already configured."
    pass

apps.populate(settings.INSTALLED_APPS)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
