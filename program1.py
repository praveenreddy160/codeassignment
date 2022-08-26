
input_file = "w_data.dat"


def read_weather_data(input_file):

    with open(input_file, "r") as fb_obj:
        data = fb_obj.readlines()
    return data


def extract_cols(row):
    rows = row.split(" ")
    if len(rows) < 10:
        return False
    records = []
    index = 0
    while len(records) < 3:
        try:
            value = rows[index].strip()
            index += 1
            if len(value) and int(value):
                records.append(int(value))
        except Exception as e:
            break
    return records if len(records) == 3 else []


def calculate_max_diff(data_list):
    max_diff_record = [0, 0]
    for row in data_list:
        cols = extract_cols(row)
        if not cols:
            continue
        diff = cols[1] - cols[2]
        if diff > max_diff_record[0]:
            max_diff_record[0] = diff
            max_diff_record[1] = cols
    return max_diff_record


if __name__ == "__main__":

    print(f"Reading the input file {input_file}")
    data = read_weather_data(input_file)
    max_diff_record = calculate_max_diff(data)
    print(max_diff_record)
    print(
        f"Day number with max temperature spread is {max_diff_record[0]} and Max and Min temperature are {max_diff_record[1][1]} and {max_diff_record[1][2]}")
