pipeline {
    agent any
    environment {
        PYTHONPATH = "C:/Users/hp/PycharmProjects/pythonProject5_terminalX_final"
        TEST_REPORTS='test-reports'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                bat 'pip install -r requirements.txt' // Install dependencies if needed
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Run your tests here
                bat 'python tests/functional_tests/test_search_is_good.py'
            }
        }
        stage('Run API Tests with Pytest') {
            steps {
                echo 'Running API Tests with Pytest..'
                script {
                    try {
                        // Run pytest with pytest-html plugin to generate HTML report
                        bat "C:/Users/hp/anaconda3/Scripts/pytest.exe tests/functional_tests/test_search_is_good.py --html=test-reports/report.html"
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Add deployment steps here if needed
            }
                     }
           }
}