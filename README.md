 In this code we are using AWS EC2 services and Python as a language. 

1. Need to create a python environment.

2. Create app.py file.

3. In this file we are creating for Groceries. Here we will be using to test our API using tools like POSTMAN. 

4. In POSTMAN we used four HTTP request operations such as GET , POST, PUT and DELETE.

5. Here we using FLASK as a python framework.

6. For Storing our data we are using SQLite


from app import app, db, Grocery

app_context = app.app_context()
  
app_context.push()

db.drop_all()

db.create_all()
 
Grocery = Grocery(item="Sugar", price=35, quantity=2, customer_rating= 8.5)

db.session.add(Grocery)

db.session.commit() 

flask run --host private ip --port 5000 --debug


PUT-

![Capture3](https://github.com/vishalcj/API-for-Grocery-List-using-Flask-and-SQLite/assets/101442389/aea8959f-7bcc-45a9-bb3e-a96de476d1a3)

POST-

![Capture2](https://github.com/vishalcj/API-for-Grocery-List-using-Flask-and-SQLite/assets/101442389/f9b30d07-3655-4364-b947-66625cc6824d)

GET-

![Capture1](https://github.com/vishalcj/API-for-Grocery-List-using-Flask-and-SQLite/assets/101442389/6c3a1df8-2806-4089-a9ec-d6db138bedd5)

DELETE-

![Capture4](https://github.com/vishalcj/API-for-Grocery-List-using-Flask-and-SQLite/assets/101442389/46b40356-e84c-4e94-8ba3-ae0b7bd05ca0)
