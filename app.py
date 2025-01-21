from flask import Flask, jsonify, request, abort
import pandas as pd

app = Flask(__name__)
#loading the csv dataset
employees_data = pd.read_csv("data.csv")

##Basic GET Endpoint
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees_data.to_dict(orient="records"))

#Query Parameter Filtering
@app.route("/employees/filter", methods=['GET'])
def filter_employees():
    department = request.args.get("department")
    country = request.args.get("country")
    filtered_employees = employees_data
    if department:
        filtered_employees = filtered_employees[filtered_employees["department"] == department]
    if country:
        filtered_employees = filtered_employees[filtered_employees["country"] == country]
    return jsonify(filtered_employees.to_dict(orient="records"))

##GET by ID
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee_by_id(employee_id):
    """returns employee based on id"""
    employee = employees_data[employees_data["employee_id"]==employee_id]
    if employee.empty:
        abort(404, description="Employee not Found")
    return jsonify(employee.iloc[0].to_dict())

#Aggregations via API
@app.route("/summary/department", methods=["GET"])
def departmental_summary():
    """returns summary for each departemnt(average salary and average performance score)"""
    summary = employees_data.groupby("department").agg(avarage_salary=("salary","mean"),
                                                       avarage_performance_score=("performance_score","mean")).reset_index()
    return jsonify(summary.to_dict(orient="records"))

##Performance Score Leaderboard
@app.route("/top-performers/<int:n>", methods=["GET"])
def performance_leaderboard(n):
    """returns top n employess by perfomance_score"""
    sorted_employees = employees_data.sort_values(by=["performance_score","salary"], ascending=[False, False]).head(n)
    return jsonify(sorted_employees.to_dict(orient="records"))

if __name__=="__main__":
    app.run(debug=True)
