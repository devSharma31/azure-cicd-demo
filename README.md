# Azure CI/CD Demo – Flask on Azure App Service

This repo is a **Day 1** DevOps portfolio project: a tiny Flask app deployed to **Azure App Service** via **GitHub Actions**.

## What this shows
- Basic **Python/Flask** web app
- **CI/CD** with GitHub Actions
- Automatic deploys to **Azure App Service (Linux, Python)** on every push to `main`

## Local run
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py  # http://127.0.0.1:8000
```

## Azure setup (one-time)
1. Create a Resource Group and an **Azure App Service (Linux)** with a **Python** runtime (3.11 is fine).
2. In the Web App, go to **Deployment Center > FTPS credentials > Get Publish Profile** and **download** it.
3. On GitHub, go to **Settings > Secrets and variables > Actions > New repository secret** and add:
   - `AZURE_WEBAPP_PUBLISH_PROFILE`: Paste the entire XML from the publish profile.
   - `AZURE_WEBAPP_NAME`: Your web app name (e.g., `dev-azure-cicd-demo`).
4. Push your code to `main`. The workflow in `.github/workflows/azure-webapp.yml` will deploy automatically.

## GitHub Actions workflow
See `.github/workflows/azure-webapp.yml`.