from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import Session, sessionmaker

from ....config import settings
from ..models.base import BaseModel


class DBSession(object):

    _session: Session

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBSession, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        engine = create_engine(settings.DATABASE_ENGINE)
        BaseModel.metadata.create_all(engine)  # type: ignore
        self._session = sessionmaker(bind=engine)()

    def query(self, *entities, **kwargs):
        return self._session.query(*entities, **kwargs)

    def add_model(self, model: BaseModel, need_flush: bool = False):
        self._session.add(model)

        if need_flush:
            self._session.flush([model])

    def delete_model(self, model: BaseModel):
        if model is None:
            print(f'{__name__}: model is None')

        try:
            self._session.delete(model)
        except IntegrityError as e:
            print(f'`{__name__}` {e}')
        except DataError as e:
            print(f'`{__name__}` {e}')

    def commit_session(self, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            print(f'`{__name__}` {e}')
            raise
        except DataError as e:
            print(f'`{__name__}` {e}')
            raise

        if need_close:
            self.close_session()

    def close_session(self):
        try:
            self._session.close()
        except IntegrityError as e:
            print(f'`{__name__}` {e}')
            raise
        except DataError as e:
            print(f'`{__name__}` {e}')
            raise
