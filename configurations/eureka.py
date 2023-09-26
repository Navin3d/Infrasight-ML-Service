import py_eureka_client.eureka_client as eureka_client

EUREKA_HOST = "172.31.98.42"


def register():
    your_rest_server_port = 8000
    eureka_client.init(eureka_server=f"http://{EUREKA_HOST}:8010/eureka",
                       app_name="Infrasight-ML-Service",
                       instance_host="172.31.99.12",
                       instance_port=your_rest_server_port)
