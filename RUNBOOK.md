# Runbook — azure-cicd-demo (Render)

## Health
- GET /health → {"ok": true}
- Render dashboard should show "Healthy" (uses /health path if render.yaml is set)

##Logs (Render)
- Service → Logs (Build & Runtime)

## Common Issues
- **Build failed**: check Logs → Build tab (usually missing deps); ensure `requirements.txt` exists.
- **App crash**: verify start command `gunicorn -w 2 -b 0.0.0.0:$PORT app:app`.
- **404 /health**: ensure @app.route("/health") exists and latest commit is deployed.
- **Cold start delay**: free plan sleeps; first request wakes the app (a few seconds).

## Rollback
- GitHub → revert to previous commit on `main`
- Render auto-redeploys
- Confirm /health returns {"ok": true}

## Scaling (later)
- Switch plan to Starter/Plus in Render to remove sleep and increase resources.


## Tech
- Python 3.11, Flask, gunicorn
- GitHub Actions (CI)
- Render (free) deployment; Azure App Service workflow included

```
::contentReference[oaicite:0]{index=0}
```
