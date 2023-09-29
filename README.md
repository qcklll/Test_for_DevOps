# Задание №1:настройка сервера с помощью Ansible для OS Ubuntu 18.04

# Роли
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

