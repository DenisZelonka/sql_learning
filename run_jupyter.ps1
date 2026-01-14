# Define the filename
$notebookFile = "db_create.ipynb"

# Check if the file exists; if not, create an empty one so Jupyter opens it directly
if (!(Test-Path $notebookFile)) {
    Write-Host "$notebookFile not found. Creating a new notebook file..." -ForegroundColor Yellow
    New-Item -ItemType File -Name $notebookFile
}

Write-Host "Launching Jupyter Notebook for $notebookFile..." -ForegroundColor Cyan

# Start jupyter and open the specific file in the browser
jupyter notebook $notebookFile
