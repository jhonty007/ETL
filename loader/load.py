from sqlalchemy import create_engine, text
from config.config import DATABASE_URL
from logger.logger import setup_logger

logger = setup_logger()

def load(df):
    engine = create_engine(DATABASE_URL)
    upsert_query = text(""" 
        INSERT INTO employees (id, name, salary)\
        VALUES( :id, :name, :salary)
        ON CONFLICT (id)
        DO UPDATE SET
            name = EXCLUDED.name,
            salary = EXCLUDED.salary,
            updated_at = NOW()
        WHERE employees.name IS DISTINCT FROM EXCLUDED.name
           OR employees.salary IS DISTINCT FROM EXCLUDED.salary;                
    """)

    # starting the engine to connect and perform the operation 
    with engine.begin() as conn:
        conn.execute(upsert_query,df.to_dict(orient="records"))

    logger.info("data loaded successfully")