import logging
import numpy as np
import pandas as pd

import src.chaimeleon_etl.utils as su

logging.basicConfig(format='[%(asctime)s] - %(levelname)s: %(message)s', datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO)
 

def etl_chup_datalake_patient(df: pd.DataFrame, df_gender: pd.DataFrame) -> pd.DataFrame:
    
    logging.info("table patient")
    df = df.copy()
    n = len(df) + 1

    df_patient = pd.DataFrame().assign(
        person_id=np.arange(1, n),
        gender_concept_id=None, # df['Gender'], # missing gender from source
        gender_concept_description=None,
        year_of_birth=None, # df['Birth_date'].dt.year,
        birth_datetime=None, # df['Idade'], # with years old we got nothing, we need birth date 
        race_concept_id=np.zeros((n-1,), dtype=int),
        ethnicity_concept_id=np.zeros((n-1,), dtype=int),
        person_source_value=df['Unnamed:_0_level_0']
    )
    # df_patient = pd.merge(df_patient, df_gender, how='left', on=['Gender'])
    
    df_patient_columns = [
        'person_id', 'gender_concept_id', 'gender_concept_description', 'year_of_birth',
        'birth_datetime', 'race_concept_id', 'ethnicity_concept_id', 'person_source_value']
    df_patient = df_patient[df_patient_columns]

    return df_patient

def etl_chup_datalake_conditions(df: pd.DataFrame, df_condition_concept: pd.DataFrame) -> pd.DataFrame:
        
    logging.info("table conditions")
   
    concepts = {
        'malignant_neoplasm_hystotype':[
            df['Tipo_histológico'], df['Data_1']],
        'neural_invasion':[
            df['Invasão_perineural'],df['Data_1']],
        'vascular_invasion':[#??
            df['Invasão_vasculolinfática'],df['Data_1']],
        # 'lymph_invasion':[
        #     df['Lymphatic_invasion'],df['Data_1']],
        'gleason_score':[
            df['GS'],df['Data_1']],
        'gleason_group':[
            df['Grupo_grau_(IDC)'],df['Data_1']],
        # 'bladder_control':[
        #     df['Bladder_control'],df['Bladder_control_Date_of_diagnosis_(if_applicable)']],
        # 'bowel_control':[
        #     df['Bowel_control'],df['Bowel_control_Date_of_diagnosis_(if_applicable)']],
        # 'Sexual_function':[
        #     df['Sexual_function'],df['Sexual_function_Date_of_diagnosis_(if_applicable)']],
        # 'hormone_treat':[
        #    df['Hormone_treatment_response_/_Castration_status_Diagnosis'],df['Hormone_treatment_response_/_Castration_status_Date_of_diagnosis_(if_applicable)']],
        # 'progression':[
        #    df['Progression_or_Recurrence'],pd.to_datetime(df['Progression_or_Recurrence_Date'], errors='coerce'),],
        # 'cause_of_death':[
        #    [hystotype + '-mortal' if death_related == 1 else None for death_related, hystotype in zip(df['Death_related_to_underlying_Prostate_Cancer'],df['Malignant_Neoplasm_Histotype'])],
        #    df['Date_of_death_(if_applicable)']],
    }
    columns = [
        'condition_concept',
        'condition_start_date',
    ]
    
    df_conditions = su.map_multi_concept(df,columns, concepts)

    df_conditions = pd.merge(df_conditions, df_condition_concept, how='left', on=['condition_concept'])
    df_conditions = df_conditions.astype({'condition_concept_id': 'Int64'})

    df_conditions = df_conditions[df_conditions['condition_concept_description'].notnull()]

    n_conditions = len(df_conditions) + 1
    df_conditions = df_conditions.assign(
        condition_occurrence_id=np.arange(1, n_conditions),
        condition_type_concept_id=32809,
        condition_type_concept_description='Case Report Form',
    )

    df_conditions_columns = [
        'condition_occurrence_id', 'person_id', 'condition_concept_id', 'condition_concept_description',
        'condition_vocab', 'condition_start_date', 'condition_type_concept_id', 'condition_type_concept_description',
        'condition_status_concept_id', 'condition_status_concept_description']
    
    df_conditions = df_conditions[df_conditions_columns]
    
    return df_conditions

