from kubernetes import client, config

config.load_kube_config()

api_instance = client.CoreV1Api()
node_list = api_instance.list_node()

for node in node_list.items:
	node_name = node.metadata.name
	labels = node.metadata.labels
	status = api_instance.read_node_status(node_name)

	print(f"Node\t: {node_name}")
	#print(f"labels {labels}")
	#print(f"status {status}")
	#print(type(status))

	conditions = status.status.conditions
	#print(type(conditions))
	for condition in conditions:
		if "Ready" == condition.type:
			print(f"Ready\t: {condition.status}")