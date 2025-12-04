import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:$(messages)s')

project_name="textSummarize"
list_of_files=[
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logginng/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/conguration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config.config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "DockerFile",
    "requirement.txt",
    "setup.py",
    "research/trails.ipynb"


]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory{filedir} of the file {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    
        logging.info(f"Creating empty file {filepath}")
    else:
        logging.info("File arleardy exists")