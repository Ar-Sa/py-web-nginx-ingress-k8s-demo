## Run instruction
### Minikube as k8s cluster
- Ensure image are built for minikube docker daemon
```
eval $(minikube docker-env)
```
- Build image and check if it runs fine.
```
docker build -t demo-py-web-app:v1 .
docker run -it --rm -p 5000:5000 demo-py-web-app:v1
curl localhost:5000 // You may need to do "minikube ssh" or "minikube tunnel" before you hit localhost
```
- k8s deployment
```
minikube addons enable ingress // In case ingress isn't yet added to minikube
kubectl apply -f kubernetes.yaml
```
- Test
```
minikube tunnel
curl localhost
```

## Additional, you may need
### Run as Bare python application 
```
cd app/
pip install -r requirements.txt
flask run
curl localhost:5000
```
### Add ingress to k8s cluster in general
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.0/deploy/static/provider/cloud/deploy.yaml
kubectl get pods --namespace=ingress-nginx
```

