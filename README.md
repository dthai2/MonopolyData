This project was implemented using postgre and connecting the database to our application using Flask.

## Getting Started

A couple things are needed before being able to launch the web application. 
To meet all of the prerequisties and successfully launch the web application, you might need to follow one, or all, of the tutorials linked below.

[Install and Setup Python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-22-04-server)

[Install Flask to Create a Web Application](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3)

[Install PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04)

Once everything above is met, you can being using the web application we've created.

## Using the Web Application
For more insight on the steps being described below, you may find it useful to follow [this](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application) tutorial first to get a better understanding of how to connect the database to Flask and have your environment set up for success.

  1. In PostgreSQL, create a database named 'monopoly'. 
  2. Download the zip file of all the code found here, and move the decompressed folder to the correct location where you have set up       your environment. Within that directory, switch into the directory of the file you just downloaded and moved.
  3. Run the init_db file using 'python init_db.py'. This step will dump all of the data from the init db file into the 'monopoly'         database that you just created. 
  4. Run flask to launch the application. Your output should provide you with a URL that says "Running on: " before the URL is displayed.   You can copy that URL and paste it into your browser.
  5. From here, you can navigate that web application and use it how you wish.

