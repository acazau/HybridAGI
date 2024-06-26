from hybridagi import FactMemory
from hybridagi import FakeEmbeddings

def test_add_triplet():
    emb = FakeEmbeddings(dim=250)
    memory = FactMemory(
        index_name="test",
        embeddings=emb,
        wipe_on_start=True,
    )

    memory.add_triplet("myself", "is a", "robot")


def test_delete_triplet():
    emb = FakeEmbeddings(dim=250)
    memory = FactMemory(
        index_name="test",
        embeddings=emb,
        wipe_on_start=True,
    )

    memory.add_triplet("myself", "is a", "robot")
    memory.delete_triplet("myself", "is a", "robot")
    assert len(memory.get_triplets("myself")) == 0

def test_get_rel_map():
    emb = FakeEmbeddings(dim=250)
    memory = FactMemory(
        index_name="test",
        embeddings=emb,
        wipe_on_start=True,
    )

    memory.add_triplet("myself", "is a", "robot")
    memory.add_triplet("robot", "has", "sensors")
    memory.add_triplet("robot", "can", "move")

    rel_map = memory.get_rel_map(subjs=["myself", "robot"], depth=2, limit=30)

    assert len(rel_map) == 2
    assert len(rel_map["myself"]) == 3
    assert len(rel_map["robot"]) == 2