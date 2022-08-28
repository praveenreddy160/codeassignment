input_file = "soccer.dat"
FOR_COL = "F"
AGAINST_COL = "A"
TEAM_COL = "Team"
START_INDEX = 0
MAX_DIFF = 1000
BLANK = ""


def read_soccer_data(input_file):

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
    if len(row.strip()) == START_INDEX:
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


def clean_col_value(value):
    return int(value.replace("-", "").strip())

def get_header_index(data_list):
    index = 0 
    while True:
        if TEAM_COL in data_list[index].strip():
            break
        index+=1
    return index

def calculate_min_diff(data_list):
    max_diff_record = [MAX_DIFF, START_INDEX]
    header_index = get_header_index(data_list)
    headers_with_indexes = get_headers_with_indexes(data_list[header_index])
    for row in data_list[header_index+1:]:
        cols = extract_cols(row, headers_with_indexes)
        if not len(cols):
            continue
        try:
            against = clean_col_value(cols[FOR_COL])
            for_goal = clean_col_value(cols[AGAINST_COL])
            diff = abs(against - for_goal)
        except:
            continue
        if diff < max_diff_record[START_INDEX]:
            max_diff_record[START_INDEX] = diff
            max_diff_record[1] = [against, for_goal, cols[TEAM_COL].strip()]
    return max_diff_record


if __name__ == "__main__":

    print(f"Reading the input file {input_file}")
    data = read_soccer_data(input_file)
    max_diff_record = calculate_min_diff(data)
    print(
        f"Team {max_diff_record[1][2]} with smallest difference is {max_diff_record[0]} and Goals for and against are {max_diff_record[1][0]} and {max_diff_record[1][1]}")
