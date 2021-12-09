pipeline{
    agent any

    stages { 

    ///pull wihtin jenkins UI localhost:8080
    // stage ("pull") {
    //     steps(
    //     checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[credentialsId: 'root', url: 'git@gitlab:root/jenkins_project.git']]])
    //          )
    //               }


        stage ("build") {
            steps {
                sh """
                docker build -t my_flask_app .
                """
            
                }
                     }

    ///Unit test

    /// build and package are the same this time

    // stage ("package") {
    //     when {
    //         branch 'feature/*'
    //         }
    //         steps {
    //          }
    //             }

    
// no e2e test set
    // stage ("e2e test") {
    //     when {
    //           branch 'master'
    //                      }
    //         steps {
               
    //             }
    //                 }

    ////stage ("publish")

        stage ("deploy") {
          when {
            anyOf{  ///just in case we have brances
              branch 'master' ;
              branch 'release/*'
                }
             }
            steps {
                sh """
                sleep 5
                docker rm -f my_flask_app
                docker run --name my_flask_app -d my_flask_app:1.0-SNAPSHOT
                """
                 }
                    }

        /// report stage

  }
}
