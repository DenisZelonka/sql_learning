# 1. Install Python using Winget
Write-Host "Installing Python..." -ForegroundColor Cyan
winget install -e --id Python.Python.3 --scope machine

# 2. Refresh environment variables so the current session sees 'python'
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# 3. Upgrade pip to the latest version
Write-Host "Upgrading pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip

# 4. Install IPython, Jupyter, and Pandas
Write-Host "Installing IPython, Jupyter, and Pandas..." -ForegroundColor Cyan
pip install ipython jupyter pandas

Write-Host "Setup complete!" -ForegroundColor Green
