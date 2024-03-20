stage('Run API Tests with Pytest') {
            steps {
                script {
                    try {
                        bat 'call venv\\Scripts\\python.exe -m pytest tests/pos_test_api&ui.py --html=${TEST_REPORTS}\\report.html --self-contained-html'
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                    }
                }
            }
        }
    }
pip freeze > requirements.txt

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

        stage('Run Add to card') {
            steps {
                bat "docker run --name test_check_card ${IMAGE_NAME}:${TAG} python pos_test_api&ui.py "
                bat "docker rm pos_test_api&ui"
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