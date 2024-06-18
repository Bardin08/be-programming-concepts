import csv

# Read

tracks = []
with open('spotify.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for index, row in enumerate(csv_reader):
        if index == 0:
            continue

        tracks.append(row)

# Filter

filtered_tracks = list(filter(lambda r: r[2] == 'False', tracks))
print(len(filtered_tracks))

# Analyze
years = list(map(lambda r: r[3][:4], filtered_tracks))

years_distribution = {}
for year in years:
    if year in years_distribution:
        years_distribution[year] += 1
    else:
        years_distribution[year] = 1

ordered_years = list(sorted(years_distribution.items(), key=lambda x: x[1], reverse=True))

print([ordered_years[0][0]])

# Visualize
with open('results.txt', mode='w') as file:
    file.write(f'Most popular year: {ordered_years[0][0]}\n')
