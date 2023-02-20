# chaimeleon-etl-chup_prostate

## Deploy notes

1. Download/copy xlsx and csv files on data folder (./data).
2. Deploy datake database running below command:
```sh
make deploy_datalake
```
3. Now, you can run ETL in two ways:

   3.1 Running the two dataflows at once:
    ```sh
    make etl_chup_prostate
    ```
   
   3.2 Or running dataflows in several process:
    ```sh
    make etl_chup_prostate_datalake
    make etl_chup_prostate_indexa
    ```
4. Check everything is okay querying data on indexa database and/or seeing outputs from above commands.
5. Stop and remove datalake container.
```sh
make down
```
6. Retrieve xml files from outputs folder.

## Software dependencies
* Docker (tested version: **20.10.17, build 100c701**).
* docker-compose (tested version: **1.29.2, build 5becea4c**).
* make (tested version: **GNU Make 4.2.1**).