def etl_chup_datalake_measurement(
        df: pd.DataFrame,
        df_measurement_concept: pd.DataFrame,
        df_measurement_value_as_concept: pd.DataFrame,
        df_measurement_event_field: pd.DataFrame,
        df_measurement_unit: pd.DataFrame) -> pd.DataFrame:
    
    logging.info("table measurement")
    concepts = {
        'test_psa': [
            'Total prostate specific antigen level',
            pd.to_datetime(df['Data'], errors='coerce'),
            df['PSA_total_(3_meses_da_RMN)'],
            None,# df['Unit_Laboratory_Studies'],
            None,# df['Range_min_Laboratory Studies'],
            None,# df['Range_max_Laboratory_Studies'],
            None, None],
        'test_serica': [
            'Serum testosterone measurement',
            pd.to_datetime(df['Data'], errors='coerce'),
            df['T_sérica'],
            None,# df['Unit_Laboratory_Studies'],
            None,# df['Range_min_Laboratory Studies'],
            None,# df['Range_max_Laboratory_Studies'],
            None, None],
        'prostate_img': [
            [str(x) + 'pi' if str(x).isnumeric() else x for x in df['PI-RADS']],
            df['DataRMN'],
            None, None, None, None, None, None],
        # 'lymph_nodes_meta':[
        #     [ 'lymph nodes metastasis' if  existMetas == 1 else None for existMetas in df['Lymph_Nodes_Metastasis']],
        #     pd.to_datetime(df['Progression_or_Recurrence_Date'], errors='coerce'),
        #     None, None, None, None, None,
        #     1147663],
        # 'viscera_meta':[
        #    [ 'viscera metastasis' if  existMetas == 1 else None for existMetas in df['Metastasis_to_the_Viscera']],
        #     pd.to_datetime(df['Progression_or_Recurrence_Date'], errors='coerce'),
        #     None, None, None, None, None,
        #     1147663],
        # 'bone_meta':[
        #   [ 'bone metastasis' if  existMetas == 1 else None for existMetas in df['Metastasis_to_the_Bone']],
        #     pd.to_datetime(df['Progression_or_Recurrence_Date'], errors='coerce'),
        #     None, None, None, None, None,
        #     1147663],
        # 'distant_meta':[
        #    [ 'distant metastasis' if  existMetas == 1 else None for existMetas in df['Distant_Metastasis_NOS']],
        #     pd.to_datetime(df['Progression_or_Recurrence_Date'], errors='coerce'),
        #     None, None, None, None, None,
        #     1147663],
        'primary_gleason':[
            [str(x) + 'pg' if str(x).isnumeric() else x for x in df['G1']],
            df['Data_2'],
            None, None, None, None, None, 
            1147663],
        'secondary_gleason':[
            [str(x) + 'sg' if str(x).isnumeric() else None for x in df['G2']],
            df['Data_2'],
            None, None, None, None, None, 
            1147663],
        'sentinel_lymph_node':[
            ['Sentinel Lymph Nodes' if pd.notnull(x) else None for x in df['Gânglios']],
            df['Data_2'],
            None, None, None, None,
            ['Positive' if x == 1 else 'Negative' for x in df['Gânglios']],
            1147663],
        'tumor_path_category':[ # TODO Filtrar casos raros
            ['TNM Path T' if pd.notnull(x) else None for x in df['pT']],
            df['Data_2'],
            None, None, None, None,
           [ 'pT' + str(x) for x in df['pT']],
            1147663],
        'lymph_node_path_category':[
            ['TNM Path N' if pd.notnull(x) else None for x in df['pN']],
            df['Data_2'],
            None, None, None, None,
            ['pN' + str(x) for x in df['pN']],
            1147663],
        # 'metastasis_path_category':[
        #     ['TNM Path M' if pd.notnull(x) else None for x in df['pR']],## unconfirmed
        #     df['Data_1'],
        #     None, None, None, None,
        #     df['pR'],
        #     1147663],
        # 'path_stage':[
        #     ['TNM Path Stage Group' if pd.notnull(x) else None for x in df['User_defined_TNM_Pathological_Stage_group_(if_different_from_calculated_result)']],
        #     df['Data_1'],
        #     None, None, None, None,
        #     [x + '_P' if pd.notnull(x) else None for x in df['User_defined_TNM_Pathological_Stage_group_(if_different_from_calculated_result)']],
        #     1147663],
        # 'tumor_clinical_category':[
        #     ['TNM Clin T' if pd.notnull(x) else None for x in df['Tumor_(T)_Clinical_Category']],
        #     df['PI-RADS_report_date'],
        #     None, None, None, None,
        #     df['Tumor_(T)_Clinical_Category'],
        #     1147663],
        # 'lymph_node_clinical_category':[
        #     ['TNM Clin N' if pd.notnull(x) else None for x in df['Regional_Lymph_Nodes_(N)_Clinical_Category']],
        #     df['PI-RADS_report_date'],
        #     None, None, None, None,
        #     df['Regional_Lymph_Nodes_(N)_Clinical_Category'],
        #     1147663],
        #  'metastasis_clinical_category':[
        #     ['TNM Clin M' if pd.notnull(x) else None for x in df['Metastasis_(M)_Clinical_Category']],
        #     df['PI-RADS_report_date'],
        #     None, None, None, None,
        #     df['Metastasis_(M)_Clinical_Category'],
        #     1147663],
        #  'clinical_stage':[
        #     ['TNM Clin Stage Group' if pd.notnull(x) else None for x in df['User_defined_TNM_Clinical_Stage_group_(if_different_from_calculated_result)']],
        #     df['PI-RADS_report_date'],
        #     None, None, None, None,
        #     [x + '_C' if pd.notnull(x) else None for x in df['User_defined_TNM_Clinical_Stage_group_(if_different_from_calculated_result)']],
        #     1147663]
    }

    columns = [
        'measurement_concept',
        'measurement_date',
        'value_as_number', 
        'unit_concept', 
        'range_low', 
        'range_high',
        'value_as_concept',
        'meas_event_field_concept_id'
                ]  
    df_measurement = su.map_multi_concept(df,columns,concepts)

    df_measurement = pd.merge(df_measurement, df_measurement_concept, how='left', on=['measurement_concept'])
    df_measurement = pd.merge(df_measurement, df_measurement_value_as_concept, how='left', on=['value_as_concept'])
    df_measurement = pd.merge(df_measurement, df_measurement_event_field, how='left', on=['meas_event_field_concept_id'])
    # df_measurement = pd.merge(df_measurement,df_measurement_unit,how='left',on=['unit_concept'])

    df_measurement = df_measurement[df_measurement['measurement_concept_description'].notnull()]

    n_measurement = len(df_measurement) + 1
    df_measurement = df_measurement.assign(
        measurement_id=np.arange(1, n_measurement),
        measurement_type_concept_id=32809,
        measurement_type_concept_description="Case Report Form",
        unit_concept_id=None,
        unit_concept_description=None,
        unit_concept_vocab=None,
        )

    df_measurement_columns = [
        'measurement_id',
        'person_id',
        'measurement_concept_id',
        'measurement_concept_description',
        'measurement_concept_vocab',
        'measurement_date',
        'measurement_type_concept_id',
        'measurement_type_concept_description',
        'value_as_number',
        'value_as_concept_id',
        'value_as_concept_description',
        'value_as_concept_vocab',
        'unit_concept_id',
        'unit_concept_description',
        'unit_concept_vocab',
        "range_low",
        "range_high",
        'meas_event_field_concept_id',
        'meas_event_field_concept_description',
        'meas_event_field_concept_vocab',
    ]

    df_measurement = df_measurement[df_measurement_columns]

    return df_measurement

