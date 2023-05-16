import json

with open("sample_data.json") as file:

    input_data = json.load(file)
    output_list = [] 
    for each_parameter in input_data["parametersList"]:
        output_dict = {
            "parameterName": each_parameter["parameterName"],
            "min_value": each_parameter["min"],
            "max_value": each_parameter["max"],
            "avg_value": each_parameter["avg"]
        }
        output_list.append(output_dict)

json_data = json.dumps(output_list, indent=4)

with open("output_json_data.json", "w") as file1:
    file1.write(json_data)