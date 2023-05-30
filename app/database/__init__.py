from ..core import settings
from .database_connection import DatabaseConnection

platzi_db = DatabaseConnection(settings.CONN_DB)
