from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from adapters.configurator.config import settings

engine = create_engine(settings.get_database_uri, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
