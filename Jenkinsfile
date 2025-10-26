pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git(
                    url: 'https://github.com/JIBINJOBY/smart-health-monitor.git',
                    credentialsId: 'github-pat',
                    branch: 'main'
                )
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t smart-health-app .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 smart-health-app'
            }
        }
    }
}
