import argparse

parser = argparse.ArgumentParser(description="Parse and transform data from an input file to an output file.")
parser.add_argument('--input', type=str, required=True, help='Input file path')
parser.add_argument('--output', type=str, required=True, help='Output file path')
args = parser.parse_args()

input_file = args.input
output_file = args.output

with open(input_file, 'r') as file:
    lines = file.read().splitlines()

with open(output_file, "w") as file:
    for line in lines:
        image_path = line.split(":")[3].split("/")[-1]
        label = line.split(":")[-1].split(",")[0].replace("(","").replace("'","")
        file.write(f"{image_path}\t{label}\n")

print(f"Data has been parsed and written to {output_file}.")
