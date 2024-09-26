from returns.maybe import Maybe, Nothing
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import Target


def create_target(target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def get_target_by_id(target_id: int) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional((
            session.query(Target)
            .get(target_id)
        ))


def get_all_targets() -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional((
            session.query(Target)
            .all()
        ))


def delete_target_by_id(target_id: int) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = get_target_by_id(target_id)
            if maybe_target is Nothing:
                return Failure(f"No user by the id {target_id}")
            target_to_delete = maybe_target.unwrap()
            session.delete(target_to_delete)
            session.commit()
            return Success(target_to_delete)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def update_target(target_id: int, target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            maybe_target = get_target_by_id(target_id).map(session.merge)
            if maybe_target is Nothing:
                return Failure(f"No target under the id {target_id}")
            target_to_update = maybe_target.unwrap()
            target_to_update.city = target.city
            target_to_update.state = target.state
            target_to_update.name = target.name
            target_to_update.address = target.address
            target_to_update.rental_fee = target.rental_fee
            target_to_update.late_fee = target.late_fee
            session.commit()
            session.refresh(target_to_update)
            return Success(target_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))
