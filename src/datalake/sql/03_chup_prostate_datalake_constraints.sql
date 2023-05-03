-- constraints
ALTER TABLE condition_occurrence ADD CONSTRAINT fpk_conditions_person_id FOREIGN KEY (person_id) REFERENCES person (person_id);
ALTER TABLE measurement ADD CONSTRAINT fpk_measurement_person_id FOREIGN KEY (person_id) REFERENCES person (person_id);
ALTER TABLE observation ADD CONSTRAINT fpk_observation_person_id FOREIGN KEY (person_id) REFERENCES person (person_id);
-- ALTER TABLE procedures ADD CONSTRAINT fpk_procedures_person_id FOREIGN KEY (person_id) REFERENCES patient (person_id);
-- ALTER TABLE drugs ADD CONSTRAINT fpk_drugs_person_id FOREIGN KEY (person_id) REFERENCES patient (person_id);