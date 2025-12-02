# backend/seed.py
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client['attendoDB']

# Insert sample teacher
db.teachers.insert_one({
    "teacher_id": "T001",
    "name": "Prof. Shreya",
    "email": "shreya@college.com",
    "password": "password-hash",
    "department": "Computer Science",
    "created_at": datetime.utcnow()
})

# Insert sample students
db.students.insert_many([
    {"student_id":"S001","name":"Amol Mankar","email":"amol@student.com","roll_no":"MCA2025-001","class_name":"MCA I","created_at":datetime.utcnow()},
    {"student_id":"S002","name":"Rohan Patil","email":"rohan@student.com","roll_no":"MCA2025-002","class_name":"MCA I","created_at":datetime.utcnow()}
])
print("Seeded sample data.")
