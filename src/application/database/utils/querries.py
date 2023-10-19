from json import loads
from ..models.base import BaseModel
from typing import Type
from .session import DBSession


def get_all_objects(session: DBSession,
                    model: Type[BaseModel]) -> list[BaseModel]:
    return session.query(model).all()


def save_object_to_db(session: DBSession, model: BaseModel):
    session.add_model(model)
    session.commit_session()


def save_objects_to_db(session: DBSession, models: list[BaseModel]):
    for model in models:
        session.add_model(model)


def get_objects_by_value(session: DBSession, model: Type[BaseModel],
                         field: str, value) -> list[BaseModel] | None:
    object = session.query(model).filter(model.__dict__[field] == value)
    if object:
        return object.all()


def get_object_by_value(session: DBSession,
                        model: Type[BaseModel],
                        field: str, value) -> BaseModel | None:
    object = session.query(model).filter(model.__dict__[field] == value)
    if object:
        return object.one_or_none()


def clear_models(session: DBSession, model: Type[BaseModel]):
    items = get_all_objects(session, model)
    for item in items:
        session.delete_model(item)


def _save_dict_to_db(session: DBSession,
                     model: Type[BaseModel], dict_data: dict[str, dict]):
    clear_models(session, model)
    model_fields = list(model.__dict__.keys())
    model_fields.remove("id")
    for value in dict_data.values():
        filtered_value = {key: value[key]
                          for key in value if key in model_fields}
        item = model(**filtered_value)
        session.add_model(item)
    session.commit_session()


def save_json_to_db(session: DBSession,
                    model: Type[BaseModel], json_data: str):
    dict_data = loads(json_data)
    _save_dict_to_db(session, model, dict_data)
