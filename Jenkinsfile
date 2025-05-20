pipeline {
    agent {label 'vm-oracle'}
    environment{
        IMAGE_NAME = "test-flask-app2"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        CONTAINER_NAME = "test-app"
    }
    stages{
        stage('Checkout'){
            steps{
                git url: 'https://github.com/ScoobyBo/test1.git', branch: 'main'
            }
        }
        stage('Build docker image'){
            steps{
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }
        stage('deploy container'){
            steps{
                sh 'docker run -d --name $CONTAINER_NAME -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }
        
    }
    post{
        always {
            sh "echo 'Cleaning up container ${CONTAINER_NAME} removing image hehehe ${IMAGE_NAME}:${IMAGE_TAG}'"
            sh "docker stop ${CONTAINER_NAME} || true"
            sh "docker rm ${CONTAINER_NAME} || true"
            sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true"
        }
       
    }
}