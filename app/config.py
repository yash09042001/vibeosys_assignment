import os
import logging


class Settings:
    # PROJECT SETUP
    PROJECT_NAME = "Product Service"
    PROJECT_VERSION = "0.1.0"
    PROJECT_DESCRIPTION = "Product Service  that manages\
          Product' data."

    envs = os.environ
    DEBUG = False
    if str(envs.get("DEBUG", 0)).lower() in ("true", "1"):
        DEBUG = True
    if DEBUG:
        logging.getLogger("CONFIG").warning("DEBUG MODE IS ON.")

    OPENAPI_URL = None
    if DEBUG:
        OPENAPI_URL = "/openapi.json"

    # DATABASE SETUP

    DB_ROOT_PASSWORD = envs.get("DB_ROOT_PASSWORD")
    DB_NAME = envs.get("DB_NAME")
    DB_USER = envs.get("DB_USER")
    DB_PASSWORD = envs.get("DB_PASSWORD")
    DSN = envs.get("DSN")
