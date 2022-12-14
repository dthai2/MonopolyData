This project was implemented using postgreSQL and connecting the database to our application using Flask.

## Getting Started

A couple things are needed before being able to launch the web application. 
To meet all of the prerequisties and successfully launch the web application, you might need to follow one, or all, of the tutorials linked below.

[Install and Setup Python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-22-04-server)

[Install Flask to Create a Web Application](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3)

[Install PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04)

Once everything above is met, you can being using the web application we've created.

## Using the Web Application
For more insight on the steps being described below, you may find it useful to follow [this](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application) tutorial first to get a better understanding of how to connect the database to Flask and have your environment set up for success.

###### Creating the PostgreSQL Database and User
  1. Open terminal then type `sudo -iu postgres psql` to open PostgreSQL
  2. In PostgreSQL type `CREATE DATABASE monopoly;` to create a new database called 'monopoly'
  3. `CREATE USER monopoly WITH PASSWORD 'password';` to create a new user
  4. `GRANT ALL PRIVILEGES ON DATABASE monopoly TO monopoly;` to grant the user administrative access
  5. `\q` to exit PostgreSQL

###### Setting Up the Database
  1. Download the zip file of all the code found here, and move the decompressed folder to the correct location where you have set up your environment. Within that directory, switch into the directory of the file you just downloaded and moved.
  2. Open terminal then type `python init_db.py`. This step will insert all of the tables and data from the init_db file into the 'monopoly' database that you just created.
  3. Run flask with the command `flask run` to launch the application. Your output should provide you with a URL that says "Running on: " before the URL is displayed. You can copy that URL and paste it into your browser.
  4.  From here, you can navigate that web application and use it how you wish.
