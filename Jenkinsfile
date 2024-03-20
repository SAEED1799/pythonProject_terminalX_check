pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Add test execution steps here
                bat 'python -m unittest tests/test_log_in.py'
                //sh 'python -m unittest RentalCar_tests.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
//                 git 'commit -am "Deploying latest changes"'
//                 git 'push origin main'

            }
        }
    }
}