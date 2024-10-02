import azure.functions as func
import logging
import subprocess

# Create the function app with anonymous auth level
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="FraudSense")
def FraudSenseTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Start the Streamlit app as a subprocess
    subprocess.Popen(["streamlit", "run", "main.py"])

    # Return a confirmation response that the Streamlit app has been triggered
    return func.HttpResponse(
        "FraudSense Streamlit app triggered!",
        status_code=200
    )
