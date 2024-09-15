import json
import boto3
import base64
import datetime
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create client connections to Bedrock and S3 services
client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')

def lambda_handler(event, context):
    input_prompt = event.get('prompt', '')
    logger.info(f"Input prompt: {input_prompt}")

    # Request to access the Bedrock Service
    response_bedrock = client_bedrock.invoke_model(
        contentType='application/json',
        accept='application/json',
        modelId='stability.stable-diffusion-xl-v1',
        body=json.dumps({
            "text_prompts": [{"text": input_prompt}],
            "cfg_scale": 10,
            "steps": 30,
            "seed": 0
        })
    )
    logger.info("Invoked Bedrock model successfully.")

    # Retrieve and decode the response
    response_body_content = response_bedrock['body'].read()
    response_bedrock_byte = json.loads(response_body_content)
    response_bedrock_base64 = response_bedrock_byte['artifacts'][0]['base64']
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)

    # Include the correct image file extension
    poster_name = 'posterName_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    logger.info(f"Poster name: {poster_name}")

    # Upload the file to S3
    response_s3 = client_s3.put_object(
        Bucket='movieposterdesign07',
        Body=response_bedrock_finalimage,
        Key=poster_name
    )
    logger.info(f"Response from S3 put_object: {response_s3}")

    # Generate Pre-Signed URL
    generate_presigned_url = client_s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': 'movieposterdesign07', 'Key': poster_name},
        ExpiresIn=3600
    )
    logger.info(f"Generated pre-signed URL: {generate_presigned_url}")

    return {
        'statusCode': 200,
        'body': generate_presigned_url
    }
