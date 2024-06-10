import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="Text_Summarizer"
# init files is needed to install local package
list_of_files = [
    ".github.com/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/_common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]
# the above file will make creation of file in one go
# in linux there is problem as backlash is used in linux and in windows there is usage of forward slash so changes is handeled using path library and below does the same.
for filepath in list_of_files:
    filepath =Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"created directory {filedir} for the file ${filename}")
    # creation of file   
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"created empty file {filepath}")
    else:
        logging.info(f" {filepath} already exists")