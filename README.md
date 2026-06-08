# kernreactor-data-engineering
Geïnspireerd door Emiel en ODC Noord

git clone https://github.com/Jyrar/kernreactor-data-engineering.git
cd kernreactor-data-engineering
powershell -ExecutionPolicy Bypass -File .\setup_project.ps1

dan

docker exec -it kernreactor_postgres psql -U nuclear_user -d nuclear_source

in terminal:

SET search_path TO raw;
\dt

als je tabellen ziet, is alles goed