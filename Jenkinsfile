pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-jenkins-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f flask-jenkins-container || true'
                sh 'docker run -d -p 5002:5000 --name flask-jenkins-container flask-jenkins-app'
            }
        }
    }
}
