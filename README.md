# python-docker-remote-debugging
This is a simple example to demonstrate how to do Python remote debugging running in a Docker container, in VS Code.

# Quickstart 


1. Install the Python Remote Debugger library 
    > Note: 3.0.0 is the only version working at the moment
    
    `pip install ptvsd==3.0.0`
    


1. Import the Python Remote Debugger library in your code

    `import ptvsd`
    
1. Setup the Python Remote Debugger in your code once

    `ptvsd.enable_attach("my_secret", address=('0.0.0.0', 3000))`

1. Run your container, mapping port 3000

    `sudo docker run -it -p 3000:3000 remote-python`

1. Add the bellow launch settings to your launch.json file

    ```
    {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Attach",
            "type": "python",
            "request": "attach",
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "${workspaceFolder}",
            "port": 3000,
            "secret": "my_secret",
            "host": "localhost"
        } 
    ]}
    ```

    >Note: if the container is not running locally, you need to set the container IP in the **host**

1. Select the *Python: Attach* configuration and Hit F5
    > Note: Breakpoints and active line are not working well in VS Code