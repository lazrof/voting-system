from app.adapter.inmemory_vote_repository import InMemoryVoteRepository
from app.domain.vote import Vote

def test_vote_save():
    vote = Vote()
    vote_repository = InMemoryVoteRepository()

    #vote recibe el vote_repository como argumento y con ese es que logra hacer el save.
    #es como dependency injection. Dependencia tiene los detalles de implementacion.
    # y vote es el que actua com modelo.
    assert vote.save(vote_repository=vote_repository).vote_id == vote.vote_id

def test_vote_repository_all():
    vote_repository = InMemoryVoteRepository()
    vote1 = Vote().save(vote_repository=vote_repository)
    vote2 = Vote().save(vote_repository=vote_repository)

    assert set(vote_repository.all()) == {vote1, vote2}

def test_vote_repository_total():
    vote_repository = InMemoryVoteRepository()
    Vote().save(vote_repository=vote_repository)
    Vote().save(vote_repository=vote_repository)

    assert vote_repository.total() == 2
