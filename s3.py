import boto3

# Create an S3 client object
client = boto3.client('s3')

# Call the list_buckets operation
response = client.list_buckets()

# Output the bucket names
print("Existing buckets:", response)
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")
