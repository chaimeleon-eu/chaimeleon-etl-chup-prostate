include .env
export DATALAKE_URL=postgresql://${DB_USER_DATALAKE}:${DB_PASS_DATALAKE}@${DB_HOST_DATALAKE}:${DB_PORT_DATALAKE}/${DB_NAME_DATALAKE}
export CANCER_TYPE=${TYPE}
clean:
	docker-compose down -v --rmi all
	rm -rf outputs/patient_*
	docker rmi chaimeleon-etl-chup-datalake:latest || true
	docker rmi chaimeleon-etl-chup-indexa:latest || true
deploy_datalake:
	docker-compose up -d datalake
etl_chup_prostate:
	docker-compose up --build etl_chup_datalake
	docker-compose up --build etl_chup_indexa
	docker-compose rm -f etl_chup_datalake etl_chup_indexa
	docker rmi chaimeleon-etl-chup-datalake:latest chaimeleon-etl-chup-indexa:latest || true
etl_chup_prostate_datalake:
	docker-compose up --build etl_chup_datalake
	docker-compose rm -f etl_chup_datalake
	docker rmi chaimeleon-etl-chup-datalake:latest || true
etl_chup_prostate_indexa:
	docker-compose up --build etl_chup_indexa
	docker-compose rm -f etl_chup_indexa
	docker rmi chaimeleon-etl-chup-indexa:latest || true
down:
	docker-compose down -v --rmi all