pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Amymah/gitjenkinsintegration.git'
            }
        }

        stage('Run Python Files') {
            steps {
                bat 'python AlertFunc.py'
                bat 'python DatePicker.py'
            }
        }
    }
}
