<!--
 * @Descripttion: 
 * @Author: SijinHuang
 * @Date: 2021-12-05 00:33:42
 * @LastEditors: SijinHuang
 * @LastEditTime: 2021-12-13 21:53:31
-->

# Deployment Steps

Following scripts are copied from [Lambda Documentations](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-from-base)

## Create Docker Image

1. Build image

    At project root directory:

    ```bash
    docker build -t sfr-lambda -f lambda/Dockerfile .
    ```

1. Authenticate the Docker CLI to your Amazon ECR registry.

    ```bash
    aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-2.amazonaws.com    
    ```

1. Create a repository in Amazon ECR using the create-repository command.

    ```bash
    aws ecr create-repository --repository-name sfr-lambda --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
    ```

1. Tag your image to match your repository name, and deploy the image to Amazon ECR using the docker push command.

    ```bash
    docker tag sfr-lambda:latest 123456789012.dkr.ecr.us-east-2.amazonaws.com/sfr-lambda:latest
    docker push 123456789012.dkr.ecr.us-east-2.amazonaws.com/sfr-lambda:latest
    ```

1. Now that your container image resides in the Amazon ECR container registry, you can [create and run](https://docs.aws.amazon.com/lambda/latest/dg/configuration-images.html) the Lambda function.

## Optional: Test the Image Locally
[Lambda Documentations](https://docs.aws.amazon.com/lambda/latest/dg/images-test.html#images-test-AWSbase)

1. Run your container image locally using the docker run command.

   ```bash
    docker run -p 9000:8080  sfr-lambda:latest
    ```

    This command runs the image as a container and starts up an endpoint locally at localhost:9000/2015-03-31/functions/function/invocations.

1. From a new terminal window, post an event to the following endpoint using a curl command:

   ```bash
    curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"img_url": "https://images-na.ssl-images-amazon.com/images/M/MV5BOTg5NDE3OTA4MF5BMl5BanBnXkFtZTcwMTA1MTQ5MQ@@._V1_.jpg"}'
    ```

    This command invokes the Lambda function running in the container image and returns a response.
