pipeline {
    agent any
    stages {
        stage('request token') {
            steps {
                sh 'python request_predix_token.py'
            }
        }
        stage('query analytics catalog') {
                    steps {
                        sh 'python query_analytics_catalog.py'
                    }
                }
    }
}
