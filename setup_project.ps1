Write-Host "Starting PostgreSQL..." -ForegroundColor Cyan
docker compose -f docker/docker-compose.yml up -d

Write-Host "Waiting for PostgreSQL..." -ForegroundColor Cyan
Start-Sleep -Seconds 10

Write-Host "Installing Python packages..." -ForegroundColor Cyan
pip install -r requirements.txt

Write-Host "Loading CSV files into PostgreSQL..." -ForegroundColor Cyan
python scripts/load_csv_to_postgres.py

Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host "Setup completed successfully!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
Write-Host ""
Write-Host "PostgreSQL:"
Write-Host "Host: localhost"
Write-Host "Port: 5434"
Write-Host "Database: nuclear_source"
Write-Host "User: nuclear_user"
Write-Host "Password: nuclear_password"
Write-Host "Schema: raw"