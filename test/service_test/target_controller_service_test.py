from repository.target_repository import get_target_by_id, get_all_targets
from service.target_controller_service import convert_one_target_to_json, convert_list_of_target_to_json


def test_convert_one_target_to_json():
    target = get_target_by_id(1).unwrap()
    result = convert_one_target_to_json(target)
    assert result


def test_convert_targets_to_list():
    targets = get_all_targets().unwrap()
    result = convert_list_of_target_to_json(targets)
    assert result
