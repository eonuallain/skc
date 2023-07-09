from kubernetes import client, config

config.load_kube_config()

api_instance = client.CoreV1Api()
node_list = api_instance.list_node()

for node in node_list.items:
	print(node.metadata.name)