from functools import partial

from flask import Blueprint, request, jsonify

from repository.target_repository import get_target_by_id, create_target, delete_target_by_id, update_target, \
    get_all_targets
from service.target_controller_service import convert_one_target_to_json, convert_list_of_target_to_json

target_blueprint = Blueprint("target", __name__)


@target_blueprint.route("/<int:target_id>", methods=['GET'])
def get_target_by_id_api(target_id: int):
    return (
        get_target_by_id(target_id)
        .map(convert_one_target_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )


@target_blueprint.route("/", methods=['GET'])
def get_targets_api():
    return (
        get_all_targets()
        .map(convert_list_of_target_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )


# @target_blueprint.route("/create", methods=['POST'])
# def create_target_api():
#     return (
#         create_target(request.json)
#         .map(convert_one_target_to_json)
#         .map(create_target)
#         .map(lambda u: (jsonify(u), 200))
#         .value_or((jsonify({}), 400))
#     )
# @target_blueprint.route("/delete/<int:user_id>", methods=['DELETE'])
# def delete_user_controller(user_id):
#     return (
#         delete_target_by_id(user_id)
#         .map(convert_to_json)
#         .map(lambda u: (jsonify(u), 200))
#         .value_or((jsonify({}), 404))
#     )
#
#
# @target_blueprint.route("/update/<int:user_id>", methods=["PUT"])
# def update_user_controller(user_id):
#     return (
#         convert_to_user(request.json)
#         .bind(partial(update_user, user_id))
#               .map(convert_to_json)
#               .map(lambda u: (jsonify(u), 200))
#               .value_or((jsonify({}), 400))
#               )
