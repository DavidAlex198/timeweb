# timeweb

This application can be cloned from here, or cloned from DockerHub
To clone from docker, move to your desire directory and run:
    docker pull davidalex198/timeweb
Prior to running, you need to enter your github credentials into a file called .credentials.
Your credentials must be in the following format:
    ## GITHUB_USER=username
    ##GITHUB_EMAIL=email
    ##GITHUB_TOKEN=personal_access_token

After both davidalex198/timeweb has been pulled and your credentials entered, copy the following command to use the container:
    docker run -p <HOSTIP>:<PORT>:5000 --env-file .credentials -it davidalex198/timeweb
    
Where HOSTIP is the IP of your machine and PORT is whatever port you want the application to run on. 

The container will start, clone the repository, and you will automatically enter the container. You are still responsible for changing into the timweb directory, running 'make setup', and sourcing your virtual environment. 

To run the applicaiton, type 'make run' or 'python app.py'. In your web browser, enter HOSTIP:PORT and you will be able to view it. 
