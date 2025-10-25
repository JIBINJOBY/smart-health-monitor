# Smart Health Monitoring Web App (DevOps Deployment)

A Flask-based web application that simulates and visualizes real-time health data such as heart rate, temperature, and oxygen level.  
The project is fully automated using Jenkins and Docker.

## Features
- Flask web server for simulated health metrics
- Docker containerization
- Jenkins CI/CD pipeline for build and deployment
- DockerHub integration

## How It Works
1. Jenkins pulls the source code from GitHub.
2. Jenkins builds the Docker image using the `Dockerfile`.
3. Jenkins pushes the image to DockerHub.
4. Jenkins deploys a running container automatically.

## Run Locally
```bash
docker build -t smart-health-monitor .
docker run -p 5000:5000 smart-health-monitor
