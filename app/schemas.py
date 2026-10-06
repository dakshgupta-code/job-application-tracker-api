from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class ApplicationCreate(BaseModel):
    company_name: str
    job_title: str
    status: str = "saved"
    job_url: str | None = None
    location: str | None = None
    applied_date: date | None = None
    notes: str | None = None


class ApplicationUpdate(BaseModel):
    company_name: str | None = None
    job_title: str | None = None
    status: str | None = None
    job_url: str | None = None
    location: str | None = None
    applied_date: date | None = None
    notes: str | None = None


class ApplicationResponse(BaseModel):
    id: int
    company_name: str
    job_title: str
    status: str
    job_url: str | None
    location: str | None
    applied_date: date | None
    notes: str | None
    created_at: datetime | None
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)