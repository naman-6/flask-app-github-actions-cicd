
# Flask App - Github Actions CI/CD

- A simple `Hello World` flask application. Demonstrates create unit tests for a basic Flask app - using the `pytest` module. 

- The unit tests can run on webpages that your web app returns, as well as responses from Api endpoints. 
- This web app is running on port 5000, so after you run the code, you can view it by going to `http://localhost:5000`. To view the endpoints `/api/DemoApiEndpoint`
## Deployment

To deploy this project, first you need to set some variables like `AWS_ACCESS_KEY`, `AWS_PUBLIC_KEY`, `AWS_SECRET_ACCESS_KEY` and `AWS_SSH_KEY` to `Repo Settings=>Secretes and Variables=>actions`.

Then on EC2 instance you need to install docker by `sudo apt-get install docker.io -y` and you need to create an ECR repository by the same name (in this case) `aws-deploy`.
