from models.base import Attack
from repository.abstract_repository import AbstractRepository


class AttackRepository(AbstrackRepository):

    def get(self, attack_id):
        return self.session.query(Attack).filter_by(id=attack_id).one_or_none()



