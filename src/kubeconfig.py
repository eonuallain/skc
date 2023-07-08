import os
import yaml

KUBECONFIG = 'KUBECONFIG'


def config_defined():
    return KUBECONFIG in os.environ


def get_config_path():
    return os.environ[KUBECONFIG]


def get_default_config_path():
    home = os.path.expanduser('~')
    config_path = os.path.join(home, '.kube', 'config')
    return config_path


def default_config_exists():
    config_path = get_default_config_path()
    config_path_exists = os.path.isfile(config_path)
    return config_path_exists


def get_config(config_path):
    with open(config_path, 'r') as file:
        config_dict = yaml.safe_load(file)

    return config_dict


def list_contexts(config):
    print(config.keys())


def get_clusters():
    config_path = ''
    if config_defined():
        config_path = get_config_path()
    else:
        if default_config_exists():
            config_path = get_default_config_path()

    config = get_config(config_path)
    return config['clusters']