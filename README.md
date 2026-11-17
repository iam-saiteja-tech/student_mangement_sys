# 🎓 Student Management System

EduTrack is a web-based Student Management System developed using **Python, FastAPI, SQLite, HTML, and CSS**. It provides a simple and user-friendly platform to manage student records efficiently.

The application allows users to add, view, update, and delete student information through an organized dashboard.

## 🚀 Features

- **Dashboard:** View all registered students.
- **Add Students:** Register new students with their details.
- **View Student Profile:** View individual student information.
- **Update Student Details:** Edit existing student records.
- **Delete Students:** Remove student records.
- **Student Information:** Manage name, age, gender, marks, course, profile image, and attendance status.
- **Responsive Design:** User-friendly interface for different screen sizes.
- **Database Integration:** Store student records using SQLite.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web framework |
| SQLite | Database |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| Jinja2 | Dynamic HTML templates |

## 📂 Project Structure

```text
EduTrack/
│
├── main.py
├── students.db
│
├── templates/
│   ├── home.html
│   ├── add-student.html
│   ├── update_std.html
│   └── single-std.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The structure above is a suggested layout. Adjust it to match your actual project files.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/iam-saiteja-tech/student-management-sys.git
```

### 2. Navigate to the Project Folder

```bash
cd student-management-sys
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open in Browser

```text
http://127.0.0.1:8000
```

## 📸 Screenshots

Add your project screenshots inside a folder named `screenshots`.

Example:

```text
screenshots/
├── dashboard.png
├── add-student.png
├── student-profile.png
└── update-student.png
```

You can display them in this section:

### Dashboard
<!-- Add dashboard screenshot here -->

### Add Student
<!-- Add add-student screenshot here -->

### Student Profile
<!-- Add profile screenshot here -->

### Update Student
<!-- Add update screenshot here -->

## 📚 What I Learned

While developing this project, I gained practical experience in:

- Building web applications using FastAPI.
- Creating GET and POST routes.
- Performing CRUD operations.
- Connecting Python applications with SQLite.
- Writing SQL queries.
- Using Jinja2 templates to display dynamic data.
- Handling HTML form submissions.
- Integrating frontend, backend, and database.
- Designing responsive user interfaces.
- Debugging and solving application errors.

## 🎯 Future Improvements

- User authentication and authorization.
- Search and filter students.
- Sort students by marks and name.
- Pagination for student records.
- Export student data to Excel or PDF.
- Admin dashboard with student statistics.
- Student performance analytics.

## 👨‍💻 Developer

**Saiteja**

GitHub: [@iam-saiteja-tech](https://github.com/iam-saiteja-tech)

---

⭐ If you find this project useful, consider giving it a star!

**EduTrack – Making Student Management Easier.**
