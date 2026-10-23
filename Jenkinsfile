
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checkout stage'
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
                echo 'Running application container'
                sh '''
                    docker rm -f aws-devops-test 2>/dev/null || true
                    docker run -d --name aws-devops-test -p 5001:5000 aws-devops-app:v1
                    sleep 5
                    curl --fail http://localhost:5001/health
                    docker rm -f aws-devops-test
                '''
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
