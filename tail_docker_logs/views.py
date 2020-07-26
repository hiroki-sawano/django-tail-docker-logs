import time
from datetime import datetime

import docker
from django.http import StreamingHttpResponse


def tail_log(request, container_name):
    client = docker.from_env()
    container = client.containers.get(container_name)
    return StreamingHttpResponse(
        _stream_docker_logs(container),
        content_type='text/event-stream'
    )


def _stream_docker_logs(container):
    for line in container.logs(
            stream=True, since=datetime.utcfromtimestamp(time.time())):
        yield 'data: {}\n\n'.format(line.decode('utf-8'))
        time.sleep(0.1)
