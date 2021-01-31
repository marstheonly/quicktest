pipeline {
    agent {
        docker {
            image 'python:3.9.1-buster'
            args '-u root'		 
            args '-p 5005:4999' 
        }
    }
    stages {
        stage('Copy myserver.py') { 
            steps {
		sh 'mkdir /app'
                sh 'cp myserver.py /app/myserver.py'
             }
        }
        stage('Install dependencies') { 
            steps {
                sh 'pip --no-cache-dir install requests flask-restful'
            }
        }
        stage('Run') { 
            steps {
                sh 'python3 /app/myserver.py'
            }
        }
    }
}
