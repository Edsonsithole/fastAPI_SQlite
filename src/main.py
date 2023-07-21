# from typing import List
import fastapi as _fastapi
# import sqlalchemy.orm as _orm
import services as _services

app = _fastapi.FastAPI()

_services.create_database()