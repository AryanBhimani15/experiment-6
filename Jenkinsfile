pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                sh 'which python3'
                sh 'python3 --version'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test Script') {
            steps {
                sh 'echo "Pipeline working successfully"'
            }
        }
    }
}
