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

    stages {
        stage('Checkout') {
            steps {
                // Check out your code from source control
                git 'https://github.com/SAEED1799/pythonProject_terminalX_check.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                // Set up your Python environment and install dependencies
                // This assumes you have a requirements.txt file
                script {
                    sh 'python -m venv venv'
                    sh '.\\venv\\Scripts\\activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests using report_unit.py
                script {
                    sh '.\\venv\\Scripts\\activate'
                    sh 'python report_unit.py'
                }
            }
        }

        stage('Publish HTML Report') {
            steps {
                // Assumes HtmlTestRunner outputs reports to 'test-reports' directory
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: 'test-reports', reportFiles: 'TestReport.html', reportName: 'HTML Test Report'])
            }
        }
    }
}
