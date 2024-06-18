import csv

# Read
rows = []
with open("spotify.csv", mode="r", encoding="utf8") as file:
    reader = csv.reader(file)

    for row_index, line in enumerate(reader):
        if row_index == 0:
            continue

        rows.append(line)

# Filter
filtered = []
for track in rows:
    if track[2] != "True":
        filtered.append(track)

# Analyze
print("Number of tracks:", len(filtered))
years_distribution = {}

for t in filtered:
    year = t[3][:4]
    if year in years_distribution:
        years_distribution[year] += 1
    else:
        years_distribution[year] = 1

years_distribution = dict(sorted(years_distribution.items(), key=lambda x: x[1], reverse=True))

print("Years distribution:")
for year, count in years_distribution.items():
    print(year, count)

print("Most popular year:", list(years_distribution.keys())[0])

# Write
with open("results.txt", mode="w", encoding="utf8") as file:
    file.write(f"Most popular year: {list(years_distribution.keys())[0]}")


print()
