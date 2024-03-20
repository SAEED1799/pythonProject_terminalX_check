pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('pos_test_api') {
            steps {
                bat "docker run --name pos_test_api_ui ${IMAGE_NAME}:${TAG} python pos_test_api_ui.py"
                bat "docker rm pos_test_api_ui"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "docker rmi ${IMAGE_NAME}:${TAG}"
 }
}
}