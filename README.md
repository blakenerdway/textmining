# Text mining
The text mining library here provides a way to easily produce topics for documents. Python is the language used for generating the topics, but bindings for communication to the Python service are provided for Java as well as Javascript.

## Installing
This project has been tested using Python 3.6.4, and should use any version >= Python 3.6. NPM and NodeJS are used to run the server for the GUI of the project. Instructions for installation will be provided below. If you do have Python3 installed already, you can check your version by typing in a console: `python3 --version`. If it is not >= 3.6, I recommend upgrading as it has not been tested with any other versions of Python.

### Linux
<b> Python </b>

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

<b> NodeJS </b>
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


### MacOS
For MacOS, I suggest using Homebrew to install Python 3.6. Python 2.7 may be installed by default, so Python 3.6 will be installed in parallel. Type the following command in a terminal window after you have installed and verified your Homebrew installation:

```
brew install python3
```

To update the python version:

```
brew update
brew upgrade python3
```

<b> NodeJS </b>
```
brew install node
```

### Windows
No new dependencies for Windows are needed, but since this release has not been tested on Windows, no installation instructions will be provided.
