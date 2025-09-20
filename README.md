# SFX (SIMPLE FILE EXPLORER)

SFX is a web based file explorer written in python and vue.js for smooth file exploration.

In future, this application is supposed to be a file server which can be accessed from the network and be used as a media streaming server.

> Note that this application is still under development and might not work on your machine

## How to run

[See Realeses here](https://github.com/mahi028/Simple-File-Explorer/releases)

Download and choose any way you like to run the Application on your machine


**1. Download the latest SFX binary from the release section and run from terminal by executing the following command:**

```sh
./SFX # path to the SFX binary
``` 
Then Visit `http://your-device-ip:9876` 


**2. Run the application from source code**

Unzip the source code first and change the directory to SFX

Create Virtual env and run the app
```sh
python3 -m venv env       # 'python -m venv env' for windows
source ./env/bin/activate # 'env\Scripts\activate' for windows
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:9876
```
Then Visit `http://your-device-ip:9876` 

**3. Run as development server with uv (Recommended way for now)**
```
uv run app.py
```
Then Visit `http://your-device-ip:9876` 

## FAQ

* How to get your device ip?
    - On Windows: Run `ipconfig` on your terminal.
    - On Linux: Run `ip address` on your terminal.

    You are trying to find an address typically starts with 192.168.-.-

* How to configure the app?
    - Instructions here