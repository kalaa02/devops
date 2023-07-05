// pipeline {
//     agent any
//     stages {
//         stage('Build') {
//             steps {
//                 sh 'docker build -t myappfk .'
//             }
//         }
//         stage('Run') {
//             steps {
//                 sh 'docker run -p 9000:9000 myappfk'
//             }
//         }
//     }
// }
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("myimagejfk:latest", "-f Dockerfile .")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.run("myimagejfk:latest", "-p 9000:9000")
                }
            }
        }
    }
}