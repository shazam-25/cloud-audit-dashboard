from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Reads the connection string from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set!")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class RecommendationDB(Base):
    __tablename__ = "finops_recommendation"

    id = Column(Integer, primary_key=True, index=True)
    resource = Column(String, index=True)
    action = Column(String)

# Create tables automatically on startup if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SRE FinOps Dashboard")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "SRE FinOps Dashboard Active"
    }

@app.get("/finops/audit")
def get_audit():
    db = SessionLocal()
    try:
        recommendations = db.query(RecommendationDB).all()

        # Seed initial mock data if the table is freashly created
        if not recommendations:
            default_recs = [
                RecommendationDB(
                    resource="vm-instance-01",
                    action="Downsize instance tier to save ~30% monthly cost",
                ),
                RecommendationDB(
                    resource="k8s-cluster-03",
                    action="Downsize instance tier to save ~30% monthly cost",
                )
            ]
            db.add_all(default_recs)
            db.commit()
            recommendations = default_recs

        return {
            "status": "success",
            "finops_recommendations_count": len(recommendations),
            "recommendations": [
                {
                    "resource": r.resource,
                    "action": r.action
                } for r in recommendations
            ]
        }
    finally:
        db.close()