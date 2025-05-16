pipeline {
    agent {label 'vm-oracle'}
    environment{
        IMAGE_NAME = "test-flask-app2"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }
    stages{
        stage('Checkout'){
            steps{
                git url: 'https://github.com/ScoobyBo/test1.git', branch: 'main'
            }
        }
//        stage('Run Tests'){
//            steps{
//                sh 'pip install -r requestments.txt'
//                sh 'pytest test_app.py'
//            }
//        }
        stage('Build docker image'){
            steps{
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }
        stage('deploy container'){
            steps{
                sh 'docker start -p 5000:5000 $IMAGE_NAME'
            }
        }
        
    }
}