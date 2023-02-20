import logging
import pandas as pd
from sqlalchemy.sql import text as sa_text
import sqlalchemy.schema as sch
from src import engine
import src.chaimeleon_etl.utils as su
import src.chaimeleon_etl.db as db
import src.datalake.etl_chup_datalake_prostate as ch

def etl_chup_datalake(filename: str, path_input_data: str) -> None:
    # load raw data
    logging.info(f"initializing etl La Fe datalake")
    df = pd.read_excel(f'{path_input_data}{filename}', sheet_name='Dados',header=[1,2,3])
    df.columns = [a for a, b, c in df.columns.tolist()]
    df.columns = [i.strip().replace(' ', '_').replace('\n', '').replace('__', '_') for i in df.columns]
    df = su.deduplicate_columns(df=df)

        # load auxiliary data
    df_gender = pd.read_csv(f'{path_input_data}gender.csv', sep=";")
    df_condition_concept = pd.read_csv(f'{path_input_data}condition-concept.csv', sep=";")
    df_measurement_concept = pd.read_csv(f'{path_input_data}measurement-concept.csv', sep=";")
    df_measurement_value_as_concept = pd.read_csv(f'{path_input_data}measurement-value-as-concept.csv', sep=";")
    df_measurement_event_field = pd.read_csv(f'{path_input_data}measurement-event-field.csv', sep=";")
    df_observation_concept = pd.read_csv(f'{path_input_data}observation-concept.csv', sep=";")
    df_observation_value_as_concept = pd.read_csv(f'{path_input_data}observation-value-as-concept.csv', sep=";")
    df_observation_event_field = pd.read_csv(f'{path_input_data}observation-event-field.csv', sep=";")

    # omop tables
    df_patient = ch.etl_chup_datalake_patient(df=df, df_gender=df_gender)
    df_conditions = ch.etl_chup_datalake_conditions(df=df,df_condition_concept=df_condition_concept)
    df_measurement = ch.etl_chup_datalake_measurement(
        df=df,
        df_measurement_concept=df_measurement_concept,
        df_measurement_value_as_concept=df_measurement_value_as_concept,
        df_measurement_event_field=df_measurement_event_field)
    df_observation = ch.etl_chup_datalake_observation(
        df=df,
        df_observation_concept=df_observation_concept,
        df_observation_value_as_concept=df_observation_value_as_concept,
        df_observation_event_field=df_observation_event_field)

   
    df_specimen = ch.etl_chup_datalake_specimen(df=df)

    # create temp schema if not exists
    sql_create_schema = f"CREATE SCHEMA IF NOT EXISTS temp"
    engine.execute(sa_text(sql_create_schema).execution_options(autocommit=True))

     # update data in the datalake
    db.upsert_df(df=df_patient, schema='public', table='patient', key_columns=['person_id'])
    db.upsert_df(df=df_conditions, schema='public', table='conditions', key_columns=['condition_occurrence_id'])
    db.upsert_df(df=df_measurement, schema='public', table='measurement', key_columns=['measurement_id'])
    db.upsert_df(df=df_observation, schema='public', table='observation', key_columns=['observation_id'])
    db.upsert_df(df=df_specimen, schema='public', table='specimen', key_columns=['specimen_id'])
   
   
   
    # TODO: delete temp schema
    return None

if __name__ == "__main__":
    etl_chup_datalake(filename='Cópia de BD1_anonimizado_25jan_revBahia.xlsx', path_input_data='./data/')
