#!/usr/bin/env python3

import requests
import subprocess
import os

def jfrogUpload():
    url = "http://43.205.240.109:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    file_path = "/var/lib/jenkins/workspace/HW2/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    absolute_path = os.path.abspath(file_path)
    username = 'admin'
    password = 'Sourav3227'

    with open(file_path,'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)
    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print(f"PUT reuquest failed with status code(response.status_code)")
        print("Response content:")
        print(response.text)

#def mvnBuild():
#    maven_command = "mvn clean install -DskipTests"
#
#    try:
#        subprocess.run(maven_command, check=True, text=True, shell=True)
 #       print("\nMaven build completed succesfully.")
  #  except subprocess.CalledProcessError as e:
   #     print(f"Error: Maven build failed with exit code (e.returncode)")

def main():
#    mvnBuld()
    jfrogUpload()

if __name__=="__main__":
    main()
