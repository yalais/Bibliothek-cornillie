import os
import subprocess

def run_notebook(notebook_path):
    command = [
        "jupyter",
        "nbconvert",
        "--to=notebook",
        "--execute",
        notebook_path,
        "--inplace"
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        raise Exception(f"Fehler beim Ausführen des Notebooks. {stderr}")

# Path to the notebooks
notebook_path1 = "scraper/scraper_blatter.ipynb"
notebook_path2 = "scraper/scraper_buchhaus.ipynb"

#run_notebook(notebook_path1)
run_notebook(notebook_path2)
