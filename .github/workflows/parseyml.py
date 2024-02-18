import yaml

def parse_yaml_file(filename, target_name):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
        
        for item in data:
            if 'name' in item and item['name'] == target_name:
                return item
        
        return None



filename = 'testApp.yml'
target_name = 'web'
result = parse_yaml_file(filename, target_name)

if result:
    print(f"Found {target_name}:")
    print(f"Age: {result['id']}")
    print(f"City: {result['app_permissions']}")
else:
    print(f"Could not find data for {target_name}.")



