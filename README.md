
# Eventify Application

Eventify is a Flask application that allows you to manage your events effortlessly.

## Requirements

- Docker (https://www.docker.com/products/docker-desktop/)
- Python 3.7+ (https://www.python.org/downloads/)

## Setup with Powershell

### Step 1: Clone the Repository

```
git clone https://github.com/dominikwiench/eventify.git
cd eventify
```

### Step 2: Start MySQL Database in Docker
The app.py contains configuration info that is needed in this step
```
docker run --name <name> -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=database -p 3306:3306 -d mysql:latest
```

### Step 3: Create the events Table

```
docker exec -it my-mysql mysql -u root -p
```
```
CREATE DATABASE IF NOT EXISTS eventify;
USE eventify;

CREATE TABLE events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    location VARCHAR(255) NOT NULL
);
```
### Step 4: Virtual Environment
To create a virtual environment you need to type:

```
python -m venv venv
```
Next, to activate it:
```
venv\Scripts\activate (Windows)
source venv/bin/activate (MacOS/Linux)
```

### Step 5: Install Flask and PyMySQL

```
pip install flask pymysql
```

### Step 6: Run the Flask Application
In order to access the app, type:

```
python app.py
```

### Step 8: Access the Application

Go to your browser and type below:

#### http://127.0.0.1:5000/ 

## Showcase
![projekt1](https://i.imgur.com/ShGWqyw.png)
![projekt2](https://i.imgur.com/AJDQ1nL.png)
![projekt3](https://i.imgur.com/PedEEED.png)






