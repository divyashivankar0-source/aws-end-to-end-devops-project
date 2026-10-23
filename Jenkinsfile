
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t aws-devops-app:v1 -f docker/Dockerfile .'
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing application health'
                sh '''
                    docker rm -f aws-devops-test 2>/dev/null || true
                    docker run -d --name aws-devops-test -p 5001:5000 aws-devops-app:v1
                    sleep 5
                    curl --fail http://localhost:5001/health
                    docker rm -f aws-devops-test
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USER" --password-stdin
                        docker tag aws-devops-app:v1 "$DOCKERHUB_USER/aws-devops-app:v1"
                        docker push "$DOCKERHUB_USER/aws-devops-app:v1"
                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
