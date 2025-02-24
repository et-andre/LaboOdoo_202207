from app                        import db
from flask                      import session

from app.dtos.service_dto       import ServiceDTO
from app.mappers.service_mapper import ServiceMapper
from app.models.service         import Service
from app.models.user            import User
from app.services.base_service  import BaseService
from app.models.user_service    import UserService
from app.dtos.user_service_dto  import UserServiceDTO

class ServiceService(BaseService):

    def find_all(self):
        return [ServiceDTO.build_from_entity(service) for service in Service.query.all()]

    def find_one(self, service_id: int):
        return ServiceDTO.build_from_entity(Service.query.filter_by(service_id=service_id).one())

    def find_one_by(self, **kwargs):
        return ServiceDTO.build_from_entity(Service.query.filter_by(**kwargs).one())

    def find_one_user_service(self, user_service_id: int):
        return UserServiceDTO.build_from_entity(UserService.query.filter_by(user_service_id=user_service_id).one())

    def insert(self, data):
        service = Service()
        ServiceMapper.form_to_entity(data, service)
        # FIXME when david is done with users
        user = User.query.filter_by(user_id=1).one()
        service.add_user(user)
        print(service)

        try:
            db.session.add(service)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return self.find_one(service.service_id)

    def update(self, service_id: int, data):
        service = Service.query.filter_by(service_id=service_id).one()

        if service is None:
            return None

        ServiceMapper.form_to_entity(data, service)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return self.find_one(service_id)

    def delete(self, service_id):
        service = Service.query.filter_by(service_id=service_id).one()

        if service is None:
            return None

        try:
            db.session.delete(service)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return service.service_id