import logging
from logging.handlers import RotatingFileHandler

# Skapar en logger som används av hela projektet
def setup_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    # Skriver loggar till app.log och roterar filen vid 500 KB
    handler = RotatingFileHandler(
        "app.log",
        maxBytes=500000,
        backupCount=3
    )

    # Bestämmer hur varje loggrad ska se ut
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Förhindrar att flera handlers läggs till av misstag
    if not logger.handlers:
        logger.addHandler(handler)

    return logger
