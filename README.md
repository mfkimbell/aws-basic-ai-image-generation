# aws-basic-ai-image-generation-and-text-summarization

# Lambda Function 1: Movie Poster Design

![imagegen-ezgif com-speed](https://github.com/user-attachments/assets/bd4d3b33-3cc1-4eaa-ae1c-373c800241a3)


# API Gateway
<img width="1194" alt="Screenshot 2024-09-17 at 10 37 58 AM" src="https://github.com/user-attachments/assets/9c90daf0-ef4c-4a98-a6f1-0c40dea436d1">


Lambda function to generate a movie poster design using a machine learning model from Bedrock and upload the image to S3.

Purpose:
- Takes an input prompt related to movie poster specifications.
- Invokes a Bedrock model to generate a poster image.
- Uploads the generated image to an S3 bucket.
- Returns a pre-signed URL for accessing the uploaded poster.

Components:
- Initializes logging and Boto3 clients for Bedrock and S3.
- Processes input prompt from Lambda event.
- Invokes Bedrock model with input prompt and specific parameters.
- Retrieves and decodes the generated poster image.
- Uploads the image to S3 and generates a pre-signed URL.
- Returns the URL in the Lambda response.

Usage:
- Triggered by events containing a 'prompt' parameter.
- Designed to handle movie poster design requests via API Gateway or other event sources.


# Lambda Function 2: Text Generation


Lambda function to generate text based on a given prompt using the Bedrock service.

Purpose:
- Takes a textual prompt and generates creative text.
- Returns the generated text as a response.

Components:
- Initializes a Boto3 client for Bedrock.
- Processes input prompt from Lambda event.
- Invokes Bedrock model with input prompt and text generation parameters.
- Reads and extracts generated text from Bedrock response.
- Returns the generated text in the Lambda response.

Usage:
- Triggered by events requiring text generation based on user input.
- Suitable for generating creative textual responses via API Gateway or other event sources.


# Additional Notes:

- Ensure Lambda environment has necessary permissions and dependencies (Boto3).
- Implement error handling for model invocation, S3 upload, and URL generation.
- Securely manage access to S3 bucket and pre-signed URLs.

