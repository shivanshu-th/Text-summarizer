import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", #CI CD related yaml file
    f"src/{project_name}/__init__.py", #local package from text summarizer import this whenever i want to install local packages
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/common.py", #write all my utility ;
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
    "setup.py", #local package
    "research/trials.ipynb"

]


for filepath in list_of_files:
    filepath = Path(filepath) #we have used forward slash but windows use backward slash for path so we use path library of which the path function checks the os and return the path
    filedir, filename = os.path.split(filepath) # to separate directory name and file name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
