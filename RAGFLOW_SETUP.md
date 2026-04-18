# RagFlow Docker 部署

## 报错

| 容器循环重启 | 缺少 nginx 配置文件 | 挂载本地 nginx 配置 |
| 显示 nginx 默认页 | sites-enabled/default 干扰 | 删除默认站点 |

## 修改文件

### 1. docker-compose-base.yml
镜像改为华为云：

sudo docker pull swr.cn-north-4.myhuaweicloud.com/infiniflow/ragflow:latest


```yaml
es01: swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}
mysql: swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/library/mysql:8.0.39
redis: swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/library/redis:7-alpine
minio: swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/minio/minio:latest
```

### 2. .env
```
RAGFLOW_IMAGE=swr.cn-north-4.myhuaweicloud.com/infiniflow/ragflow:latest
```

### 3. docker-compose.yml
取消注释 volumes：
```yaml
- ./nginx/ragflow.conf.python:/etc/nginx/conf.d/ragflow.conf.python:ro
- ./nginx/ragflow.conf.golang:/etc/nginx/conf.d/ragflow.conf.golang:ro
- ./nginx/ragflow.conf.hybrid:/etc/nginx/conf.d/ragflow.conf.hybrid:ro
- ./nginx/proxy.conf:/etc/nginx/proxy.conf:ro
```


## 启动命令

```bash
sed -i '1i DEVICE=gpu' .env #GPU
sudo docker-compose -f docker-compose.yml up -d

#关
sudo docker-compose -f docker-compose.yml down
#sudo /usr/local/bin/docker-compose -f docker-compose.yml down
```

## 删除默认站点

```bash
sudo docker exec docker-ragflow-cpu-1 rm /etc/nginx/sites-enabled/default
sudo docker exec docker-ragflow-cpu-1 nginx -s reload
```


