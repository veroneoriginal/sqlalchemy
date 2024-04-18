from pathlib import Path
from sqlalchemy.orm import declarative_base

# изолирует от конкретной реализации базы
from sqlalchemy import create_engine

# BASE_DIR будет хранить путь к каталогу, в котором расположен скрипт
# Path(__file__).parent - из пути к текущему скрипту берется только часть,
# соответствующая каталогу, в котором он находится

BASE_DIR = Path(__file__).parent
db_file_path = BASE_DIR / "birds_blog.sqlite3"

DB_URL = f'sqlite:///{db_file_path}'
DB_ECHO = True

engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO
)

Base = declarative_base()