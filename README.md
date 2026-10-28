# Cloud FinOps Dashboard API

A production-ready, containerized microservice built for real-time cloud resource auditing, cost-optimization, and infrastructure spend visibility. Designed with a **$0/card-free architecture** pattern suitable for modern SRE portfolios.

---

## 🚀 Problem Statement & Solution

### The Problem
Modern multi-cloud environment suffer from unchecked cost sprawl, idle virtual machines, and unoptimized resource allocations (e.g., over-provisioned Kubernetes nodes and underutilized cloud instances), leading to inflated monthly infrastructure bills.

### The Solution
This API provides an automated auditing engine that scans cloud infrastructure, identifies waste patterns (such as oversized VM instances or idle clusters), and generates actionable cost-saving recommendations through a high-performance FastAPI interface backed by serverless PostgreSQL storage.

---

## 🛠️ Tech Stack & Architecture

* **Backend Framework:** FastAPI (Asynchronous Python)
* **ORM & Database:** SQLAlchemy, PostgreSQL (Hosted on Neon Serverless with SSL enforcement)
* **Containerization:** Docker & Docker Compose (Multi-layer optimized builds)
* **Infrastructure as Code (IaC):** Terraform (Zero-cost cloud resource provisioning)
* **Environment Management:** Native `.env` mapping and configuration security

---

## ⚙️ Getting Started & Local Development

### Prerequisites
* [Docker Desktop](https://www.docker.com/) installed and running
* Git

### 1. Clone the Repository
```bash
git clone [https://github.com/shazam-25/cloud-audit-dashboard.git](https://github.com/shazam-25/cloud-audit-dashboard.git)
cd sre-finops-dashboard
```
--- 

## 📂 Project Structure
├── main.py              # FastAPI application entrypoint and DB models
├── Dockerfile           # Optimized Python slim container configuration
├── docker-compose.yml   # Local orchestration and environment mapping
├── requirements.txt     # Python runtime dependencies
├── .dockerignore        # Excludes local artifacts from container build
└── .env                 # Local secrets (git-ignored)

---

## 🔒 Security Principles

* **Zero Trust Secret Injection:** Credentials are injected purely at runtime via environment files and never hardcoded.
* **Secure Transport:** Enforces strict SSL/TLS handshake configurations (sslmode=require) for database communication over public networks.
* **Lightweight Footprint:** Built using multi-stage/slim container images to minimize attack surface and resource consumption.