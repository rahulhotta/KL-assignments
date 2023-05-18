import json
import datetime
with open("sample_data.json") as file:

    input_data = json.load(file)
    output_data = {}
    for each_parameter in input_data["parametersList"]:
        json_key = each_parameter['parameterName']
        sparkListDateTime = each_parameter['sparkListTime']
        sparkListDateEpoch = []

        inner_dict = {}
        sparklist = each_parameter['sparkList']
        sparklistsum = 0
        for ele in sparklist:
            try:
                if ele != "NA":
                    sparklistsum = sparklistsum + int(ele)
            except Exception as e:
                print(e.args)
        for ele in sparkListDateTime:
            # date = datetime.datetime.strptime(ele, "%Y-%m-%d %H:%M").strftime("%Y,%m,%d")
            year = datetime.datetime.strptime(ele, "%Y-%m-%d %H:%M").strftime("%Y")
            month = datetime.datetime.strptime(ele, "%Y-%m-%d %H:%M").strftime("%m")
            date = datetime.datetime.strptime(ele, "%Y-%m-%d %H:%M").strftime("%d")
            hour = datetime.datetime.strptime(ele, "%Y-%m-%d %H:%M").strftime("%H")
            minute = datetime.datetime.strptime(ele, "%Y-%m-%d %H:%M").strftime("%M")
            try:
                output = datetime.datetime(int(year),int(month),int(date),int(hour),int(minute)).timestamp()
                sparkListDateEpoch.append(output)
            except Exception as e:
                print(e.args)

        print(sparklistsum)
        inner_dict["sparklistSum"] = sparklistsum
        inner_dict["sparkListDateEpoch"] = sparkListDateEpoch
        output_data[json_key] = inner_dict
json_data = json.dumps(output_data, indent=4)

with open("output_json_data2.json", "w") as file1:
    file1.write(json_data)