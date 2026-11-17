from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3
from pydantic import BaseModel

class students(BaseModel):
    name : str
    age : int
    gender : str
    marks : int
    courese : str
    image : str
    status : str

def get_connection():
    connection = sqlite3.connect(
        "students.db"
    )
    return connection
get_connection()



templates = Jinja2Templates(
    directory="templates"
)

app = FastAPI()

def create_table():
    connection = get_connection()
    course = connection.cursor()
    q = """
        CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        marks INTEGER,
        courese TEXT,
        image TEXT,
        status INTEGER
        )
        """
    course.execute(q)
    connection.commit()
    connection.close()

create_table()


@app.get("/")
def get_studs(req:Request):
    connection = get_connection()
    cursor = connection.cursor()

    q = "select * from students"
    cursor.execute(q)
    students = cursor.fetchall()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"students": students}
    )

@app.get("/students/single-std/{std_id}")
def single_std(req:Request,std_id:int):
    connection = get_connection()
    course = connection.cursor()
    q = "select * from students where id=?"
    course.execute(q, (std_id,))
    students = course.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={
            "student": students
        }
    )

@app.get("/students/add")
def add_stud(req : Request):
    return templates.TemplateResponse(
        request=req,
        name="add-student.html",
        context={}
    )

@app.post("/students/add")
def add_student(
    name = Form(),
    age = Form(),
    gender = Form(),
    marks = Form(),
    courese = Form(),
    image = Form(),
    status = Form(),
):

    student = students(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        courese=courese,
        image=image,
        status=status
    )

    values = (student.name, student.age, student.gender, student.marks, student.courese, student.image, student.status)
    connection = get_connection()
    cursor = connection.cursor()
    q = """
        INSERT INTO students(name,age,gender,marks,courese,image,status)
        values(?,?,?,?,?,?,?)
        """
    cursor.execute(q, values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/" , status_code=303)

@app.get("/students/delete/{std_id}")
def delete (std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    q = "delete from students where id=?"
    cursor.execute(q, (std_id,))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/" , status_code=303)

@app.get("/students/update/{std_id}")
def update(req:Request,std_id:int):
    connection = get_connection()
    cursor  = connection.cursor()
    q = "select * from students where id=?"
    cursor.execute(q,(std_id,))
    student = cursor.fetchone()
    connection.close
    print(student)

    return templates.TemplateResponse(
        request=req,
        name="update_std.html",
        context={"std":student}
    )

@app.post("/students/update/{std_id}")
def std_update(std_id:int,
    name = Form(),
    age = Form(),
    gender = Form(),
    marks = Form(),
    courese = Form(),
    image = Form(),
    status = Form(),
):

    student = students(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        courese=courese,
        image=image,
        status=status
    )

    values = (student.name, student.age, student.gender, student.marks, student.courese, student.image, student.status)
    connection = get_connection()
    cursor = connection.cursor()
    q = """
        UPDATE students SET name=?,age=?,gender=?,marks=?,courese=?,image=?,status=? WHERE id=?
        """
    values=(name,age,gender,marks,courese,image,status,std_id)
    cursor.execute(q, values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/" , status_code=303)
