import os
import yaml

KUBECONFIG = 'KUBECONFIG'


def config_defined():
    return KUBECONFIG in os.environ


def get_config():
    kube_config = os.environ[KUBECONFIG]
    print(kube_config)

    with open(kube_config, 'r') as file:
        config_dict = yaml.safe_load(file)

    return config_dict

