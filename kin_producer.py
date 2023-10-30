import json
import random
import time
import boto3

client = boto3.client("kinesis", region_name = "us-east-2")

STREAM_NAME = "kin_stream_example"

try:
    while True:
        time.sleep(1)
        id  = random.randint(1, 100000)
        age = random.randint(1, 100)
        name_pool = ('Adm', 'Jhon', 'Yi', 'Rui')
        name  = random.choice(name_pool)
        data = {
            "Id" : id,
            "Name" : name,
            "Age" : age
        }
        encode_data = bytes(json.dumps(data).encode("utf-8"))
        print(f"Sending:{data}")
        response = response = client.put_record(StreamName=STREAM_NAME, Data=encode_data ,PartitionKey="A")
        print(f"SequenceNumber is : {response['SequenceNumber']}")

except KeyboardInterrupt:
    print("Finshing due to keyboard interrupt")





