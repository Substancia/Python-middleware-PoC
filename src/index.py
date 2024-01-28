from middlewares.helpers.with_middlewares import with_middlewares
from middlewares.add_timestamp_middleware import add_timestamp_middleware

def main(event, _context):
    print(f"event: {event}")
    print("log: Hello world")
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

if __name__ == "__main__":
    print(f"response: {with_middlewares(main, [add_timestamp_middleware()])({}, {})}")