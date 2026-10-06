from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post(
    "/applications",
    status_code=201,
    response_model=schemas.ApplicationResponse,
)
def create_application(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db),
):
    new_application = models.Application(**application.model_dump())

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application

@app.get(
    "/applications",
    response_model=list[schemas.ApplicationResponse],
)
def get_applications(db: Session = Depends(get_db)):
    applications = db.query(models.Application).all()
    return applications

@app.get(
    "/applications/{application_id}",
    response_model=schemas.ApplicationResponse,
)
def get_applications(application_id: int, db:Session = Depends(get_db)):
    application = db.query(models.Application).filter(models.Application.id == application_id).first()
    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    
    return application

@app.patch(
    "/applications/{application_id}",
    response_model=schemas.ApplicationResponse,
)
def update_application(
    application_id: int,
    application_data: schemas.ApplicationUpdate,
    db: Session = Depends(get_db),
):
    application = (
        db.query(models.Application)
        .filter(models.Application.id == application_id)
        .first()
    )

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    update_data = application_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(application, field, value)

    db.commit()
    db.refresh(application)

    return application
@app.delete("/applications/{application_id}")

def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
):
    application = (
        db.query(models.Application)
        .filter(models.Application.id == application_id)
        .first()
    )

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found")

    db.delete(application)
    db.commit()

    return {"message": "Application deleted successfully"}