# Vehicle Telemetry — DevOps Project

This project simulates automotive telemetry (speed, engine temp, battery, GPS, fuel) and sends it to a backend API.  
The backend stores the data in MongoDB.  
Everything runs inside Docker containers and can be deployed to Kubernetes.

---

## 🚗 Project Architecture

Simulator → API → MongoDB  
All running via Docker or Kubernetes.

---

## 📁 Project Structure

vehicle-telemetry/
├── api/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_api.py
│
├── telemetry-simulator/
│   ├── simulator.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/
│   ├── namespace.yml
│   ├── mongo-deployment.yml
│   ├── mongo-service.yml
│   ├── api-deployment.yml
│   ├── api-service.yml
│   └── simulator-job.yml
│
├── .github/
│   └── workflows/
│       ├── cicd.ym


---

## ▶️ Run Locally (Docker Compose)

```bash
docker compose up --build

**Check health:**

curl http://localhost:5000/health

**Get stored telemetry:**

curl http://localhost:5000/telemetry

**Monitor simulator logs:**

docker compose logs -f simulator

---------

**## ☸️ Deploy to Kubernetes**

kubectl apply -f k8s/
kubectl port-forward svc/api 5000:5000 -n vehicle-telemetry



└── README.md
