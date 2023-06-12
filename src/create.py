import json
import logging
import todoList


def create(event, context):
    """Create a new todo resource.
    Path: POST todos
    Mandatory to receive JSON format and required at least "text"
    property on JSON payload.
    :event: environment variables such as payload, path paramethers, etc.
    :context: --
    :raise Exception if mandatory fields are not received on JSON Payload.
    :return: An object with two properties: (int) statusCode and (string) body.
    """
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation failed")
        raise Exception("Couldn't create the todo item.")
    item = todoList.put_item(data['text'])
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response
