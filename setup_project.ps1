Write-Host "Starting PostgreSQL..." -ForegroundColor Cyan
docker compose -f docker/docker-compose.yml up -d

Write-Host "Installing Python packages..." -ForegroundColor Cyan
pip install -r requirements.txt

Write-Host "Loading CSV files into PostgreSQL..." -ForegroundColor Cyan
python scripts/load_csv_to_postgres.py

Write-Host "Setup completed successfully!" -ForegroundColor Green
Write-Host "PostgreSQL is available at localhost:5434"
Write-Host "Database: nuclear_source"
Write-Host "User: nuclear_user"
Write-Host "Password: nuclear_password"
Write-Host "Schema: raw"