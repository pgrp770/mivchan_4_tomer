from repository.target_repository import get_target_by_id, get_all_targets


def test_get_target_by_mission_id():
    result = get_target_by_id(1).unwrap()
    assert result


def test_get_all_targets():
    result = get_all_targets().unwrap()
    assert result
