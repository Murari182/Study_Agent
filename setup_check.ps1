<#
.\setup_check.ps1 - Verify Study Agent setup (PowerShell)
#>

Set-StrictMode -Version Latest

Write-Host "================================"
Write-Host "Study Agent Setup Verification"
Write-Host "================================`n"

$checks_passed = 0
$checks_failed = 0

function Test-Command {
    param([string]$cmd)
    $found = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($found) {
        Write-Host "✓ $cmd is installed" -ForegroundColor Green
        $script:checks_passed++
    } else {
        Write-Host "✗ $cmd is not installed" -ForegroundColor Red
        $script:checks_failed++
    }
}

function Test-PythonPackage {
    param([string]$pkg)
    try {
        python -c "import $pkg" 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Python package '$pkg' is available" -ForegroundColor Green
            $script:checks_passed++
        } else {
            throw
        }
    } catch {
        Write-Host "✗ Python package '$pkg' is missing" -ForegroundColor Red
        $script:checks_failed++
    }
}

Write-Host "Checking System Requirements..."
Test-Command "python"
Test-Command "node"
Test-Command "npm"

Write-Host "`nChecking Backend Virtual Environment..."
if (Test-Path "backend\.venv") {
    Write-Host "✓ Virtual environment exists at backend/.venv" -ForegroundColor Green
    $checks_passed++
} else {
    Write-Host "✗ Virtual environment not found. Run: cd backend; python -m venv .venv" -ForegroundColor Red
    $checks_failed++
}

Write-Host "`nChecking Backend Dependencies..."
if (Test-Path "backend") {
    Push-Location backend
    if (Test-Path ".venv\Scripts\Activate.ps1") {
        Write-Host "Sourcing virtualenv activation script..."
        # Do not auto-activate in this script to avoid side effects; just test packages
        Test-PythonPackage "fastapi"
        Test-PythonPackage "langchain"
        Test-PythonPackage "google"
        Test-PythonPackage "pydantic"
        Test-PythonPackage "faiss"
    } else {
        Write-Host "Virtualenv activation script not found; run: cd backend; python -m venv .venv; .\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow
    }
    Pop-Location
} else {
    Write-Host "backend/ directory not found" -ForegroundColor Red
    exit 1
}

Write-Host "`nChecking Configuration Files..."
if (Test-Path "backend\.env") {
    Write-Host "✓ backend/.env exists" -ForegroundColor Green
    $checks_passed++
} else {
    Write-Host "⚠ backend/.env not found. Copy from .env.example and add API keys" -ForegroundColor Yellow
}

if (Test-Path ".env.example") {
    Write-Host "✓ .env.example template found" -ForegroundColor Green
    $checks_passed++
} else {
    Write-Host "✗ .env.example template not found" -ForegroundColor Red
    $checks_failed++
}

if (Test-Path ".gitignore") {
    Write-Host "✓ .gitignore exists" -ForegroundColor Green
    $checks_passed++
} else {
    Write-Host "⚠ .gitignore not found" -ForegroundColor Yellow
}

Write-Host "`nChecking Frontend..."
if (Test-Path "frontend\package.json") {
    Write-Host "✓ frontend/package.json exists" -ForegroundColor Green
    $checks_passed++
} else {
    Write-Host "✗ frontend/package.json not found" -ForegroundColor Red
    $checks_failed++
}

if (Test-Path "frontend\node_modules") {
    Write-Host "✓ frontend dependencies installed" -ForegroundColor Green
    $checks_passed++
} else {
    Write-Host "⚠ frontend/node_modules not found. Run: cd frontend; npm install" -ForegroundColor Yellow
}

Write-Host "`n================================"
Write-Host "Results: $checks_passed passed, $checks_failed failed"
Write-Host "================================`n"

if ($checks_failed -eq 0) {
    Write-Host "✓ All checks passed! You're ready to go." -ForegroundColor Green
    Write-Host "`nNext steps:"
    Write-Host "1. Configure API keys: edit backend/.env and add GOOGLE_API_KEY or OPENAI_API_KEY"
    Write-Host "2. Start backend (PowerShell):"
    Write-Host "   cd backend; .\.venv\Scripts\Activate.ps1; uvicorn main:app --reload"
    Write-Host "3. Start frontend (PowerShell):"
    Write-Host "   cd frontend; npm run dev"
} else {
    Write-Host "✗ Some checks failed. Please fix the issues above." -ForegroundColor Red
}
