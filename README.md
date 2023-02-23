# chaimeleon-etl-chup-prostate

## Deploy notes

1. Clone the repository
```sh
git clone https://github.com/chaimeleon-eu/chaimeleon-etl-chup-prostate.git
``` 
2. Initialize the submodule
```sh
git submodule init
git submodule update
```
3. Download/copy xlsx and csv files on data folder (./data).
4. Deploy datake database running below command:
```sh
make deploy_datalake
```
5. Now, you can run ETL in two ways:

   5.1 Running the two dataflows at once:
    ```sh
    make etl_chup_prostate
    ```
   
   5.2 Or running dataflows in several process:
    ```sh
    make etl_chup_prostate_datalake
    make etl_chup_prostate_indexa
    ```
6. Check everything is okay querying data on indexa database and/or seeing outputs from above commands.
7. Stop and remove datalake container.
```sh
make down
```
8. Retrieve xml files from outputs folder.

## Software dependencies
* Docker (tested version: **20.10.17, build 100c701**).
* docker-compose (tested version: **1.29.2, build 5becea4c**).
* make (tested version: **GNU Make 4.2.1**).
