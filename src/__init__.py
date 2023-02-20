import os
from sqlalchemy import create_engine


engine = create_engine(os.getenv('DATALAKE_URL', 'postgresql://postgres:postgres@host.docker.internal:5432/CHUP_PROSTATE_DATALAKE'))
