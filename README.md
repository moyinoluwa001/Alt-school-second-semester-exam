# Name: Ogunwale Abdulrahmon Ajibola
# ID: ALT/SOE/025/1331
# Track: Backend Engineering (Python)

# EduTrack Lite API

EduTrack Lite API is a lightweight FastAPI-based application designed to manage users, courses, and enrollments. It provides endpoints for CRUD operations and includes validation logic to ensure data integrity.

## Features
- **User Management**: Create, retrieve, update, deactivate, and delete users.
- **Course Management**: Create, retrieve, update, and delete courses.
- **Enrollment Management**: Enroll users in courses and manage enrollment details.
- **Validation**: Ensures data consistency and integrity.
- **Testing**: Includes test cases for all endpoints.

## Requirements
- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- HTTPX
- Python-dotenv

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd EduTrack-lite-API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/docs
   ```
   This will open the interactive API documentation (Swagger UI).

## Running Tests
Run the test suite using Pytest:
```bash
pytest
```

## Project Structure
```
EduTrack-lite-API/
├── main.py                # Entry point of the application
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignore file
├── routes/                # API route definitions
├── schemas/               # Pydantic schemas
├── services/              # Business logic
├── tests/                 # Test cases
```

## License
This project is licensed under the MIT License.