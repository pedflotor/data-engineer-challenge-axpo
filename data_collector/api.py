from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main import SensorData

DATABASE_URL = "sqlite:///iot_data.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI()

@app.get("/sensors/")
def get_sensors():
    session = SessionLocal()
    sensors = session.query(SensorData).all()
    session.close()
    return sensors


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
