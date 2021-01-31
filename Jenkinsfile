pipeline {
    agent { any }
    stages {
        stage('Build image') {
            steps {
                sh 'docker build -t mycustomflaskserver .'
                }
        }
        stage('Run') {
            steps {
                sh 'docker run -it -p 5005:4999 mycustomflaskserver'
                }
        }
    }  
}     
