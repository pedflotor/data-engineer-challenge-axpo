from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main import SensorData
from sqlalchemy.sql import func
from fastapi import Query
from pydantic import BaseModel
from typing import List, Optional

DATABASE_URL = "sqlite:///iot_data.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()

# Pydantic model to serialize SensorData
class SensorDataSchema(BaseModel):
    sensor_id: str
    value: float
    timestamp: str

    class Config:
        orm_mode = True  # Tells Pydantic to treat the SQLAlchemy model as a dict

# Route to get all sensor data
@app.get("/sensors/", response_model=List[SensorDataSchema])
def get_sensors():
    session = SessionLocal()
    sensors = session.query(SensorData).all()
    session.close()
    return sensors

# Route to get aggregated data for 60-minute intervals
@app.get("/sensors/aggregated60/", response_model=List[dict])
def get_aggregated_data(interval: int = Query(60)):
    session = SessionLocal()
    results = session.query(
        SensorData.sensor_id,
        func.strftime('%Y-%m-%d %H:%M', SensorData.timestamp).label("time_bucket"),
        func.avg(SensorData.value).label("avg_value")
    ).group_by(SensorData.sensor_id, "time_bucket").all()
    
    session.close()
    
    # Convert results to a list of dictionaries
    return [{"sensor_id": result[0], "time_bucket": result[1], "avg_value": result[2]} for result in results]

# Route to get aggregated data for 10-minute intervals
@app.get("/sensors/aggregated10/", response_model=List[dict])
def get_aggregated_data(interval: int = Query(10)):
    session = SessionLocal()
    results = session.query(
        SensorData.sensor_id,
        func.strftime('%Y-%m-%d %H:%M', SensorData.timestamp).label("time_bucket"),
        func.avg(SensorData.value).label("avg_value")
    ).group_by(SensorData.sensor_id, "time_bucket").all()
    
    session.close()
    
    # Convert results to a list of dictionaries
    return [{"sensor_id": result[0], "time_bucket": result[1], "avg_value": result[2]} for result in results]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


