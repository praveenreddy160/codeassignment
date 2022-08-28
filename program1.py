
input_file = "w_data.dat"
MAX_TEMP_COL = "MxT"
MIN_TEMP_COL = "MnT"
DAY_COL = "Dy"
START_INDEX = 0
BLANK = ""
START_TEXT = "<pre>"
END_TEXT = '</pre>'



def read_weather_data(input_file):

    with open(input_file, "r") as fb_obj:
        data = fb_obj.readlines()
    return data


def get_headers_with_indexes(header):
    start = START_INDEX
    end = START_INDEX
    start_flag = False
    header_indexs = []
    for index in range(len(header)):
        ch = header[index]
        if ch.strip() != BLANK:

            if not start_flag:
                if start > START_INDEX:
                    header_indexs.append(
                        [header[start:end].strip(), start, end])
                start_flag = True
                start = index
        else:
            start_flag = False
            end = index
    header_indexs.append([header[start:end].strip(), start, end])
    return header_indexs


def extract_cols(row, headers):
    records = []
    if len(row.strip()) in [BLANK,END_TEXT] :
        return records
    header_map = {}
    index = START_INDEX
    for header in headers:
        try:
            value = row[header[1]:header[2]].strip()
            header_map[header[START_INDEX]] = value
        except Exception as e:
            break
    return header_map

def get_header_index(data_list):
    index = 0 
    while True:
        if MIN_TEMP_COL in data_list[index].strip():
            break
        index+=1
    return index

def calculate_max_diff(data_list):
    max_diff_record = [START_INDEX, START_INDEX]
    header_index = get_header_index(data_list)
    headers_with_indexes = get_headers_with_indexes(data_list[header_index])
    for row in data_list[header_index + 1:]:
        cols = extract_cols(row, headers_with_indexes)
        if not len(cols):
            continue
        try:
            diff = int(cols[MAX_TEMP_COL]) - int(cols[MIN_TEMP_COL])
        except:
            continue
        if diff > max_diff_record[START_INDEX]:
            max_diff_record[START_INDEX] = diff
            max_diff_record[1] = [int(cols[MAX_TEMP_COL]), int(
                cols[MIN_TEMP_COL]), cols[DAY_COL]]
    return max_diff_record


if __name__ == "__main__":

    print(f"Reading the input file {input_file}")
    data = read_weather_data(input_file)
    max_diff_record = calculate_max_diff(data)
    print(
        f"Day number {max_diff_record[1][2]} with max temperature spread is {max_diff_record[0]} and Max and Min temperature are {max_diff_record[1][0]} and {max_diff_record[1][1]}")
