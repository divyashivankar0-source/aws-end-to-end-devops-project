```groovy
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'aws-devops-app'
        DOCKER_TAG   = 'v1'

        // Replace with your application EC2 public IP
        APP_HOST     = '13.232.154.71'

        APP_CONTAINER = 'aws-devops-app'
        APP_PORT      = '5000'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                sh '''
                    docker build \
                      -t ${DOCKER_IMAGE}:${DOCKER_TAG} \
                      -f docker/Dockerfile .
                '''
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing application health'
                sh '''
                    docker rm -f aws-devops-test 2>/dev/null || true

                    docker run -d \
                      --name aws-devops-test \
                      -p 5001:5000 \
                      ${DOCKER_IMAGE}:${DOCKER_TAG}

                    sleep 5

                    curl --fail --retry 3 --retry-delay 2 \
                      http://localhost:5001/health

                    docker rm -f aws-devops-test
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        set -e

                        echo "$DOCKERHUB_TOKEN" | \
                          docker login \
                            -u "$DOCKERHUB_USER" \
                            --password-stdin

                        docker tag \
                          ${DOCKER_IMAGE}:${DOCKER_TAG} \
                          "$DOCKERHUB_USER/${DOCKER_IMAGE}:${DOCKER_TAG}"

                        docker push \
                          "$DOCKERHUB_USER/${DOCKER_IMAGE}:${DOCKER_TAG}"

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to Application EC2') {
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'app-ec2-ssh-key',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    ),
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        set -e

                        echo "Deploying to application EC2..."

                        # Pull the latest image on the application server
                        ssh -i "$SSH_KEY" \
                          -o StrictHostKeyChecking=accept-new \
                          "$SSH_USER@$APP_HOST" \
                          "echo '$DOCKERHUB_TOKEN' | sudo docker login \
                            -u '$DOCKERHUB_USER' --password-stdin \
                            && sudo docker pull \
                            '$DOCKERHUB_USER/$DOCKER_IMAGE:$DOCKER_TAG'"

                        # Replace the running container
                        ssh -i "$SSH_KEY" \
                          -o StrictHostKeyChecking=accept-new \
                          "$SSH_USER@$APP_HOST" \
                          "sudo docker rm -f '$APP_CONTAINER' 2>/dev/null || true"

                        ssh -i "$SSH_KEY" \
                          -o StrictHostKeyChecking=accept-new \
                          "$SSH_USER@$APP_HOST" \
                          "sudo docker run -d \
                            --name '$APP_CONTAINER' \
                            --restart unless-stopped \
                            -p '$APP_PORT:5000' \
                            '$DOCKERHUB_USER/$DOCKER_IMAGE:$DOCKER_TAG'"

                        # Verify the deployed application
                        ssh -i "$SSH_KEY" \
                          -o StrictHostKeyChecking=accept-new \
                          "$SSH_USER@$APP_HOST" \
                          "sleep 5 && \
                            curl --fail --retry 3 --retry-delay 2 \
                            http://localhost:5000/health"

                        # Log out of Docker Hub on the application server
                        ssh -i "$SSH_KEY" \
                          -o StrictHostKeyChecking=accept-new \
                          "$SSH_USER@$APP_HOST" \
                          "sudo docker logout"

                        echo "Deployment completed successfully!"
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
            echo 'Application has been deployed to EC2.'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }

        always {
            sh 'docker rm -f aws-devops-test 2>/dev/null || true'
        }
    }
}
```