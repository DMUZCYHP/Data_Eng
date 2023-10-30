import json
import base64
import boto3




def send_to_s3(data, sequenceNumber):
    s3 = boto3.client("s3")
    file_name = f"{sequenceNumber}.json"
    s3_path = "test_data/" + file_name
    bucket = "yi-aws-us-east-2-s3-bucket-example-1"
    response = s3.put_object(Bucket = bucket, Key = s3_path, Body = data)
    return response



def lambda_handler(event, context):
    print(f"event: {event}")
    for record in event["Records"]:
        encode_data = record["kinesis"]["data"]
        decode_data = base64.b64decode(encode_data)
        deserialized_data  =json.loads(decode_data)
        print(f'data: {deserialized_data}')
    
    sequenceNumber = record["kinesis"]["sequenceNumber"]
    result = send_to_s3(decode_data, sequenceNumber)
    print(f'dump data to s3 bucket: {result}')
    