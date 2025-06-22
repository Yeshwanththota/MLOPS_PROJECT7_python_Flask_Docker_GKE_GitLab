**Tech Stack**
<p align="left"> 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" title="VS Code" alt="VS Code" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" title="Flask" alt="Flask" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg" title="Kubernetes" alt="Kubernetes" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" title="GKE" alt="Google Cloud / GKE" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/gitlab/gitlab-original.svg" title="GitLab" alt="GitLab" width="40" height="40"/>&nbsp; </p>

**Summary**
Leveraged GitLab for code versioning and CI/CD automation. Configured GitLab pipelines to build Docker images, push to Google Container Registry, and deploy to GKE, with secure handling of service account credentials and environment variables.

**Go to mlops_project7_results for outputs**

**Highlights**

1.	Code versioning and CI-CD using GitLab.
2.	GIthub for easy collaboration, Gitlab for stronger security and enterprise system.
3.	GCP setup, clusters, registry
4.	CI-CD Deployment using Gitlab (using Docker, GCR, GKE)
5.	Why not Jenkins? Manual setup, more customised, mostly free.
6.	Why Gitlab? Integrated setup, limited Customizations, free for basic use.

Step 1
Project setup
1.	Creating virtual Environment in project folder.
2.	Creating required folders and files. (artifacts for outputs, pipeline folder, src where main project code lies, (static , templates for html,css,js and flask automatically finds them in project directory), utils for common functions, requirements and setup file. To make a folder a package we need to create a __init__.py file inside it so that the methods/files can be accessed from other places.
3.	Next, we code for setup, custom exceptions, logger, requirements files (basic things at first like numpy, pandas) .
4.	Then we run setup.py in venv in cmd using pip install -e . This will install all the required dependencies for the project make the project directory ready for next steps. This step automatically created a folder with project name given in the setup.py

Step 2
1.	After jupyter notebook testing we start with Data processing.
2.	Create data_processing.py, code it and test. You should see the artifacts in the project directory.
3.	Now model_training.py in src, code it and test. Should see the model.pkl in the artifacts.

Step 3
User App building using Flask
1.	Create application.py in root , code and test. Make sure flask in requirements.
2.	Create index.html, style.css and code, Run.

Step 4
Training Pipeline, Data and Code versioning
1.	Create training_pipeline.py in pipeline folder, code and run.
2.	Now create a account in gitlab and signin. Create a new project- give name- select GKE in the deployment option- make project public – untick the readme- create.
3.	Now we need to configure, go to global and run the 2 cmds in the venv.
4.	In the same page go to HTTPS.
5.	Now in terminal, git init, add branch, add remote, add, commit.
6.	Now push all the necessary code to gitLab.

Step 5
CI/CD Deployment 
1.	Go to Gcp and enable some API’s required for the project. 
2.	Kubernetes Engine API, google container registry API, compute Engine API, IAM API, cloud build API, Cloud storage API.
3.	Search for artifact registry. Create repo- select docker-region uscentral lowa-create.
4.	Next create a service account in IAM- name of account- permissions (owner, storage object viewer, storage object admin, artifact registry administrator, artifact registry writer)-Done.
5.	Create key for service account- hamburger- manage keys- add key- json-create.
6.	Now we need to create cluster. So go to kubernetes engine-cluster- create- give name- select region same as in GCR- tick for “access to DNS”-review-create.
7.	now copy the json file to project root in vscode-rename-add to gitignore.
8.	Create Dockerfile in root, code it.
9.	Then create Kubernetes_deployment.yaml and code it.
10.	Now go to bash in terminal and convert the json key to base64 using cmd cat gcp-key.json | base64 -w 0. Copy the encoded key.
11.	go to gitlab, project, settings – CI/CD-varibales-give the name for key in bottom- paste the key in value and create.
12.	Now in project root create .gitlab-ci.yml, where we write the ci-cd code.
13.	Now push the changes to gitlab.
14.	When you go to project-pipeline- you see it will be running. When you go inside you will see the steps we configured in .gitlab-ci.yml. should be green tick on all.
15.	 After some time (5-10min). go to Kubernetes cluster – workloads-you should see the OK status- go to endpoint- there your application is running-test.
16.	Done
17.	Clean up , clusters, artifacts registry etc.
