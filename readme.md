# Library Database with SQLAlchemy
Project written with Python, SQLite3 and Object Relational Mapping(ORM).<br/>
Firstly, if you do not have Python on your computer download Python on their offical website [Python Download Link](https://www.python.org/downloads/).<br/>
Secondly, there is SQLite plug-in in the Python standard library. No need to install separatly. <br/>
You should download SQLAlchemy.
SQLAlchemy version is 1.4.22.
To download SQLAlchemy ,you should write **pip install SQLAlchemy** on linux terminal.
DB Browser must be downloaded for SQLite. For Ubuntu system,

1) sudo add-apt-repository -y ppa:linuxgndu/sqlitebrowser
2) sudo apt-get update
3) sudo apt-get install sqlitebrowser <br/>
Additionally, <br/>
I use conda env-package system for this project. If you do not have Conda on your computer, you can download conda like; <br/>
1) Download the installer: [Anaconda Installer](https://www.anaconda.com/products/individual)
2) In a terminal window enter **sha256sum filename**
3) In your terminal window, run: **bash Anaconda-latest-Linux-x86_64.sh**
4) Follow the prompts on the installer screens.
5) If you are unsure about any setting, accept the defaults. You can change them later.
6) To make the changes take effect, close and then re-open your terminal window.
7) Test your installation. In your terminal window or Anaconda Prompt, run the command conda list. A list of installed packages appears if it has been installed correctly.
Default environment is base, you can create your own enviroment **conda create --name env_name python=version** (I use python 3.8)
**conda activate env_name** you can enter your environment
To download SQLAlchemy ,you should write **pip install SQLAlchemy** on linux terminal.

My system versions,
Python = 3.8
OS type: 64-bit
Ubuntu version is 18.04.5 LTS
conda 4.10.3
Ready for SQLite and ORM.
