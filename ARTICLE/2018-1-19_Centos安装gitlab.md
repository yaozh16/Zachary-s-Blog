
# Centos 7 安装gitlab
## 1. Install and configure the necessary dependencies
```bash
sudo yum install -y nano lokkit curl openssh-server openssh-clients postfix cronie
sudo service postfix start
sudo chkconfig postfix on
sudo lokkit -s http -s ssh
```

## 2. Add the GitLab package repository and install the package
```
curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
sudo yum install -y gitlab-ce

```
## 3. 修改    /etc/gitlab/gitlab.rb
```
external url ="ipaddress:port"
```
## 4. 更新，开启
```
sudo gitlab-ctl reconfigure

其他命令
gitlab-ctl start

gitlab-ctl stop

gitlab-ctl status

gitlab-ctl restart

```

ns1.alidns.com
