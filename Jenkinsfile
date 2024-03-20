pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'C:\\Users\\mhmdh\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pip.exe install selenium requests'
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Your build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'C:\\Users\\mhmdh\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\python.exe -m unittest tests/pos_test_api&ui.py'

            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Your deployment steps here
            }

}