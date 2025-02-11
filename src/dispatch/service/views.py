from fastapi import APIRouter, Body, Depends, HTTPException, status
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from dispatch.database.core import get_db
from dispatch.database.service import common_parameters, search_filter_sort_paginate
from dispatch.exceptions import ExistsError
from dispatch.models import PrimaryKey

from .models import ServiceCreate, ServicePagination, ServiceRead, ServiceUpdate
from .service import get, create, update, delete, get_by_external_id_and_project_name


router = APIRouter()


@router.get("", response_model=ServicePagination)
def get_services(*, common: dict = Depends(common_parameters)):
    """Retrieve all services."""
    return search_filter_sort_paginate(model="Service", **common)


@router.post("", response_model=ServiceRead)
def create_service(
    *,
    db_session: Session = Depends(get_db),
    service_in: ServiceCreate = Body(
        ...,
        example={
            "name": "myService",
            "type": "pagerduty",
            "is_active": True,
            "external_id": "234234",
        },
    ),
):
    """Create a new service."""
    service = get_by_external_id_and_project_name(
        db_session=db_session,
        external_id=service_in.external_id,
        project_name=service_in.project.name,
    )
    if service:
        raise ValidationError(
            [
                ErrorWrapper(
                    ExistsError(msg="A service with this external_id already exists."),
                    loc="external_id",
                )
            ],
            model=ServiceCreate,
        )
    service = create(db_session=db_session, service_in=service_in)
    return service


@router.put("/{service_id}", response_model=ServiceRead)
def update_service(
    *, db_session: Session = Depends(get_db), service_id: PrimaryKey, service_in: ServiceUpdate
):
    """Update an existing service."""
    service = get(db_session=db_session, service_id=service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "A service with this id does not exist."}],
        )

    try:
        service = update(db_session=db_session, service=service, service_in=service_in)
    except IntegrityError:
        raise ValidationError(
            [ErrorWrapper(ExistsError(msg="A service with this name already exists."), loc="name")],
            model=ServiceUpdate,
        )

    return service


@router.get("/{service_id}", response_model=ServiceRead)
def get_service(*, db_session: Session = Depends(get_db), service_id: PrimaryKey):
    """Get a single service."""
    service = get(db_session=db_session, service_id=service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "A service with this id does not exist."}],
        )
    return service


@router.delete("/{service_id}")
def delete_service(*, db_session: Session = Depends(get_db), service_id: PrimaryKey):
    """Delete a single service."""
    service = get(db_session=db_session, service_id=service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "A service with this id does not exist."}],
        )
    delete(db_session=db_session, service_id=service_id)
