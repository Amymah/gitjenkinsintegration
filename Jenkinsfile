pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from version control
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Build your project
                sh 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                // Run tests
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy the application
                sh './deploy.sh'
            }
        }
    }
}
