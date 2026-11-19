from iadev.catalog import curriculum_nodes

def test_curriculum_structure():
    nodes = curriculum_nodes()
    ids = [node.id for node in nodes]
    assert len(ids) == len(set(ids))
    assert len([n for n in nodes if n.kind == "stage"]) == 8
    assert len([n for n in nodes if n.kind == "day"]) == 37
    assert all(n.parent_id is None or n.parent_id in ids for n in nodes)
