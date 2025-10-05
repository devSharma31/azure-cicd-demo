![CI](https://github.com/devSharma31/azure-cicd-demo/actions/workflows/ci.yml/badge.svg)

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


Deploy (Render – free, recommended now)

Render auto-builds from GitHub on push.

Build command
```
pip install -r requirements.txt
```

Start command
```
gunicorn -w 2 -b 0.0.0.0:$PORT app:app
```

You can also keep this as code with a render.yaml:
```
services:
  - type: web
    name: azure-cicd-demo
    env: python
    plan: free
    branch: main
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn -w 2 -b 0.0.0.0:$PORT app:app
    healthCheckPath: /health
```


## Deploy (Azure – when subscription is active)
1. Create a Resource Group and an **Azure App Service (Linux)** with a **Python** runtime (3.11 is fine).
2. In the Web App, go to **Deployment Center > FTPS credentials > Get Publish Profile** and **download** it.
3. On GitHub, go to **Settings > Secrets and variables > Actions > New repository secret** and add:
   - `AZURE_WEBAPP_PUBLISH_PROFILE`: Paste the entire XML from the publish profile.
   - `AZURE_WEBAPP_NAME`: Your web app name (e.g., `dev-azure-cicd-demo`).
4. Azure Web App → Configuration → General settings → Startup Command:
```
   gunicorn -w 2 -b 0.0.0.0:$PORT app:app
```
5. Push your code to `main`. The workflow in `.github/workflows/azure-webapp.yml` will deploy automatically.

## CI (GitHub Actions)
- Basic sanity workflow: .github/workflows/ci.yml
-checks out repo, installs deps, compiles app.py
-Badge at the top shows last CI status.
