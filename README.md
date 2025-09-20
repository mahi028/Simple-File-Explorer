# SFX (SIMPLE FILE EXPLORER)

SFX is a web based file explorer written in python and vue.js for smooth file exploration.

In future, this application is supposed to be a file server which can be accessed from the network and be used as a media streaming server.

> Note that this application is still under development and might not work on your machine

## How to run

[See Realeses here](https://github.com/mahi028/Simple-File-Explorer/releases)

Download a release and choose any way you like to run the Application on your machine


**1. Download the latest SFX binary from the release section and run:**

```sh
./SFX # path to the SFX binary
``` 
Then Visit `http://your-device-ip:9876` 


**2. Download the latest SFX source code from the release section and run with uv (Recommended way for now)**

Unzip the source code first and change the directory to SFX

```sh
uv run wsgi.py
```
Then Visit `http://your-device-ip:9876` 

**3. Run as development server with uv**

Unzip the source code first and change the directory to SFX

```sh
uv run app.py
```
Then Visit `http://your-device-ip:9876` 

**4. If you don't have uv installed**

Unzip the source code first and change the directory to SFX

```sh
# Change directory
cd SFX # path to source code directory

# Create virtual environment
python3 -m venv env       # 'python -m venv env' for Windows

# Activate environment
source ./env/bin/activate # 'env\Scripts\activate' for Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 wgsi.py  # or python3 app.py for development server
```
Then Visit `http://your-device-ip:9876` 


## FAQ

* How to get your device ip?
    It should be visible when you run the application form the terminal. But if not: 
    - On Windows: Run `ipconfig` on your terminal.
    - On Linux: Run `ip address` on your terminal.

    You are trying to find an address typically starts with 192.168.-.-

* How to configure the app?
    - Instructions here