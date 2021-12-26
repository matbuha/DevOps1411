def my_func():
    print("hello world")
    properties([[$class: 'JobLocalConfiguration', changeReasonComment: ''], pipelineTriggers([pollSCM('* * * * * ')])])
node {
    stage("clone"){
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/matbuha/DevOps1411.git']]])
    }
    stage("show files"){
        bat "dir"
    }
}
