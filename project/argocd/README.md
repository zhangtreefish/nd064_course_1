## ArgoCD Manifests 

Place the ArgoCD manifests in this directory.
vagrant up
vagrant ssh
start k3s: curl -sfL https://get.k3s.io | sh -
`kubectl apply -f argocd-server-nodeport.yaml`
https://192.168.50.4:30007/applications
`kubectl apply -f techtrends-prod.yaml --namespace=argocd`
//application.argoproj.io/techtrends-prod created

