# Hello Wissen Service

Flask REST API that returns the greeting "hello wissen" via a GET endpoint.

## Endpoint

- `GET /api/greeting`
   - Response: `{"message": "hello wissen"}` with HTTP 200

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask development server:
   ```bash
   python app.py
   ```
3. Access the endpoint at `http://localhost:5000/api/greeting`.

## Running with Docker

```bash
# Build the image
docker build -t hello-wissen-service .

# Run the container
docker run -p 5000:5000 hello-wissen-service
```

## Testing

```bash
pytest tests/
```
