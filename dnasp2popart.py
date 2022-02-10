from collections import defaultdict
import re

data = defaultdict(lambda : 0)
hap_list = set()

with open("16S.arp", "r") as f:
    sample_array = f.read().split("}\n")
    for sample in sample_array:
        sample_data = sample.split("\n")
        if len(sample_data[0].split('"'))>1:
            # Sample name
            sample_name = sample_data[0].split('"')[1]
            data[sample_name] = defaultdict(lambda : 0);
            data[sample_name]["sample_size"] = sample_data[1].split('=')[1].strip()
            for hap in sample_data[3:]:
                if hap:
                    data[sample_name][hap.split()[0].strip()] = hap.split()[1].strip()
                    hap_list.add(hap.split()[0].strip())

with open("output.csv", "w+") as f:
    hap_list = sorted(list(hap_list), key=lambda x : int(x.split('_')[1]))
    key_list = sorted(data.keys())
    f.write("sample_name, " + ", ".join(key_list) + "\n")
    f.write("sample_size, " + ", ".join([data[key]["sample_size"] for key in key_list]) + "\n")
    for hap in hap_list:
        f.write(hap)
        for key in key_list:
            f.write(", " + str(data[key][hap]))
        f.write("\n")
