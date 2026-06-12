from fastapi import FastAPI, HTTPException,Path
from pydantic import BaseModel , Field
import json

app = FastAPI()

class Student_data(BaseModel):
    roll_no  : int = Field(gt=0,description="Roll Number Must Be Positve Integer")
    name : str
    course : str
    college : str
    phone_no : str



def readDB():
    try:
        with open("studentDb.json", 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []

def write_data(data:Student_data):
    with open('studentDb.json', 'w') as f:
        json.dump(data,f,indent=4)


@app.get("/")
def root():
   return {"message": "Student Dashboard"}

@app.get("/view-students")
def get_students():
    students_dta= readDB()
    return students_dta

@app.get("/students/{name}")
def get_student(name:str):
    students = readDB()
    for student in students:
        # print(student["name"])
        # print(name)
        if student["name"].lower() == name.lower():
            return student
    raise HTTPException(status_code=404,detail=f"Student named {name} Not Found in Database!")     

@app.post("/add-students")
def creatr_student(student_data : Student_data):
    students = readDB()
    new_student = student_data.dict()
    students.append(new_student)
    write_data(students)
    return {"message":"data updated","status":new_student}

@app.delete("/del-student/{student_id}")
def del_student(student_id:int):
    student_db = readDB()
    new_data = [i for i in student_db if i["roll_no"] != student_id]
    write_data(new_data)
    return {"sucess" :"Record Delete Sucessfully"} 

    

@app.put("/student/{roll_no}")
def update_data(roll_no:int, updated_data : Student_data):
    student_data = readDB()
    student_exsist = False
    for index , value in enumerate(student_data):
        if student_data[index]["roll_no"] == roll_no:
            student_exsist = True
            student_data[index] = updated_data.dict()
            break
    if not student_exsist:
        return {"message" : "Student Not Found"}
    write_data(student_data)
    return {"meaasge" : "Data Updated SucessFully!", "Updated Data" : updated_data}

@app.get("/course/{course_name}")
def filter_data_by_course(course_name : str = Path(description="Enter Course Name e.g - bca , mca , btech")):
    read_data = readDB()
    new_data = [data for data in read_data if data["course"].lower() == course_name.lower()]
    
    if not new_data:
        raise HTTPException(status_code = 404, detail = "Student not found")
    
    return new_data

@app.get("/search_student")
def search_student(course:str=None , college:str = None):
    new_data = readDB()
    if course:
        new_data = [data for data in new_data if data["course"].lower() == course.lower()]

    if college:
        new_data = [data for data in new_data if data["college"].lower() == college.lower()]

    if not new_data:
        raise HTTPException(status_code=404,detail="No Student Found!")
 
    return new_data