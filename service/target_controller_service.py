from typing import Dict, List

from sqlalchemy import inspect
from toolz import pipe
from toolz.curried import partial

from model import Target


def convert_one_target_to_json(target: Target) -> Dict[str, str]:
    return {c.key: getattr(target, c.key) for c in inspect(target).mapper.column_attrs}


def convert_list_of_target_to_json(targets: List[Target]) -> List[Dict[str, str]]:
    return pipe(
        targets,
        partial(map, lambda target: convert_one_target_to_json(target)),
        list
    )


def create_target(target_dict: Dict[str, str]) -> Target:
    return Target(
        coordinates_id=target_dict["coordinates_id"],
        location_id=target_dict["location_id"],
        type_id=target_dict["type_id"],
        industry_id=target_dict["industry_id"],
        priority=target_dict["priority"],
        mission_id=target_dict["mission_id"],
    )