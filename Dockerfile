# --- Dockerfile for Market Earnings Monitoring System (Plotly Dash) ---
# Deploys to Google Cloud Run. Place this file in the root of your project,
# next to app.py and requirements.txt.

FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (better Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Cloud Run injects $PORT at runtime — do not hardcode 8050
ENV PORT=8080
EXPOSE 8080

# gunicorn serves the underlying Flask server Dash is built on.
# "app:server" means: in app.py, expose a variable called `server`
# (server = app.server) — this is required, Dash's dev server won't work here.
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 0 app:server