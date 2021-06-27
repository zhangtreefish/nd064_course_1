python3 --version

http://0.0.0.0:5000/ 
Mommys-iMac:exercises mommy$ pip3 install -r requirements.txt
Python3 app.py
No hot loading: CtrlC and then start again when editing
app.logger.info('Inside /status endpoint')
python3 exercises/python-helloworld/app.py
http://0.0.0.0:5000/status
http://0.0.0.0:5000/metrics

SUSE
python3 --version

http://0.0.0.0:5000/ 
Mommys-iMac:exercises mommy$ pip3 install -r requirements.txt
Python3 app.py
No hot loading: CtrlC and then start again when editing
app.logger.info('Inside /status endpoint')
python3 exercises/python-helloworld/app.py

docker run -d -p 5111:5000 python-helloworld
docker build -t python-helloworld lesson1/python-app
docker images
docker ps
docker run -d  -p 5000:5000 hola-mundo //`docker run -d hola-mundo -p 5000:5000` does not 
Running a detached container: no input/output; need to `docker attach` after 
`docker start`
`docker run -it --name go-helloword -p 6111:6111 -v $PWD:/mnt golang:1.11.13-alpine3.10 sh` // start a go docker

docker ps
docker container rm 89600001a636

s up to date...
==> default: Clearing any previously set network interfaces...
There was an error while executing `VBoxManage`, a CLI used by Vagrant
for controlling VirtualBox. The command and stderr is shown below.

Command: ["hostonlyif", "create"]

* `kubectl config --kubeconfig=config-demo set-cluster` to define clusters
* `kubectl config --kubeconfig=config-demo set-credentials` for setting user credentials
* `kubectl config --kubeconfig=config-demo set-context` to define or change contexts
`kubectl config use-context` command. The currently active context can be checked with `kubectl config current-context`.
*  https://community.suse.com/feed
* https://community.suse.com/posts/cluster-this-is-your-admin-do-you-read
export KUBECONFIG=˜/.kube/config:second-config-file:third-config-file
kubectl config view --minify --flatten --context=mycontext > myconfig.yaml

Export KUBECONFIG=HOME/.kube/config:(ls -m HOME/.kube/*.yaml) | \
tr ',' ':' | \
tr -d "[:blank:]")
By default, kubectl looks for a file named config in the $HOME/.kube directory.
How to display current cluster and namespace in your command line prompt.

Sudo su
Kubectl get no
kubectl --kubeconfig ~/.kube/config/k3s.yaml get pods --all-namespaces

To choose the current context:
kubectl config use-context
https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
kubectl config --kubeconfig=config-demo view

Set the current context:
kubectl config --kubeconfig=config-demo use-context dev-frontend. —minify//minify: only current context
Or export KUBECONFIG= /etc/rancher/k3s/k3s.yaml
Kubectl port-forward po/<pod> podPort:hostPort //so that can verify on host port
Kubectl edit deploy <deploy> -o yaml. /default rolling updates?
Kubectl cluster-info
Kubectl get nodes -o wide //get internal IP etc
Kubectl describe node <node> | grep CIDR

Sudo -s. //to enter as sudo user
Echo $USER
Echo $HOME/.kube
sudo chown -R $USER $HOME/.kube //assign  <> as new owner of <>
cat /etc/rancher/k3s/k3s.yaml

Docker image ls
Vagrant ssh
curl -sfL https://get.k3s.io | sh -
kubectl create deploy go-helloworld --image=treefishdocker/go-helloworld:v1.0.0
zypper install -t pattern apparmor//after ssh into vagrant

kubectl port-forward --address 0.0.0.0 po/go-helloworld-8689ff4dff-txs67 6111:6111

docker build -t go-helloworld .
docker tag go-helloworld:latest treefishdocker/go-helloworld:v2.0.0
kubectl edit deploy go-helloworld

192.168.50.4:6112//without changing the port at Vagrant, this still works 
0.0.0.0:6112


