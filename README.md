# Junior-DevOps-Exercise
    1. Container:
    a. Create a simple Rest API with one of the next dev languages (Node.js, Python, C# ,Java).
       Rest API should include 2 or more routing.
        a. GET: /hello.
        b. POST: /hello + Username.
        c. PUT: /hello update the Username.
    b. Create Dockerfile.
    c. Create container and run the application.
    d. Use with Postman for verify the application is work. (Provide import file from postman).
    e. Docker commands: (Provide screenshots and files)
        a. What is the internal Ip address of your container?
        b. To which volume container was bound?
        c. Get logs from containers and save as file.
    2. CI/CD: Create simple CI process you can use Jenkins/GitHub Actions/Azure DevOps/other CI tool
       to build image for the Rest API application. ( Provide files)
    3. Bonus - Optional
        a. Create Database container.
        b. Create Docker Compose.
        c. Config the Rest API  connect to database.
        d. Save the name in database.
*Create zip file to all files with following format ${YOUR_NAME}.${DATE}.zip

Good Luck :)




Steps to execute the exercise
in the terminal run
docker-compose up --build
it will build a flask app with MySQL DB
you can see it on browser - localhost:5000


for question 2
cd Build_CI\CD 
docker-compose up --build
that will build Jenkins, GitLab, and artifactory(if we want to publish)
on browser - localhost:80 - upload the project to GitLab
on browser - localhost:8080 to launch Jenkins
follow the steps on the screen
creat ssh key on GitLab and share it with Jenkins
creat a pipeline job using the jenkinsfile from the GitLab project



