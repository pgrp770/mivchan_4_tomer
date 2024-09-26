from model import Target
from repository.target_repository import get_target_by_id, get_all_targets, create_target


def test_get_target_by_id():
    result = get_target_by_id(1).unwrap()
    assert result


def test_get_all_targets():
    result = get_all_targets().unwrap()
    assert result


def test_create_target():
    target = Target(coordinates_id=1,
                    location_id=1,
                    type_id=1,
                    industry_id=1,
                    priority=1,
                    mission_id=2
                    )
    result = create_target(target)
    assert result
