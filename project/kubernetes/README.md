## Kubernetes Declarative Manifests 

Place the Kubernetes declarative manifests in this directory.
```
kubectl create ns sandbox --save-config --dry-run=client -o yaml > sandbox.yaml
kubectl apply -f sandbox.yaml

kubectl create deploy techtrends --image=techtrends:latest --port=3111 --save-config --dry-run=client -o yaml -n sandbox > techtrends.yaml
vi techtrends.yaml
kubectl apply -f techtrends.yaml

kubectl expose deployment/techtrends --type=ClusterIP --port=4111 -n sandbox 
kubectl get svc -n sandbox -o yaml > techtrends-svc.yaml
vi techtrends-svc.yaml
```
