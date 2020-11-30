import json
import cv2
import numpy as np

print()

def hello(event, context):
    body = {
        "cv2version": cv2.__version__,
        "npversion": np.__version__,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
