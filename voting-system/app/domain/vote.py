import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    # This is necessary to prevent circular imports
    from app.domain.vote_repository import VoteRepository


@dataclass # como un modelo de django? una entidad.
class Vote:
    """Vote entity. Receives a vote_id as parameter, if not vote_id given it will generate one.

    vote_id: str = uuid4
    """
    vote_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def save(self, vote_repository: "VoteRepository"):
        vote_repository.add(self)

    # es usado para poder usar las llaves {} sobre un vote y obtener su hash(?)
    def __hash__(self) -> int:
        return hash(self.vote_id)

