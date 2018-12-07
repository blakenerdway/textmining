
# Text mining
The text mining library here provides a central location for various text mining resources. Python is the language used for generating the topics, but bindings for communication to the Python service are provided for Java as well as JavaScript.


## Table of Contents

* [1. Requirements](#Requirements)
  * [1.1 Linux](#linux)
	  * [1.1.1 Python](#linux-python)
	  * [1.1.2 NodeJS](#linux-nodejs)
  * [1.2 MacOS](macos)
      * [1.2.1 Python](#macos-python)
	  * [1.2.2 NodeJS](#macos-nodejs)
  * [1.3 Windows](#windows)
 * [2. Installing](#installing)
	 * [1.1 Python packages](#python-packages)
	 * [1.2 Node dependencies](#node-dependencies)
 * [3. Running](#running)
	 * [3.1 Python](#running-python)
	 * [3.2 Node](#running-node)
 * [4. Notes](#notes)


## 1. Requirements
This project has been tested using Python 3.6.4, and should work with any version >= Python 3.6.1. NodeJS is used to run the server for the GUI of the project. Instructions for installation will be provided below. If you do have Python3 installed already, you can check your version by typing in a console: `python3 --version`. If it is not >= 3.6.1, I recommend upgrading as it has not been tested with any other versions of Python. You should also upgrade your pip version to >= 18.0: `python -m pip install --upgrade pip`

### 1.1 Linux
#### 1.1.1 Python  <a name="linux-python"></a>
For Ubuntu >= 16.10, the following commands can be used to upgrade:
```
sudo apt-get update
sudo apt-get install python3.6
```

If you are using Ubuntu < 16.10, type the following commands:
```
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
```
At this point, you should check that your 3.6 is >=3.6.1. (`python3.6 -V`)

If you type `python3 -V` and  it shows that default installed version (generally 3.5) is below 3.6.1, you will need to update the default version that the OS looks for. This can be done via the following commands:
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
```
([An article here explains more indepth](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/))

#### 1.1.1 NodeJS <a name="linux-nodejs"></a>

Some widely-used Linux packages are used by NPM as dependencies for the packages. One such package is `build-essential`, installed as follows:
```
sudo apt install build-essential
```

For Ubuntu 14.04 through Ubuntu 16.04, the following command may be used to install NodeJS as well as the package manager NPM:
```
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
```

For some versions of Ubuntu starting with 16.04, the `apt-get` command has been deprecated and has been replaced with `apt`. The updated commands are:
```
sudo apt update
sudo apt install nodejs
sudo apt install npm
```


### 1.2 MacOS
#### 1.2.1 Python <a name="macos-python"></a>
For MacOS, I suggest using Homebrew to install Python 3.6. Python 2.7 may be installed by default, so Python 3.6 will be installed in parallel. Type the following command in a terminal window after you have installed and verified your Homebrew installation:
```
brew install python3
```
To update the python version:
```
brew update
brew upgrade python3
```

#### 1.2.2 NodeJS <a name="macos-nodejs"></a>
```
brew install node
```

### 1.3 Windows
It seems that Python 3.6.1 is needed due to an issue with Protobuf. (see here)[https://github.com/protocolbuffers/protobuf/issues/5046]


## 2. Installing
### 2.1 Python Packages
You will need to run the following commands for the python packages:
```
pip install nltk configparser beautifulsoup4 lxml
pip install grpcio
pip install grpcio-tools googleapis-common-protos
```

**Note**: If the `googleapis-common-protos` fails with an error: `Command "python setup.py egg_info" failed with error code 1`, you will need to also do the following [pip upgrade](https://github.com/googleapis/google-cloud-python/issues/3884#issuecomment-325161411):

`pip install --upgrade setuptools`

and then:

`pip install googleapis-common-protos`

Next we need to install some `nltk` packages. In a console, start a new python script by typing either: `python` or `python3` :
```
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> exit()
```

### 2.2 Node Dependencies
In `<PROJ_HOME>/js` type `npm install` to retrieve all the required dependencies for the node server.

## 3. Running
### 3.1 Python <a name="running-python"></a>
The Pycharm IDE was used to develop the Python module, so to keep it simple, we will be using that to run. Run the main class xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx to start the server.

### 3.2 Node <a name="running-node"></a>
In a terminal/command prompt, navigate to `<PROJ_HOME>/js` and run: `node app.js` to start the server.

Now you can open a browser and go to `localhost:3000` to see the GUI. You should be able to connect to the server from any remote machine that has a connection to it


## 4. Notes
You should run the Node and Python services on the same machine so that the Python service can access the file uploaded to the server. You can connect to the server via browser from any machine you desire though.

There is a known error where the Node server is killed unexpectedly. This is caused by gRPC when the server-side (in Python) is killed while the Node instance is still running after it has created a client and opened a stream to the gRPC server. (This happens when you upload documents).

To test, move the the python/ directory. Then type `python3 -m text_summary.run_tests` or `python -m text_summary.run_tests`
