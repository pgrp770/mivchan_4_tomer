from flask import Blueprint, request, jsonify

from model import Target
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


@target_blueprint.route("/update/<int:target_id>", methods=["PUT"])
def update_target_api(target_id):
    target_data = request.json
    return (
        update_target(target_id, target_data)
        .map(convert_one_target_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({"error": "Target not found or update failed"}), 400))
    )


@target_blueprint.route("/delete/<int:target_id>", methods=['DELETE'])
def delete_user_controller(target_id):
    return (
        delete_target_by_id(target_id)
        .map(convert_one_target_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )


@target_blueprint.route("/create", methods=['POST'])
def create_target_api():
    target_data = request.json
    target = Target(**target_data)
    return (
        create_target(target)
        .map(convert_one_target_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({"error": "Target creation failed"}), 400))
    )
