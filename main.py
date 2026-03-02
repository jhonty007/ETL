
# import os 
# import pandas as pd
# from  sqlalchemy import create_engine,text
# import logging

# # loading the dot env 

# # logging setup

# # //database config


# # etl_process

# def extract():
#     logger.info("extracting data...")
#     df=pd.read_csv("data/sample.csv")
#     return df

# def transform(df):
#     logger.info("Transforming the extracted data")

#     df = df.drop_duplicates()
#     df["salary"] = df["salary"].fillna(0)
#     df["processed_at"] = pd.Timestamp.utcnow()
#     return df

# def load(df):
#     logger.info("Loading the data into the database")
#     engine=create_engine(DATABASE_URL)
#     # df.to_sql("employees", engine, if_exists="append" , index=False)

#     with engine.begin() as conn:
#         for _,row in df.iterrows():
#             query = text(""" 
#                 CREATE TABLE IF NOT EXISTS employees(
#                     id BIGINT PRIMARY KEY,
#                     name TEXT,
#                     salary BIGINT,
#                     processed_at TIMESTAMP WITH TIME ZONE );
                         
#                 INSERT into employees (id,name,salary,processed_at)
#                 VALUES (:id, :name, :salary, :processed_at)
#                 ON CONFLICT(id)
#                 DO UPDATE SET 
#                     name= EXCLUDED.name,
#                     salary=EXCLUDED.salary,
#                     processed_at=NOW()
                
#                 WHERE employees.name IS DISTINCT FROM EXCLUDED.name OR
#                     employees.salary IS DISTINCT FROM EXCLUDED.salary;
#             """)

#             conn.execute(query, {
#                 "id":row["id"],
#                 "name": row["name"],
#                 "salary": row["salary"],
#                 "processed_at": row["processed_at"]
                
#             })

#     logger.info("Data loaded successfully!")


# def run_pipeline():
#     try:
#         df=extract()
#         df=transform(df)
#         load(df)
#         logger.info("ETL pipeline completed succesfully")
#     except:
#         logger.info("Pipeline execution failed ", exc_info=True)


# if __name__=="__main__":
#     run_pipeline()


from extractor.extract import extract
from transformer.transform import transform
from loader.load import load
from logger.logger import setup_logger

logger = setup_logger()

def run_pipeline():
    logger.info("Starting ETL pipeline")

    df = extract()
    df = transform(df)
    load(df)

    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
