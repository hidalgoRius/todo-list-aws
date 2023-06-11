import json
import decimalencoder
import todoList


def list(event, context):
    """Get all todo from the persistent storage
    Path: GET todos

    :event: environment variables such as payload, path paramethers, etc. 
    :context: --
    :return: An object with two properties: (int) statusCode and (string) body.
    """
    # fetch all todos from the database
    result = todoList.get_items()
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
    }
    return response
