-- patient
CREATE TABLE person( 
	person_id INTEGER,
	gender_concept_id INTEGER,
	gender_concept_description VARCHAR(50),
	year_of_birth INTEGER,
	birth_datetime TIMESTAMP,
	race_concept_id INTEGER,
	ethnicity_concept_id INTEGER,
    person_source_value VARCHAR(50)
);

--  conditions
CREATE TABLE condition_ocurrence(
	condition_occurrence_id INTEGER,
	person_id INTEGER,
	condition_concept_id INTEGER,
	condition_concept_description VARCHAR(100),
	condition_vocab VARCHAR(20),
	condition_start_date TIMESTAMP,
	condition_type_concept_id INTEGER,
	condition_type_concept_description VARCHAR(50),
	condition_status_concept_id INTEGER,
	condition_status_concept_description VARCHAR(50)
);

-- measurement
CREATE TABLE measurement(
	measurement_id INTEGER,
	person_id INTEGER,
	measurement_concept_id INTEGER,
	measurement_concept_description VARCHAR(100),
	measurement_concept_vocab VARCHAR(20),
	measurement_date DATE,
	value_as_concept_id INTEGER,
	value_as_concept_description VARCHAR(50),
	value_as_concept_vocab VARCHAR(20),
	unit_concept_id INTEGER,
	unit_concept_description VARCHAR(50),
	unit_concept_vocab VARCHAR(20),
	range_low DECIMAL,
	range_high DECIMAL,
	measurement_type_concept_id INTEGER,
	measurement_type_concept_description VARCHAR(50),
	value_as_number DECIMAL,
	meas_event_field_concept_id INTEGER,
	meas_event_field_concept_description VARCHAR(50),
	meas_event_field_concept_vocab VARCHAR(20)
);

-- observation
CREATE TABLE observation(
	observation_id INTEGER,
	person_id INTEGER,
	observation_concept_id INTEGER,
	observation_concept_description VARCHAR(100),
	observation_concept_vocab VARCHAR(20),
	observation_date DATE,
	observation_type_concept_id INTEGER,
	observation_type_concept_description VARCHAR(50),
	value_as_concept_id INTEGER,
	value_as_concept_description VARCHAR(100),
	value_as_concept_vocab VARCHAR(20),
	obs_event_field_concept_id INTEGER,
	obs_event_field_concept_description VARCHAR(100),
	obs_event_field_concept_vocab VARCHAR(20),
	nomop_phase VARCHAR(10)
);

-- procedures
-- CREATE TABLE procedure_ocurrence(
-- 	procedure_occurrence_id INTEGER,
-- 	person_id INTEGER,
-- 	procedure_concept_id INTEGER,
-- 	procedure_concept_description VARCHAR(50),
-- 	procedure_concept_vocab VARCHAR(20),
-- 	procedure_date DATE,
-- 	procedure_end_date DATE,
-- 	procedure_type_concept_id INTEGER,
-- 	procedure_type_concept_description VARCHAR(50),
-- 	modifier_concept_id INTEGER,
-- 	modifier_concept_description VARCHAR(50),
--     modifier_concept_vocab VARCHAR(20)
-- );

-- specimen
CREATE TABLE specimen(
	specimen_id INTEGER,
	person_id INTEGER,
	specimen_concept_id INTEGER,
	specimen_concept_description VARCHAR(50),
	specimen_date DATE,
	specimen_concept_vocab VARCHAR(20),
	specimen_type_concept_id INTEGER,
	specimen_type_concept_description VARCHAR(50)
);

-- drugs
-- CREATE TABLE drugs(
-- 	drug_exposure_id INTEGER,
-- 	person_id INTEGER,
-- 	drug_concept_id INTEGER,
-- 	drug_concept_description VARCHAR(50),
-- 	drug_concept_vocab VARCHAR(20),
-- 	drug_exposure_start_date DATE,
-- 	drug_exposure_end_date DATE,
-- 	drug_type_concept_id INTEGER,
-- 	drug_type_concept_description VARCHAR(50)
-- );

-- CREATE TABLE death(
-- 	person_id INTEGER,
-- 	death_date DATE
-- );

