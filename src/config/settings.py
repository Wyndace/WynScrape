MODE = "DEV"
DATABASE_ENGINE = 'sqlite:///database.db' if MODE == "DEV" else ""
LOG_LEVEL = "DEBUG" if MODE == "DEV" else "NORMAL"
