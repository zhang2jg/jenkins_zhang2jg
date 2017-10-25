pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World, 10/25/2017"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
