from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

DATABASE_URL = "postgresql://kairos:kairos@postgres-py:5432/kairos_py"


for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("✅ Database connected")
        break
    except Exception as e:
        print("⏳ Waiting for database...")
        time.sleep(2)
else:
    raise Exception("❌ Could not connect to database")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)