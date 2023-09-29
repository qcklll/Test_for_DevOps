# Задание №1:настройка сервера с помощью Ansible для OS Ubuntu 18.04

## Роли
- Написать роль Ansible, которая установит на хост 5 выбранных пакетов (например: nmap, traceroute, vim и т.д.)
- Настроить DNS-серверы для хоста: 8.8.8.8, 1.1.1.1
- Написать роль Ansible, которая установит на хост ELK-стек из дефолтного файла docker-compose, используя модуль docker_containers и шаблоны для настройки конфигураций.

> 1.Создать структуру каталога для Ansible проекта
**Используем команды** `mkdir <directory_name>` и `touch file_name`
```yaml
├───ansible_project
   └───roles 
       ├───configure_dns
       │   ├───tasks
                main.yml
       │   └───templates
                dns-resolvconf.j2
       ├───install_elk_stack
       │   ├───files
                docker-compose.yml
       │   └───tasks
                main.yml
       └───install_packages
           └───tasks
               main.yml
    inventory.ini
    playbook.yml
```

1. Создание inventory.ini
```yaml
[myserver]
server_ip_address ansible_ssh_user=root ansible_ssh_private_key_file=/root/.ssh/id_rsa
```

2. Создание ролей Ansible
- Для каждой роли необходимо создать 3 отдельных файла
- Также: для *install_elk_stack* создать подпапку *files* и в ней файл `touch docker-compose.yml`  
- Для *configure_dns* создать шаблон `touch dns-resolvconf.j2`
3. Разрабокта ролей
>Создать роли для установки пакетов, настройки dns, установки ELK-stack
4. Создание плейбука `touch playbook.yml` 


```yaml
---
- hosts: ubuntu
  tasks:
    - name: Include the install_packages role
      include_role:
        name: install_packages

    - name: Include the configure_dns role
      include_role:
        name: configure_dns

    - name: Include the install_elk_stack role
      include_role:
        name: install_elk_stack
```
5. запуск плейбука
```bash
ansible-playbook -i inventory.ini playbook.yml
```


# Задание №2.Kubernetes

## 1. Написать приложение на Python, которое будет слушать порт 8080 и обрабатывать входящие запросы.
```python
from http.server import HTTPServer, BaseHTTPRequestHandler
*app.py*
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Kubernetes!"
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f'Listening on {host}:{port}')
    httpd.serve_forever()
```
## 2. Упаковать это приложение в Docker и загрузить его на Docker Hub.
    2.1 Создать Dockerfile `touch Dockerfile`
    ```Dockerfile
        # my-python-app/Dockerfile
        FROM python:3.8

        WORKDIR /app
        COPY app.py .

        EXPOSE 8080

        CMD ["python", "app.py"]
    ```
    2.1.1 Для запуска Dockerfile необходимо залогиниться в docker
    `bash sudo docker login`
    2.1.2 Соберём образ и запустим его `bash docker build -t my-python-app .` *Важно находится в директории с Dockerfile т.к мы указали ".", что означает использовать текущую директорию
     `bash docker run -p 8080:8080 my-python-app`
    Переходим на [local](localhost:8080) Завершить работу приложения можно нажав сочетание клавиш *ctrl+c*
## 3. Создание Helm-чарта
    3.1. Создайте структуру директорий Helm-чарта, включая файлы Chart.yaml, values.yaml, и каталоги templates и charts.

    3.2. В каталоге templates, создайте следующие файлы:

        + deployment.yaml: Опишите развертывание вашего контейнера в    Kubernetes Deployment.
        + service.yaml: Опишите создание Kubernetes Service, который будет обслуживать ваше приложение.
        + ingress.yaml: Опишите настройку ингреса для вашего приложения, чтобы можно было получить к нему доступ извне.
    3.3. В файле values.yaml укажите параметры вашего Helm-чарта, такие как имя образа, версия и настройки ингреса.
## 4 Установка Helm-чарта в Kubernetes
    4.1 Установить kubernetes 
`bash sudo apt install -y kubectl kubeadm kubelet kubernetes-cni`
    4.2 Установить Helm Чарт, используя команду `helm install my-python-app ./my-python-app-chart`
## 5 Проверка приложения  
`bash kubectl get nodes`
`bash kubectl get pods`
`bash kubectl get ingress`




