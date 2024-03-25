// pipeline {
//     agent any
//
//     environment {
//         // Define the Docker image name
//         IMAGE_NAME = 'tests'
//         TAG = 'latest'
//     }
//
//     stages {
//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     def customImage = docker.build("${IMAGE_NAME}:${TAG}")
//                 }
//             }
//         }
//
//         stage('test_runner') {
//             steps {
//                 bat "docker run --name add_to_cart ${IMAGE_NAME}:${TAG} python report_unit.py"
//                 bat "docker rm add_to_cart"
//             }
//         }
//     }
//
//     post {
//         always {
//             echo 'Cleaning up...'
//             bat "docker rmi ${IMAGE_NAME}:${TAG}"
//  }
// }
// }
pipeline {
    agent any

    environment {
        // Define your Python virtual environment path if needed
        VENV_PATH = '/path/to/your/virtualenv'
    }

    stages {
        stage('Prepare') {
            steps {
                echo 'Preparing the environment...'
                // If you're using a virtual environment, activate it
                sh '${VENV_PATH}/bin/activate'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Run your Python test script
                sh 'python report_unit.py'
            }
        }

        stage('Publish Report') {
            steps {
                echo 'Publishing HTML report...'
                // Assuming the script generates an HTML report in the 'test-reports' directory
                publishHTML target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'test-reports',
                    reportFiles: 'TestReport.html', // Update this if your report file has a different name
                    reportName: 'HTML Test Report'
                ]
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Any post-build cleanup steps go here
        }
    }
}
