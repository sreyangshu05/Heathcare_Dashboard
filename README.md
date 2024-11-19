# Healthcare Dashboard

A web-based application that allows users to submit their personal details and upload files. This project consists of a React frontend and a Flask backend to process and manage the data.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Frontend](#frontend)
  - [Installation and Running](#installation-and-running)
- [Backend](#backend)
  - [Installation and Running](#installation-and-running)
- [API Endpoints](#api-endpoints)
- [File Uploads](#file-uploads)

---

## Features

- User-friendly form with validation.
- Allows file uploads with specific formats.
- Backend for handling and saving uploaded data.

---

## Technologies Used

- **Frontend**: React, CSS
- **Backend**: Flask
- **Styling**: Responsive CSS with Flexbox and gradients
- **File Handling**: Flask with `werkzeug.utils`
- **Data Transfer**: RESTful API

---

## Setup Instructions

### Prerequisites

- Node.js and npm installed
- Python (3.8+) installed
- Virtual environment tools (`venv` or `virtualenv`)
- Git installed
- A browser for testing

---

## Frontend

### Installation and Running

1. Navigate to the `healthcare_dashboard` directory:
   ```bash
   cd healthcare_dashboard
   npm install
   npm start

- The application will open in the browser at http://localhost:3000.

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   python -m venv venv
   .\venv\Scripts\activate (For Windows)
   source venv/bin/activate (For MacOS)
   pip install flask werkzeug 
   python app.py

- The backend will run at http://localhost:5000.

## API Endpoints

### POST /upload
- Description: Handles file uploads and form submission.
- equest Payload: name (string): User's name, age (string): User's age, file (file): File to upload.
- Response: 200 OK: Form and file submitted successfully, 400 Bad Request: Missing or invalid fields/file.

## File Uploads

- Allowed file formats: Images: .png, .jpg, .jpeg, .gif , Documents: .pdf, .txt
- Uploaded files are stored in the uploads directory.
