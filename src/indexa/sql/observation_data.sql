select
    observation_id,
    person_id,
    observation_concept_id,
    observation_concept_description,
    observation_concept_vocab,
    observation_date,
    observation_type_concept_id,
    observation_type_concept_description,
    value_as_concept_id,
    value_as_concept_description,
    value_as_concept_vocab,
    obs_event_field_concept_id,
    obs_event_field_concept_description,
    obs_event_field_concept_vocab,
    nomop_phase
from observation
;