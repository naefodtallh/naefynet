pipeline {

    gent any 

    stages{

        stage('Clone'){
            steps {
                git branch:'master', url 'https://github.com/naefodtallh/naefynet.git'
            }
            
        }

        stage('Build'){
            steps {
                sh 'pip3 install -r requirements'
            }
            
        }

        stage('Lint'){
            steps {
                sh 'pylint'
            }
            
        }
    }

}