python3 --version
docker rm <container> then docker rmi <image>
http://0.0.0.0:5000/ //Flask default port is 5000! 
Mommys-iMac:exercises mommy$ pip3 install -r requirements.txt
Python3 app.py
No hot loading: CtrlC and then start again when editing
app.logger.info('Inside /status endpoint')
python3 exercises/python-helloworld/app.py
http://0.0.0.0:5000/status
http://0.0.0.0:5000/metrics

SUSE
python3 --version
$ docker run -dp 80:5000 mypyworld
docker 
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

`sudo -s.`//to enter as sudo user-does not work anymore; ?
Echo $USER
Echo $HOME/.kube
sudo chown -R $USER $HOME/.kube //assign  <> as new owner of <>
`cat /etc/rancher/k3s/k3s.yaml`
`kubectl cluster-info` //https://127.0.0.1:6443
Docker image ls
`vagrant up`, then `vagrant ssh` (`vagrant reload` if changing Vagrantfile)
curl -sfL https://get.k3s.io | sh -
`sudo su - ;`return; then `k3s kubectl get node`//check node
1. kubectl create deploy go-helloworld --image=treefishdocker/go-helloworld:v1.0.0
2. kubectl get rs, kubectl get deploy
kubectl get po
3. //how to check svc endpoint?: kubectl port-forward --address 0.0.0.0 po/go-helloworld-8689ff4dff-txs67 6111:6111
or: pod-ip:port eg `curl 10.42.0.28:80`;
4. or: kubectl expose deploy go-helloworld --port=8111 --target-port=6112
then 4.1. kubectl run test-$RANDOM --namespace=demo --rm -it --image=alpine -- sh
4.2: 
4.3:  -qO 10.43.221.112:8111

5. for rolling update: kubectl edit deploy <deploy> -o yaml
deploy rs pod
6. or kubectl apply -f argocd-python.yaml
-which list source code url and the path for the deployment.yml file
install helm from curl script:in /usr/local/bin/helm
then `helm create mychart`





docker build -t go-helloworld .
docker tag go-helloworld:latest treefishdocker/go-helloworld:v2.0.0


zypper install -t pattern apparmor//after ssh into vagrant





192.168.50.4:6112//without changing the port at Vagrant, this still works 
0.0.0.0:6112

kubectl run test-$RANDOM --namespace=default --rm -it --image=alpine -- sh
wimpty kubectl run test-$RANDOM --namespace=default --rm -it --image=alpine -- sh
wget -qO- <service-cluster-ip>:port //command not found

wget -qO- 10.43.221.112:8111
wget: can't connect to remote host (10.43.221.112): Connection refused
//svc describe list Endpoints of pod-ip:port; so use those. 


kubectl expose deploy go-helloworld --port=6112 --target-port=6112
echo "cmVk" | base64 -D
kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patche


kubectl get all -n custom-metrics //or looping through all api-resources in this namespace shows no resources exist at all: 
kubectl api-resources  --namespaced=true -o name | xargs -n 1 kubectl get -n custom-metrics

kubectl get all -n demo
https://github.com/marketplace/actions/build-and-push-docker-images
nodePort -> port? -> targetPort: per https://stackoverflow.com/questions/41963433/what-does-it-mean-for-a-service-to-be-of-type-nodeport-and-have-both-port-and-t


kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl get all -n argocd
kubectl get service/argocd-server -n argocd -o yaml 
kubectl apply -f argocd-server-nodeport-derived.yaml -n argocd
 kubectl get svc -n argocd

 kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

 kubectl apply -f argocd-alpine.yaml -n argocd

 kubectl cluster-info
kubectl get node
kubectl get all --all-namespaces

//how to get current namespace?
kubectl config current-context
echo NS=$(kubectl get sa -o=jsonpath='{.items[0]..metadata.namespace}')
kubectl config view --minify
kubectl config view --minify --output 'jsonpath={..namespace}'; echo
//where is kube_config_cluster.yml in rancher RKE

~/.kube/config' but with k3s it is at /etc/rancher/k3s/k3s.yml
kubectl get nodes -w
kubectl describe node localhost //has Non-terminated Pods:(with namespace and name of pods)
or kubectl get sa  then kubectl describe sa <sa>


define //containers //env with valueFrom: //configMapKeyRef://name: & //key 


after kubectl apply -f nginx-alpine-server-nodeport.yaml -n demo
 curl 10.43.248.85:30009 //did not work inside localhost node
 
 curl  10.42.0.36:8111 //curl: (7) Failed to connect to 10.42.//.36 port 8111: Connection refused
localhost:~ # curl  10.42.0.36:80//works

https://192.168.50.4:80//404
https://argoproj.github.io/argo-cd/getting_started/ Chrome: https://192.168.50.4:30007/applications for argocd dashboard
error at argocd: 
rpc error: code = Unknown desc = Manifest generation error (cached): nginx-deployment: app path does not 

revive pod: delete it if in cluster: kubectl delete po <pod>  
`kubectl describe node localhost | grep Taint`
`kubectl taint node node01 spray=mortein:NoSchedule`
`kubectl taint node controlplane node-role.kubernetes.io/master:NoSchedule-`
kubectl get po mosquito -o wide
kubectl exec ubuntu-sleeper -- whoami
kubectl get pod/ubuntu-sleeper -o yaml > sleeper.yaml
kubectl create -f docker-registry.yaml --edit -o json
kubectl exec -it <pod_name> -- /bin/bash</pod_name> //`kubectl exec -it ubuntu-sleeper -- /bin/bash`
--cap-add=
kubectl exec -it security-context-demo -- sh
kubectl -n elastic-stack exec -it app -- cat /log/app.log // or `kubectl -n elastic-stack logs app`
 kk label node node01 color=blue
kk explain pod.spec.nodeSelector
kk explain pod.spec | grep -i nodeselector
kk api-resources | grep -i persistentvolumeclaim

kk describe pod <pod-name> | grep -i events -A 10
kk describe node controlplane | grep -i Taints -A 10
kk run cj1 --image=nginx --restart=OnFailure --schedule="*/1 * * * * " \
--dry-run -o yaml > cj1.yaml

kk annotate --help | head -30 //per https://github.com/lucassha/CKAD-resources/blob/master/tipsAndtricks.md
kk create deploy blue --image=nginx --replicas=3 --dry-run=client -o yaml > blue.yaml

deployment.spec.template.spec.affinity:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: color
                operator: In
                values: ["blue"]
                                        
    affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: "node-role.kubernetes.io/master"

                operator: "Exists"

kubectl -n elastic-stack logs kibana

useradd <user>
useradd -K MAIL_DIR=/dev/null nomailuser
passwd <user> //enter pwd twice
sudo vipw
su <user> //switch user to <>, enter pwd ;
visudo //to edit /etc/sudoers

cat /sys/block/sda/sda1/start //to view boundary of a partitionl

 docker container prune [OPTIONS]//remove stopped containers
 