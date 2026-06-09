Write-Host "Starting services..." -ForegroundColor Cyan
docker compose up -d

Write-Host "Waiting for PostgreSQL..." -ForegroundColor Cyan
Start-Sleep -Seconds 15

Write-Host "Installing Python packages..." -ForegroundColor Cyan
pip install -r requirements.txt

Write-Host "Loading CSV files into PostgreSQL (optional bootstrap)..." -ForegroundColor Cyan
$env:RAW_DATA_PATH = Join-Path $PSScriptRoot "..\data"
python (Join-Path $PSScriptRoot "scripts\load_csv_to_postgres.py")

Write-Host ""
Write-Host "==================================" -ForegroundColor Green
Write-Host "Setup completed successfully!" -ForegroundColor Green
Write-Host "==================================" -ForegroundColor Green
Write-Host ""
Write-Host "PostgreSQL:"
Write-Host "  Host: localhost"
Write-Host "  Port: 5434"
Write-Host "  Database: nuclear_source"
Write-Host "  User: nuclear_user"
Write-Host "  Password: nuclear_password"
Write-Host "  Schema: raw"
Write-Host ""
Write-Host "Airflow:"
Write-Host "  URL: http://localhost:8081"
Write-Host "  User: admin"
Write-Host "  Password: admin"
Write-Host "  DAG: load_raw_nuclear_data (trigger manually or on schedule)"
