
## Endpoints

### 1. **Get All Employees**
- **URL**: `/employees`
- **Method**: `GET`
- **Description**: Returns a list of all employees.
- **Response**: A list of employee records.
- **Example Response**:
    ```json
   [
    {
        "age": 23,
        "country": "USA",
        "department": "Engineering",
        "employee_id": 1,
        "name": "Employee 1",
        "performance_score": 2,
        "salary": 43469,
        "years_of_experience": 1
    },
    {
        "age": 24,
        "country": "Canada",
        "department": "Marketing",
        "employee_id": 2,
        "name": "Employee 2",
        "performance_score": 3,
        "salary": 43792,
        "years_of_experience": 2
    }
    ]
    ```

### 2. **Filter Employees by Department and/or Country**
- **URL**: `/employees/filter`
- **Method**: `GET`
- **Query Parameters**:
  - `department` (optional): The department to filter by.
  - `country` (optional): The country to filter by.
- **Description**: Filters the list of employees based on the given query parameters.
- **Example Request**:
    ```
    GET /employees/filter?department=HR&country=Canada
    ```
- **Example Response**:
    ```json
    [
       {
        "age": 38,
        "country": "Canada",
        "department": "HR",
        "employee_id": 16,
        "name": "Employee 16",
        "performance_score": 2,
        "salary": 48314,
        "years_of_experience": 16
    }
    ]
    ```

### 3. **Get Employee by ID**
- **URL**: `/employees/{employee_id}`
- **Method**: `GET`
- **URL Parameters**:
  - `employee_id` (required): The ID of the employee to retrieve.
- **Description**: Returns data for a specific employee identified by `employee_id`.
- **Example Request**:
    ```
    GET /employees/1
    ```
- **Example Response**:
    ```json
    {
    "age": 27,
    "country": "Germany",
    "department": "Marketing",
    "employee_id": 200,
    "name": "Employee 200",
    "performance_score": 1,
    "salary": 107746,
    "years_of_experience": 14
    }
    ```

### 4. **Summary of Employees by Department**
- **URL**: `/summary/department`
- **Method**: `GET`
- **Description**: Returns the average salary and performance score per department.
- **Example Response**:
    ```json
   [
    {
        "avarage_performance_score": 3.0588235294117645,
        "avarage_salary": 75446.0,
        "department": "Engineering"
    },
    {
        "avarage_performance_score": 2.909090909090909,
        "avarage_salary": 75769.0,
        "department": "Finance"
    }
    ]
    ```

### 5. **Top n Performers**
- **URL**: `/top-performers/{n}`
- **Method**: `GET`
- **URL Parameters**:
  - `n` (required): The number of top performers to retrieve.
- **Description**: Returns the top N employees sorted by performance score (with salary as a tiebreaker).
- **Example Request**:
    ```
    GET /top-performers/3
    ```
- **Example Response**:
    ```json
    [
      
    {
        "age": 26,
        "country": "UK",
        "department": "Engineering",
        "employee_id": 199,
        "name": "Employee 199",
        "performance_score": 5,
        "salary": 107423,
        "years_of_experience": 13
    },
    {
        "age": 60,
        "country": "France",
        "department": "Marketing",
        "employee_id": 194,
        "name": "Employee 194",
        "performance_score": 5,
        "salary": 105808,
        "years_of_experience": 8
    }
    ]
    ```

## Running the App

To run the Flask app locally, follow these steps:

1. Install dependencies:
pip install -r requirements.txt
    

2. Start the app:

    
    python app.py
   

The app will be running at `http://127.0.0.1:5000`.

## Done By
## BLESSED ZHOU
