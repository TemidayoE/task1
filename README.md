# **HNG TASK1: NUMBER FACTS API**

This is a simple Django RESTAPI that returns fun facts about numbers thats inserted. The facts are generated from [Number API]("http:numbersapi/number"):
It supports **CORS** for cross-origin requests.
_____________________________________________________

## **SetUp Instructions**
### **1. Clone the repo**
```sh
git clone
https://github.com/TemidayoE/task.git
cd math_app
```

### **2. Create a venv & Install dependencies**
```sh
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```
### **3. Run Database migrations**
```sh
python manage.py migrate
```
### **4. Start the development server**
```sh
python manage.py runserver
```
_____________________________________________________
## **API Documentation**

### Endpoint
|Method|URL|Description|
|:----:|:-:|:---------:|
|GET | /api/classify-number/?number={num} | Returns something similar to the below JSON response |

### **Example JSON Response**
```json
{
  "number": 1000,
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "even"
  ],
  "digit_sum": 1,
  "fun_fact": "1000 is the number of elephants it took to bring in the material to build the Taj Mahal from various parts of India."
}
```
______________________________________________________

## **CORS Support**

By default, this API allows requests from all origins. You can modify that in **setting.py**
______________________________________________________
## **Contributing**
Fork the repo, make improvements and submit a pull request.
_______________________________________________________