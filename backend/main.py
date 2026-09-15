import os
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from typing import List, Literal
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Session


DATABASE_URL = os.getenv('DATABASE_URL') or 'sqlite:///./test_run_hub.db'
engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
Base = declarative_base()


class TestRun(Base):
    __tablename__ = 'test_runs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    suite_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    duration_seconds = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)


class TestRunCreate(BaseModel):
    title: str = Field(..., min_length=4, max_length=100)
    suite_name: str = Field(..., min_length=4, max_length=50)
    status: Literal['PASSED', 'FAILED', 'SKIPPED']
    duration_seconds: float = Field(..., gt=0)


class TestRunResponse(BaseModel):
    id: int
    title: str
    suite_name: str
    status: str
    duration_seconds: float
    created_at: datetime

    class Config:
        orm_mode = True


apps = FastAPI(
    title='my test run hub',
    description='A simple test run hub API',
    version='1.0.0',
)


apps.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@apps.get('/api/v1/runs', response_model=List[TestRunResponse])
def get_all(db: Session = Depends(get_db)):
    return db.query(TestRun).order_by(TestRun.created_at.desc()).all()


@apps.get('/api/v1/runs/{run_id}', response_model=TestRunResponse)
def get_run(run_id: int, db: Session = Depends(get_db)):
    run = db.query(TestRun).filter(TestRun.id == run_id).first()
    if not run:
        raise HTTPException(status_code=404, detail='Test run not found')
    return run


@apps.post('/api/v1/runs', response_model=TestRunResponse, status_code=201)
def create_run(run: TestRunCreate, db: Session = Depends(get_db)):
    new_run = TestRun(**run.model_dump())
    db.add(new_run)
    db.commit()
    db.refresh(new_run)
    return new_run