# Flask App Deployment on Kubernetes

This repository contains a simple Flask application that is deployed on a Kubernetes cluster using Minikube.

## Prerequisites

Before you begin, ensure you have the following installed:

- Git
- Docker
- Minikube
- kubectl

## Getting Started

git clone https://github.com/MelekBadreddine/simple-deployment.git

cd simple-deployment

Build the Docker image:

- docker build -t flask-app .

Start minikube:

- minikube start

Apply Kubernetes deployment and service configurations:

- kubectl apply -f deployment.yaml
- kubectl apply -f service.yaml

Get the Minikube IP and Port for accessing the service:

- minikube service flask-service --url

Cleaning Up
to stop the container and clean up resources:

Delete the Kubernetes deployment and service:

- kubectl delete -f deployment.yaml
- kubectl delete -f service.yaml

Stop Minikube:

- minikube stop

Optionally, delete the Minikube cluster:

- minikube delete
