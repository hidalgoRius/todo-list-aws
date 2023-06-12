# 2023-06-12 Pau Hidalgo Rius
# Posible solución del Apartado C caso práctico 1
# DISCLAIMER: No tengo expertise en lenguage PYTHON, primera vez que
# lo uso.
import json
import decimalencoder
import todoList


def translate(event, context):
    """Get a todo from the persistent storage. Identified by path parameter.
    Path: GET todos/{id}/{lang}
    200 on success
    404 on not found.
    :event: environment variables such as payload, path paramethers, etc.
    :context: --
    :return: An object with two properties: (int) statusCode and (string) body.
    """
    # create a response
    item = todoList.translate_item(event['pathParameters']['id'],
                                   event['pathParameters']['lang'])
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