def etl_chup_datalake_observation(df: pd.DataFrame, 
        df_observation_concept: pd.DataFrame,
        df_observation_value_as_concept: pd.DataFrame,
        df_observation_event_field:pd.DataFrame) -> pd.DataFrame:

    logging.info("table observation")
    
    concepts = {
        # 'ecog_performance_diag':[
        #     [str(x) + 'ecog' if str(x).isnumeric() else x for x in df['ECOG']],
        #     pd.to_datetime(df['DataRMN'], errors='coerce'), # is this date right?
        #     None,None,'diagnosis'],
        # 'ecog_performance_fu':[
        #      [str(x) + 'ecog' if str(x).isnumeric() else x for x in df['ECOG_Performance_status2']],
        #   pd.to_datetime(df['ECOG_Date_of_performance_status_record_(if_applicable)'], errors='coerce'),
        #     None,None,'followup'],
        'benign_hiperplasia':[
            [str(x) + '_hyper' if x == 1 or x == 0 else x for x in df['HBP_1']],
            df['Data_2'],
            'Benign prostatic hyperplasia', None,None],
        # 'deferred_treat':[
        #     df['Deferred_treatment'],#differentiate numeric concepts
        #     pd.to_datetime(df['Date_of_initiation_(if_applicable)'], errors='coerce'),
        #     None,None,None],
        # 'local_recurrence':[
        #     ['local_recurrence' if x == 1 else None for x in df['Local_recurrence_or_progression']],
        #      pd.to_datetime(df['Progression_or_Recurrence_Date'], errors='coerce'),
        #     None,1147663,None],
        #  'last_contact':[ # no pilla ninguna
        #    ['Date last contact' if pd.notnull(LCDate) and pd.isnull(deathDate) else None for LCDate,deathDate in zip(df['Date_of_last_contact_(if_no_date_of_death_already_registered)'],df['Date_of_death_(if_applicable)'])],#differentiate numeric concepts
        #     pd.to_datetime(df['Date_of_last_contact_(if_no_date_of_death_already_registered)'], errors='coerce'),
        #     None,None,None],

    }
    columns=[
        'observation_concept',
        'observation_date',
        'value_as_concept',
        'obs_event_field_concept_id',
        'nomop_phase'
    ]

    df_observation = su.map_multi_concept(df,columns,concepts)

    df_observation = pd.merge(df_observation, df_observation_concept, how='left', on=['observation_concept'])
    df_observation = pd.merge(df_observation, df_observation_value_as_concept, how='left', on=['value_as_concept'])
    df_observation = pd.merge(df_observation, df_observation_event_field, how='left', on=['obs_event_field_concept_id'])
    
    df_observation = df_observation[df_observation['observation_concept_description'].notnull()]

    n_observation = len(df_observation) + 1
    df_observation = df_observation.assign(
        observation_id=np.arange(1, n_observation),
        # visit_occurrence_id=None, ??
        observation_type_concept_id=32809,
        observation_type_concept_description='Case Report Form')

    df_observation_columns = [
        'observation_id',
        'person_id',
        'observation_concept_id',
        'observation_concept_description',
        'observation_concept_vocab',
        'observation_date',
        'observation_type_concept_id',
        'observation_type_concept_description',
        'value_as_concept_id',
        'value_as_concept_description',
        'value_as_concept_vocab',
        'obs_event_field_concept_id',
        'obs_event_field_concept_description',
        'obs_event_field_concept_vocab',
        'nomop_phase'
    ]

    df_observation = df_observation[df_observation_columns]
    return df_observation


