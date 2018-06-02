pipeline {
  agent any
  stages {
    stage('test script') {
      steps {
        sh '''pushd test
python3 test.py
popd'''
      }
    }
    stage('email') {
      steps {
        mail(subject: 'Jenkins VC test passed', body: 'test passed', from: 'josh@hauptj.com', to: 'josh@hauptj.com')
      }
    }
  }
}