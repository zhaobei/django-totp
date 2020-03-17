export IMAGE=uhub.service.ucloud.cn/safehouse/django-frame-ci:0.0.2

docker build \
  -t $IMAGE \
  -f docker/ci/Dockerfile \
  . && \
  docker push $IMAGE
