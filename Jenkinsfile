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

        stage('Run Add Food to Meal Test') {
            steps {
                bat "docker run --name tests/pos_test_api&ui ${IMAGE_NAME}:${TAG} python tests/pos_test_api&ui.py"
                bat "docker rm tests/pos_test_api&ui"
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