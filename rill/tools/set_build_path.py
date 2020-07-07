import os 
import pathlib

current_directory = pathlib.Path(__file__).parent
build_path = (pathlib.Path(__file__).parent/".."/"build").resolve()
