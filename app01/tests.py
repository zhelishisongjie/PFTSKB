from django.test import TestCase
links = [{'source': 'Abdominal Surgery', 'target': 'Intraoperative', 'value': 98}, {'source': 'Urological Surgery', 'target': 'Intraoperative', 'value': 5}, {'source': 'Vascular Surgery', 'target': 'Intraoperative', 'value': 5}, {'source': 'Gynecological Surgery', 'target': 'Intraoperative', 'value': 9}, {'source': 'Abdominal Surgery', 'target': 'Postoperative', 'value': 23}, {'source': 'Abdominal Surgery', 'target': 'Preoperative', 'value': 4}, {'source': 'Orthopedic Surgery', 'target': 'Intraoperative', 'value': 4}, {'source': 'Vascular Surgery', 'target': 'Postoperative', 'value': 1}, {'source': 'Orthopedic Surgery', 'target': 'Postoperative', 'value': 1}, {'source': 'Thoracic Surgery', 'target': 'Intraoperative', 'value': 1}, {'source': 'Intraoperative', 'target': 'Fluid Volume Estimation', 'value': 98}, {'source': 'Postoperative', 'target': 'Fluid Volume Estimation', 'value': 23}, {'source': 'Preoperative', 'target': 'Fluid Volume Estimation', 'value': 4}, {'source': 'Fluid Volume Estimation', 'target': 'Ppv', 'value': 5}, {'source': 'Fluid Volume Estimation', 'target': 'Svv', 'value': 10}, {'source': 'Fluid Volume Estimation', 'target': 'Cvp', 'value': 15}, {'source': 'Fluid Volume Estimation', 'target': 'Ci', 'value': 9}, {'source': 'Fluid Volume Estimation', 'target': 'Sv', 'value': 27}, {'source': 'Fluid Volume Estimation', 'target': 'Blood Flow Time', 'value': 2}, {'source': 'Fluid Volume Estimation', 'target': 'Map', 'value': 26}, {'source': 'Fluid Volume Estimation', 'target': 'Svi', 'value': 4}, {'source': 'Fluid Volume Estimation', 'target': 'Standard Haemodynamic Parameters', 'value': 2}, {'source': 'Fluid Volume Estimation', 'target': 'Ftc', 'value': 6}, {'source': 'Fluid Volume Estimation', 'target': 'Pvi', 'value': 3}, {'source': 'Fluid Volume Estimation', 'target': '△Pv', 'value': 4}, {'source': 'Fluid Volume Estimation', 'target': 'Ivc Respiratory Variation', 'value': 1}, {'source': 'Fluid Volume Estimation', 'target': 'Paop', 'value': 6}, {'source': 'Fluid Volume Estimation', 'target': 'Pam', 'value': 1}]
nodes = ['Thoracic Surgery', '△Pv', 'Blood Flow Time', 'Urological Surgery', 'Svi', 'Fluid Volume Estimation', 'Paop', 'Svv', 'Vascular Surgery', 'Postoperative', 'Ci', 'Intraoperative', 'Pvi', 'Preoperative', 'Sv', 'Ppv', 'Ivc Respiratory Variation', 'Gynecological Surgery', 'Abdominal Surgery', 'Orthopedic Surgery', 'Cvp', 'Ftc', 'Pam', 'Standard Haemodynamic Parameters', 'Map']

option_dict = {
    'classification_of_fluid_therapy_parameters': ['Hemodynamic parameters'],
    'application': ['Fluid volume estimation'],
    'surgery_type': ['Abdominal surgery']
}

# 更新选项以匹配links和nodes中的大小写
option_dict['application'] = [option.title() for option in option_dict['application']]
option_dict['surgery_type'] = [option.title() for option in option_dict['surgery_type']]

# 过滤nodes
filtered_nodes = [node for node in nodes if node in option_dict['application'] or node in option_dict['surgery_type']]

# 过滤links
filtered_links = []
for link in links:
    if (link['source'] in option_dict['application'] or link['source'] in option_dict['surgery_type']) and \
       (link['target'] in option_dict['application'] or 'operative' in link['target'].lower()):
        filtered_links.append(link)
    elif (link['target'] in option_dict['application'] or link['target'] in option_dict['surgery_type']) and \
         (link['source'] in option_dict['application'] or 'operative' in link['source'].lower()):
        filtered_links.append(link)

# 打印结果
print("Filtered Nodes:")
print(filtered_nodes)
print("\nFiltered Links:")
print(filtered_links)




