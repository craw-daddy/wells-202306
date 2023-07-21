This is an application that is designed to show off using Python tools to query a database, create a visualization using Altair, and using streamlit to develop a website to perform these actions.  

We have deployed on Render.com (it is here: https://wells-202306-vr3d.onrender.com/). 

Important notes:  
*  We need to provide Render.com with an environmental variable in the configuration called `WELLS_URL` that has the connection string for connecting with the online database (remember that for security reasons we don't want to include it in the `git` repository as it has a username and password in that connection string).  It is possible to supply one or more environmental variables through the web interface when we create the application.
*  We should tell Render.com what version of Python we are using, i.e. we developed the application on Python 3.10.8 so we know it should work with that Python version (and, of course, the packages we will install in the environment using the `requirements.txt` file).  Render.com will otherwise default to some Python version of its own choosing.  
*  Render.com is generally assuming we are running a Flask application, but we are using `streamlit`.  We must provide the "startup" command so that Render will correctly start the application.  Also, we need to tell Render to use an open port to communicate with the "outside world" and to not attempt to open a web browser on the deployment machine when starting the `streamlit` application (not only would that be not helpful, I think it might actually cause an error).  The way to do this on Render is to use the startup command `streamlit run --server.port=$PORT --server.headless=true app.py` (replace `app.py` with whatever the name of your application might be).  

