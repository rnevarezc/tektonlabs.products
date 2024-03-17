import logging.config
import sys

# Logging configuration
config = {
    "version": 1,
    "formatters": {
        "simple":{
            "format": "%(levelname)s: - %(asctime)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": sys.stdout,
        },
        "file":{
            "level": "DEBUG",
            "class": "logging.FileHandler", 
            "formatter": "simple",
            "filename": "access.log"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console", "file"
        ],
        "propagate": True
    }
}

logging.config.dictConfig(config)