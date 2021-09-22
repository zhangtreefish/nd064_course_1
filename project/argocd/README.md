## ArgoCD Manifests 

Place the ArgoCD manifests in this directory.
vagrant up
vagrant ssh
start k3s: curl -sfL https://get.k3s.io | sh -
`kubectl apply -f argocd-server-nodeport.yaml`
https://192.168.50.4:30007/applications
`kubectl apply -f techtrends-prod.yaml --namespace=argocd`
//application.argoproj.io/techtrends-prod created

kubectl describe deploy techtrends  --namespace=default 

SyncFailed: Deployment.apps "techtrends" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app.kubernetes.io/instance":"techtrends-prod", "app.kubernetes.io/name":"techtrends-chart"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable

kubectl get svc --all-namespaces//default techtrends ClusterIP 10.43.147.189 <none> 7111/TCP 24h
kubectl describe svc/techtrends 
curl 10.42.0.34:3111/healthz

