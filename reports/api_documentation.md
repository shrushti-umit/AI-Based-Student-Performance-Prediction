# API Documentation

## Base URL
http://localhost:5000

| Endpoint | Method | Purpose |
|----------|--------|---------|
| /predict | POST | Predict student performance |
| /students | GET | Retrieve student records |
| /upload-data | POST | Upload dataset |
| /clean-data | POST | Clean the uploaded dataset |
| /health | GET | Check if the server is running |

---

## Endpoint: /predict

### Method
POST

### Request

```json
{
  "attendance": 90,
  "study_hours": 6,
  "previous_grade": 78
}
```

### Response

```json
{
  "predicted_grade": 88,
  "status": "Success"
}
```

---

## Endpoint: /students

### Method
GET

### Response

Returns all student records.

---

## Endpoint: /upload-data

### Method
POST

### Response

Dataset uploaded successfully.

---

## Endpoint: /clean-data

### Method
POST

### Response

Dataset cleaned successfully.

---

## Endpoint: /health

### Method
GET

### Response

Server is running.