def etl_chup_datalake_specimen(df: pd.DataFrame) -> pd.DataFrame:

    logging.info("table specimen")
    df = df.copy()
    n = len(df) + 1

    df_specimen = pd.DataFrame().assign(
        person_id=np.arange(1, n),
        specimen_concept_id=[4028082 if pd.notnull(x) else None for x in df['Data_1']],
        specimen_date=df['Data_2'],
    )

    df_specimen = df_specimen[df_specimen['specimen_concept_id'].notnull()]

    df_specimen_concept = pd.DataFrame(data={
        'specimen_concept_id': [4028082],
        'specimen_concept_description': ['Tissue specimen from prostate'],
        'specimen_concept_vocab': ['SNOMED']
    })
   
    df_specimen = pd.merge(df_specimen,df_specimen_concept,how='left', on=['specimen_concept_id'])
    

    n_specimen = len(df_specimen) + 1
    df_specimen = df_specimen.assign(
        specimen_id=np.arange(1, n_specimen),
        specimen_type_concept_id=32809,
        specimen_type_concept_description="Case Report Form",
       )
    
    df_specimen_columns = [
        'specimen_id',
        'person_id',
        'specimen_concept_id',
        'specimen_concept_description',
        'specimen_concept_vocab',
        'specimen_date',
        'specimen_type_concept_id',
        'specimen_type_concept_description',
    ]

    df_specimen = df_specimen[df_specimen_columns]

    return df_specimen

#procedure

#drugs

#death

