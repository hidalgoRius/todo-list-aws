import todoList


def delete(event, context):
    """Delete a todo from the persistent storage. Identified by path parameter.
    Path: DELETE todos/{id}
    200 on success
    This function do not return any response to the client.
    :event: environment variables such as payload, path paramethers, etc.
    :context: --
    :return: An object with one property: (int) statusCode.
    """
    todoList.delete_item(event['pathParameters']['id'])

    # create a response
    response = {
        "statusCode": 200
    }

    return response
