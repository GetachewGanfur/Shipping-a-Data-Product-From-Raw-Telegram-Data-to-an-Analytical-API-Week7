# 📦 Shipping a Data Product: From Raw Telegram Data to an Analytical API Week7

 The project extracts and analyzes messages and images from Ethiopian medical-related Telegram channels, transforming them into actionable insights via an analytical API.

---

## 📌 Project Overview

- **Objective:** Build a robust data platform to answer business questions about Ethiopian medical products using public Telegram channel data.
- **Stack:** Python, PostgreSQL, Docker, Telethon, dbt, YOLOv8, FastAPI, Dagster
- **Key Features:**
  - Telegram scraping (messages + images)
  - Star schema modeling with dbt
  - Object detection on images (YOLOv8)
  - API exposing analytical insights
  - Full orchestration with Dagster

---



## 🗃️ Project Structure

```bash

├── data/
│   └── raw/
│       └── telegram_messages/YYYY-MM-DD/channel_name.json
├── dbt_project/
│   ├── models/
│   │   ├── staging/
│   │   ├── marts/
│   │   └── schema.yml
├── images/
│   └── raw/
├── api/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
├── orchestration/
│   └── dagster_job.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
````

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/GetachewGanfur/Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API-Week7.git
cd Shipping-a-Data-Product-From-Raw-Telegram-Data-to-an-Analytical-API-Week7
```

### 2. Set Up Environment Variables

Create a `.env` file:

```env
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
DATABASE_URL=postgresql://postgres:postgres@db:5432/kaimdb
```

> ✅ Make sure `.env` is added to `.gitignore`.

### 3. Run Docker Environment

```bash
docker-compose up --build
```

This will:

* Spin up a PostgreSQL database
* Build your Python environment

---

## 🚀 Running Each Component

### A. Telegram Data Scraping

```bash
python scripts/scrape_telegram.py
```

Scrapes messages and images from public channels and stores them in `data/raw/`.

---

### B. Load Raw JSON to PostgreSQL

```bash
python scripts/load_raw_to_db.py
```

Loads raw data from JSON into a raw table in PostgreSQL.

---

### C. dbt Transformations

```bash
cd dbt_project
dbt run
dbt test
```

Builds the staging and mart models using a star schema.

---

### D. YOLOv8 Object Detection

```bash
python scripts/yolo_detect.py
```

Detects objects in scraped images and stores results in `fct_image_detections`.

---

### E. Launch FastAPI Server

```bash
uvicorn api.main:app --reload
```

#### 📊 Key Endpoints

* `GET /api/reports/top-products?limit=10`
* `GET /api/channels/{channel}/activity`
* `GET /api/search/messages?query=paracetamol`


---

### F. Dagster Orchestration

Launch Dagster UI:

```bash
dagster dev
```

Run the full pipeline from scraping to enrichment via Dagster job.

---



---



## Environment Setup

1. Copy the example environment file and fill in your secrets:

   ```sh
   cp .env.example .env
   # Then edit .env to add your actual credentials
   ```

2. Build and start the services with Docker Compose:

   ```sh
   docker-compose up --build
   ```