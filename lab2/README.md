# Лабораторная работа 2

## Подготовка

Были установлены все необъодимые инструменты: **kubectl**, **minikube**, **helm**

Проверка установки

```
docker --version
kubectl version --client
minikube version
helm version
```

<img src="./images/image8.png" width="800px"/>

## Поднятие кластера и разворачивание сервиса

Далее был поднят кластер с помощью `minikube start --driver=docker`

<img src="./images/image10.png" width="800px"/>

Проверка, что узел готов `kubectl get nodes`

<img src="./images/image12.png" width="500px"/>

Для сервиса была создана папка k8s, в которой написан `app.yaml`, содержащий Namespace, Deployment, Service. В качестве сервиса был выбран nginxdemos/hello (Как иммитация отклика приложения на запрос в браузер).

<img src="./images/image6.png" width="500px"/>

Был совершён деплой через команду `kubectl apply -f app.yaml`, а также проверка через `kubectl get all -n hello-lab`

<img src="./images/image1.png" width="500px"/>

Далее сервис был открт в браузере `minikube service hello-service -n hello-lab --url`

<img src="./images/image4.png" width="600px"/>

## Helm chart

Был создан скелет чарта через `helm create test-chart`

<img src="./images/image2.png" width="500px"/>

В `values.yaml` был заменён replicaCount и image

<img src="./images/image11.png" width="500px"/>

Далее была проведена проверка через lint и выведен итоговый манифест

<img src="./images/image7.png" width="500px"/>

Чарт был задеплоен и проверен `helm list -n test-lab`, `kubectl get all -n test-lab`

<img src="./images/image9.png" width="800px"/>

Далее открыт в браузере

<img src="./images/image5.png" width="600px"/>

### Upgrade

Для изучения обновления было увеличено количество реплик до 4

<img src="./images/image13.png" width="300px"/>

И прведён upgrade. Проверено появление новой ревизии, а также изменение количества подов.

<img src="./images/image3.png" width="700px"/>

