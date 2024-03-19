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
            "level": "INFO",
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
        "level": "INFO",
        "handlers": [
            "console", "file"
        ],
        "propagate": True
    }
}

logging.config.dictConfig(config)