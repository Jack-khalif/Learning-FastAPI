
## Student Management API (FastAPI)

This is a beginner-friendly FastAPI project that demonstrates how to build a simple RESTful API to manage student data. The API supports basic CRUD operations (Create, Read, Update, Delete) using in-memory storage.

![FastAPI Screenshot](FastAPI.png)

---

### Features

* `GET /` — Root endpoint returns a simple welcome message.
* `GET /get-students/{student_id}` — Get a student by ID (path parameter with validation).
* `GET /get-by-name/` — Get a student by name using a **query parameter**.
* `GET /get-by-name/{student_id}` — Combine path and query parameters to fetch a student.
* `POST /create-student/{student_id}` — Create a new student using a path param and request body.
* `PUT /update-student/{student_id}` — Update an existing student with optional fields.
* `DELETE /delete-student/{student_id}` — Delete a student by ID.

---

###  Technologies Used

* Python 3.13
* [FastAPI](https://fastapi.tiangolo.com/)
* Pydantic for data validation
* Uvicorn as the ASGI server

---

###  Screenshot

> 📎 `FastAPI.png` — Shows the interactive Swagger UI documentation at `/docs`

---

### Installation & Usage

1. **Clone the repository**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Install dependencies**

```bash
pip install fastapi uvicorn
```

3. **Run the server**

```bash
uvicorn myapi:app --reload
```

4. **Access the API docs**

* Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

---

