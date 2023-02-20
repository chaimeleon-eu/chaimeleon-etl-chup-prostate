-- primary keys
ALTER TABLE person ADD CONSTRAINT xpk_patient PRIMARY KEY (person_id);
ALTER TABLE condition_ocurrence ADD CONSTRAINT xpk_conditions PRIMARY KEY (condition_occurrence_id);
ALTER TABLE measurement ADD CONSTRAINT xpk_measurement PRIMARY KEY (measurement_id);
ALTER TABLE observation ADD CONSTRAINT xpk_observation PRIMARY KEY (observation_id);
-- ALTER TABLE procedures ADD CONSTRAINT xpk_procedures PRIMARY KEY (procedure_occurrence_id);
-- ALTER TABLE drugs ADD CONSTRAINT xpk_drugs PRIMARY KEY (drug_exposure_id);