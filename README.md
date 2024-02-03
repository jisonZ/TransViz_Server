# TransViz_Server
Inside that directory you can run several commands:


        python run.py
                Starts the server, default config is set to development.


        export secret_key=STRING
                Sets the secret key for your app.


        export PRODUCTION=True
                Sets production config for your app. Setting it to False will set the development config.


        source venv/bin/activate (unix)
        ./venv/Scripts/activate  (windows)
                Activate the virtual enviroment for the app.


        pip install -r requirements.txt
                Install the packages listed in requirements.txt into the venv.


We suggest that you start by typing:
        cd TransVizServer
        source venv/bin/activate
        pip install -r requirements.txt
        python run.py
Or:
        flask run--debug
Great Progress!
Testing! Yayy!
Happy hacking!