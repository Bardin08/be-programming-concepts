import csv

datasets = []

with open('datasources.txt', mode='r') as datasources:
    for line_index, line in enumerate(datasources.readlines()):
        print(f"{line_index + 1}. {line.strip()}")
        datasets.append(line)

dataset_number = input('Enter dataset number: ')
dataset_index = int(dataset_number) - 1
selected_dataset = datasets[dataset_index].strip()

print(f"selected dataset is: {selected_dataset}")

tracks = []
with open(selected_dataset, 'r') as dataset:
    for line_index, line in enumerate(csv.reader(dataset)):
        if line_index == 0:
            continue

        tracks.append(line)

print(tracks)

years_distribution = {}

for t in tracks:
    year = t[3][:4]
    if year in years_distribution:
        years_distribution[year] += 1
    else:
        years_distribution[year] = 1

years_distribution = dict(sorted(years_distribution.items(), key=lambda x: x[1], reverse=True))
top_year = list(years_distribution.items())[0]

with open('results.txt', 'a') as file:
    file.write(f"Datasource: {selected_dataset}, Result: {top_year}\n")