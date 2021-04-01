# The Atlantic API

A simple API built in Django accepting JSON and storing it in a SQLite database in order to copy over the information and update it as needed.

## Setting up and Running the code
- `git clone` this repo or download the repo locally
- From bash shell/terminal, navigate inside the project root directory and start up a virtual environment. 
	- I use `virtualenv`, so after installation, run `virtualenv env` to create the virtual environment.
	- Then, inside the project root directory, run `source env/bin/activate` to activate
- Navigate one level deeper inside the `main_app` directory. Run `pip install -r requirements.txt` to install all dependencies.
- Run `python manage.py makemigrations` and then run `python manage.py migrate` to set up the database.
- Run `python manage.py runserver` to start the server.

## Testing the application
- Make sure the server is started. Run `python manage.py runserver` to start the server.
- Use postman to send information to the following routes. Make sure in the Body tab of your request, you select `raw` and `JSON` from the dropdown menu.
	- For submitting: http://127.0.0.1:8000/submit/
	- For updating: http://127.0.0.1:8000/update/
- You can use the following test case inside the Body tab of your Postman request and adjust accordingly for the route.
```
{
  "customer": {
    "id": "b73b8b0e-0240-42a9-874c-00445d51dd8a",
    "first_name": "Ernest",
    "last_name": "Hemingway",
    "address_1": "907 Whitehead St",
    "address_2": "",
    "city": "Key West",
    "state": "FL",
    "postal_code": "33043",
    "subscription": {
      "id": "eac8709f-d898-42f0-84d8-a1997c25cae9",
      "plan_name": "print & digital",
      "price": "5999"
    },
    "gifts": [
      {
        "id": "53368db4-6097-49c6-ba8b-b00ab4a3ce3b",
        "plan_name": "digital",
        "price": "4999",
        "recipient_email": "mark@twain.com"
      },
      {
        "id": "fb7a077b-928f-4d44-a2e5-6969c72d3b45",
        "plan_name": "digital",
        "price": "4999",
        "recipient_email": "jane@austin.com"
      }
    ]
  }
}
```
## Schema
#### Subscription
| Column  | Type |
| ------------- |:-------------:|
| id      | Char     |
| plan_name     | Text|
| price      | Integer|
#### Customers
| Column  | Type |
| ------------- |:-------------:|
| id      | Char     |
| first_name     | Text|
| last_name     | Text|
| address_1      | Text|
| address_2      | Text|
| city      | Text|
| state      | Text|
| postal_code      | Text|
| Subscription     | Foreign Key|
#### Gifts
| Column  | Type |
| ------------- |:-------------:|
| id      | Char     |
| plan_name     | Text|
| price      | Integer|
| recipient_email      | Email Field|
| Customer      | Foreign Key|

## Final Thoughts
I was able to accomplish the main functionalities of the app, but wasn't really able to hit any of the bonuses. Some further extensions of the app I'd like to implement would testing and error handling, along with some read endpoints. 