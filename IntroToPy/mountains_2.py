import ast
def load_mountains(mountains_file):
    countries_map = {}
    count = 0
    with open(mountains_file, "r", encoding="utf-8") as data_file:
        for line in data_file.readlines():
            line_parts = line.split("\t")
            height_name=(line_parts[1])
            mountains_name = (line_parts[0])
            country_name=(line_parts[3])
            if height_name == "NULL":
                count_0_height += 1
            if country_name not in countries_map:
                countries_map[country_name] = []
            countries_map[country_name].append(mountains_name)
            count += 1
    return countries_map, count,count_0_height

if __name__ == "__main__":
    countries_map, count ,count_0_height = load_mountains("IntroToPy/mountains_db.tsv")
    print(f"Loaded {len(countries_map.keys())} unique countries containing {count} iterations")
    print(f"For {count_0_height} mountains, the height is unknown")