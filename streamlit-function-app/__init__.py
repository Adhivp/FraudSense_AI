import logging
import azure.functions as func
import os
import subprocess

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Get the current working directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Navigate to the parent directory where main.py is located
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Build the path to main.py
    script_path = os.path.join(parent_dir, 'main.py')
    
    command = ['streamlit', 'run', script_path, '--server.headless', 'true']

    subprocess.Popen(command, env=dict(os.environ))

    return func.HttpResponse("Streamlit app is running.")
