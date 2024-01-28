# import json
from middlewares.helpers.with_middlewares import with_middlewares
from middlewares.add_timestamp_middleware import add_timestamp_middleware

def main(event, _context):
    # print(f"main: {json.dumps(event)}")
    print(f"main: {event}")
    print("Hello world")
    return {
        "statusCode": 200,
        "body": {
            "success": "true",
            "message": "Works"
        }
    }
    # raise Exception({
    #     "statusCode": 500,
    #     "body": {
    #         "success": "false",
    #         "message": "Fails"
    #     }
    # })

def callback(err, res):
    # print(f"Err: {json.dumps(err)}")
    # print(f"Res: {json.dumps(res)}")
    print(f"Err: {err}")
    print(f"Res: {res}")

if __name__ == "__main__":
    with_middlewares(main, [add_timestamp_middleware()])({}, {}, callback)