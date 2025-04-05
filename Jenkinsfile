pipeline {
    agent {
        label 'ec2-linux-docker-agent'
    }
    
    environment {
        SONARQUBE_SERVER = 'http://your-sonarqube-server'  // Replace with your SonarQube server URL
        SONARQUBE_TOKEN = credentials('sonar-token')     // Store the SonarQube token securely in Jenkins credentials
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Checkout the code from the repository
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // Install required Python dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run SonarQube Scan') {
            steps {
                withSonarQubeEnv(installationName: 'sql') {
                   sh 'sonar-scanner' 
                }
            }
        }
        
        stage('Quality Gate Check') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
