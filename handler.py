import json
import re
import os

# check_list = ["Oracle", "Google", "Microsoft", "Amazon", "Deloitte"]
check_list = os.environ['CHECK_LIST'].split(" ")
added_mark = chr(169)

def replace(msg):
    processed_word = msg
    for pattern in check_list:
        if re.search(re.compile(pattern), processed_word):
            processed_word = re.sub(re.compile(pattern), pattern+added_mark, processed_word)
    # print(processed_word)
    return processed_word

def process(event, context):
    print(event)
    if 'body' in event:
        body = {
            "input": event['body'],
            "output": replace(event['body'])
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    else:
        body = {
            "output": "Please input some text"
        }
        response = {
            "statusCode": 400,
            "body": json.dumps(body)
        }
    return response



if __name__ == "__main__":
    replace("Amazon, ;:Oracle,Amazon!!")