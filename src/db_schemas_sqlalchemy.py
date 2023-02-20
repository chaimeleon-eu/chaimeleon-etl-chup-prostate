from sqlalchemy.types import *

patient_schema = {
    'person_id': Integer,
    'gender_concept_id': Integer,
    'gender_concept_description': String(50),
    'year_of_birth': Integer,
    'birth_datetime': DateTime,
    'race_concept_id': Integer,
    'ethnicity_concept_id': Integer,
    'person_source_value': String(50)
}

conditions_schema = {
    'condition_occurrence_id': Integer,
    'person_id': Integer,
    'condition_concept_id': Integer,
    'condition_concept_description': String(100),
    'condition_vocab': String(20),
    'condition_start_date': DateTime,
    'condition_type_concept_id': Integer,
    'condition_type_concept_description': String(50),
    'condition_status_concept_id': Integer,
    'condition_status_concept_description': String(50)
}

measurement_schema = {
    'measurement_id': Integer,
    'person_id': Integer,
    'measurement_concept_id': Integer,
    'measurement_concept_description': String(100),
    'measurement_concept_vocab': String(20),
    'measurement_date': Date,
    'value_as_concept_id': Integer,
    'value_as_concept_description': String(50),
    'value_as_concept_vocab': String(20),
    'unit_concept_id': Integer,
    'unit_concept_description': String(50),
    'unit_concept_vocab': String(20),
    'range_low': Float,
    'range_high': Float,
    'measurement_type_concept_id': Integer,
    'measurement_type_concept_description': String(50),
    'value_as_number': Float,
    'meas_event_field_concept_id': Integer,
    'meas_event_field_concept_description': String(50),
    'meas_event_field_concept_vocab': String(20)
}

observation_schema = {
    'observation_id': Integer,
    'person_id': Integer,
    'observation_concept_id': Integer,
    'observation_concept_description': String(100),
    'observation_concept_vocab': String(20),
    # 'visit_occurrence_id': Integer,
    'observation_date': Date,
    'observation_type_concept_id': Integer,
    'observation_type_concept_description': String(50),
    'value_as_concept_id': Integer,
    'value_as_concept_description': String(100),
    'value_as_concept_vocab': String(20),
    'obs_event_field_concept_id': Integer,
    'obs_event_field_concept_description': String(100),
    'obs_event_field_concept_vocab': String(20),
    'nomop_phase': String(10)
}

procedure_schema = {
    'procedure_occurrence_id': Integer,
    'person_id': Integer,
    'procedure_concept_id': Integer,
    'procedure_concept_description': String(50),
    'procedure_concept_vocab': String(20),
    'procedure_date': Date,
    'procedure_end_date': Date,
    'procedure_type_concept_id': Integer,
    'procedure_type_concept_description': String(50),
    'modifier_concept_id': Integer,
    'modifier_concept_description': String(50),
    'modifier_concept_vocab': String(20),
}

specimen_schema = {
    'specimen_id': Integer,
    'person_id': Integer,
    'specimen_concept_id': Integer,
    'specimen_concept_description': String(50),
    'specimen_date': Date,
    'specimen_concept_vocab': String(20),
    'specimen_type_concept_id': Integer,
    'specimen_type_concept_description': String(50),
}

drug_schema = {
    'drug_exposure_id': Integer,
    'person_id': Integer,
    'drug_concept_id': Integer,
    'drug_concept_description': String(50),
    'drug_concept_vocab': String(20),
    'drug_exposure_start_date': Date,
    'drug_exposure_end_date': Date,
    'drug_type_concept_id': Integer,
    'drug_type_concept_description': String(50)
}

death_schema = {
     'person_id': Integer,
     'death_date': Date
}
