import os


def get_config():
    
    config = {
        "project_name": os.getenv("PROJECT_NAME", "pyforge"),
        "version": os.getenv("VERSION", "0.1.0"),
        "secret_key": os.getenv("SECRET_KEY", None),
        "debug": os.getenv("DEBUG", "False"),
        "database_url": os.getenv("DATABASE_URL", "sqlite:///default.db")

    }

    return config