from flask import Flask, jsonify, request
from student import Student

app = Flask(__name__)
students = {}


@app.route("/student", methods=["POST"])
def create():
    data = request.json
    name = data["name"]
    age = data["age"]
    major = data["major"]
    gender = data["gender"]
    id = str(data["id"])
    student = Student(name, age, gender, major, id)
    students[id] = student
    return jsonify(student.dict()), 202


@app.route("/student/<id>", methods=["GET"])
def read(id):
    student = students.get(id)
    if student:
        return jsonify(student.dict()), 202
    else:
        return jsonify({"msg": "Student is not found"}), 404


@app.route("/student/<id>", methods=["DELETE"])
def delete(id):
    student = students.get(id)
    if student:
        student1 = students.pop(id)
        return (student1.dict()), 202
    else:
        return jsonify({"msg": "The student is not found"}), 404


@app.route("/student/<id>", methods=["PUT"])
def update(id):
    data = request.json
    student = students.get(id)
    print(students)
    if student:
        student.age = data["age"]
        student.major = data["major"]
        return jsonify(student.dict()), 202
    else:
        return jsonify({"msg": "The student is not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=8000)
