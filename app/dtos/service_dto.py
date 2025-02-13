from app.dtos.abstract_dto import AbstractDTO
from app.dtos.service_type_dto import ServiceTypeDTO
from app.models.service import Service


class ServiceDTO(AbstractDTO):
    def __init__(self):
        self.service_id = None
        self.name = None
        self.description = None
        self.request = None
        self.service_type = None
        self.type = None
        self.users = []

    @staticmethod
    def build_from_entity(service: Service):
        service_dto = ServiceDTO()

        service_dto.service_id = service.service_id
        service_dto.name = service.name
        service_dto.description = service.description
        service_dto.request = service.request
        service_dto.type = ServiceTypeDTO.build_from_entity(service.type)
        service_dto.users = []
        # FIXME when david is done with user DTO
        # for user in service.users:
        #     service_dto.users.append(UserDTO.build_from_entity(user))
        return service_dto

    def get_json_parsable(self):
        return self.__dict__

    def __str__(self):
        return f"{self.service_id} - {self.name} {self.description} {self.service_type} {self.request}"
