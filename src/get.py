import json
import decimalencoder
import todoList


def get(event, context):
    """Get a todo from the persistent storage. Identified by path parameter.
    Path: GET todos/{id}
    200 on success
    404 on not found.
    :event: environment variables such as payload, path paramethers, etc.
    :context: --
    :return: An object with two properties: (int) statusCode and (string) body.
    """
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
