import json
import logging
import decimalencoder
import todoList


def update(event, context):
    """Update an existing todo element.
    Identified by path parameter.
    Path: PUT todos/{id}
    Mandatory to receive JSON format and required at least "text" 
    property on JSON payload.
    :event: environment variables such as payload, path paramethers, etc.
    :context: --
    :raise Exception if mandatory fields are not received on JSON Payload.
    :return: An object with two properties: (int) statusCode and (string) body.
    """
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return
    # update the todo in the database
    result = todoList.update_item( 
        event['pathParameters']['id'],
        data['text'], data['checked'])
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result,
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
