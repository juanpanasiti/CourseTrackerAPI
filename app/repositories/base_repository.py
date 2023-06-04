from typing import Generic
from typing import List
from typing import TypeVar

from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from ..database import platzi_db
from ..database.models import BaseModel

ModelType = TypeVar('ModelType', bound=BaseModel)

DEFAULT_FILTER = {'is_deleted': False}


class BaseRepository(Generic[ModelType]):
    def __init__(self, db: Session = platzi_db.session) -> None:
        self.db = db
        self.model = ModelType

    def create(self, new_resource: ModelType) -> None:
        try:
            self.db.add(new_resource)
            self.db.commit()
            self.db.refresh(new_resource)
        except IntegrityError as ie:
            raise ie
        finally:
            self.db.close()

    def get_all(self, limit: int, offset: int, search_filter: dict = None) -> List[ModelType]:
        if search_filter is None:
            search_filter = DEFAULT_FILTER
        else:
            search_filter.update(DEFAULT_FILTER)

        try:
            return self.db.query(self.model).filter_by(**search_filter).offset(offset).limit(limit).all()
        except Exception as ex:
            raise ex
        finally:
            self.db.close()

    def get_one_by_filter(self, search_filter: dict = None) -> ModelType | None:
        if search_filter is None:
            search_filter = DEFAULT_FILTER
        else:
            search_filter.update(DEFAULT_FILTER)

        try:
            return self.db.query(self.model).filter_by(**search_filter).first()
        except NoResultFound as nf:
            print('\033[91m', nf.args, '\033[0m')
            return None
        except Exception as ex:
            raise ex
        finally:
            self.db.close()

    def get_by_id(self, id: int, search_filter: dict = None) -> ModelType:
        if search_filter is None:
            search_filter = DEFAULT_FILTER

        query = self.db.query(self.model).filter_by(id=id, **search_filter)
        try:
            return query.one()
        except NoResultFound as nf:
            print('\033[91m', nf.args, '\033[0m')
            raise nf
        except Exception as ex:
            print('\033[91m', ex.args, '\033[0m')
            raise ex

    # def get_list_by_filter(self, search_filter: dict) -> List[ModelType]:
    #     query = self.db.query(self.model).filter_by(**search_filter)
    #     try:
    #         return query.all()
    #     except Exception as ex:
    #         raise ex
    #     finally:
    #         self.db.close()

    def update(self, resource_id: int, new_data: dict, search_filter: dict = {}) -> ModelType:
        search_filter = {**DEFAULT_FILTER, **search_filter}
        try:
            # Get the resource to update
            resource_db = self.get_by_id(resource_id, search_filter)
            # Update the fields that change (dict)
            for field in new_data.keys():
                setattr(resource_db, field, new_data.get(field))
            # Commit changes
            self.db.commit()
            # Return updated model
            return resource_db
        except NoResultFound as nf:
            print('\033[91m', nf.args, '\033[0m')
            raise nf
        except Exception as ex:
            raise ex

    # def delete(self, id: int) -> None:
    #     try:
    #         resource = self.get_by_id(id)
    #         if resource:
    #             resource.is_deleted = True
    #             self.update(resource)
    #     except Exception as ex:
    #         # TODO: logger critical
    #         raise ex
    #     finally:
    #         self.db.close()
