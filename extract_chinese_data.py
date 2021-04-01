import csv, sys, re


def extract_csv():
    in_file = open('parser.csv', mode='r')
    out_file = open('chinese.csv', mode='w')
    reader = csv.reader(in_file, delimiter=",")
    writer = csv.writer(out_file)
    for row in reader:
        if row[2] == 'Chinese':
            writer.writerow(row)
    in_file.close()
    out_file.close()


def extract_common_errors():
    in_file = open('chinese.csv', mode='r')
    out_file = open('chinese_errortypes.csv', mode='w')
    reader = csv.reader(in_file, delimiter=",")
    writer = csv.writer(out_file)
    error_types = {}
    for row in reader:
        if row[6] in error_types.keys():
            error_types[row[6]] += 1
        else:
            error_types[row[6]] = 1
    for error in error_types:
        line = [error, error_types[error]]
        writer.writerow(line)

    in_file.close()
    out_file.close()


def extract_error(error_type):
    in_file = open('chinese.csv', mode='r')
    out_file = open('chinese_'+error_type+'_errors.csv', mode='w')
    reader = csv.reader(in_file, delimiter=",")
    writer = csv.writer(out_file)

    match_regex = re.compile('(?<=<NS type="'+error_type.upper()+'">)(.+?)(?=<\/NS>)')
    sub_regex = re.compile('<NS type="'+error_type.upper()+'">(.+?)<\/NS>')
    prev_text = None
    for row in reader:
        if row[6] == error_type.upper():
            if row[5] != prev_text:
                raw_text = row[5]
                prev_text = row[5]
            match = re.search(match_regex, raw_text)
            raw_text = re.sub(sub_regex, ' ', raw_text, 1)
            if not match:
                match = ''
            else:
                match = match.group(0)
            new_row = row[0:7] + [match] + row[7:]
            writer.writerow(new_row)
    in_file.close()
    out_file.close()


def error_list(error_type):
    in_file = open('chinese_'+error_type+'_errors.csv', mode='r')
    out_file = open('chinese_'+error_type+'.csv', mode='w')
    reader = csv.reader(in_file, delimiter=",")
    writer = csv.writer(out_file)
    match_regex = re.compile('^<i>(.+?)</i><c>(.+?)</c>')
    i_regex = re.compile('(?<=<i>)(.+?)(?=</i>)')
    c_regex = re.compile('(?<=<c>)(.+?)(?=</c>)')
    for row in reader:
        match = re.search(match_regex, row[7])
        if match != None:
            incorrect = re.search(i_regex, match.group(0)).group(0)
            correct = re.search(c_regex, match.group(0)).group(0)
        else:
            incorrect = ''
            correct = ''
        writer.writerow([row[0], row[1], incorrect, correct])
    in_file.close()
    out_file.close()


if __name__ == "__main__":
    if sys.argv[1] == 'extract':
        extract_csv()
    elif sys.argv[1] == 'geterrors':
        extract_common_errors()
    elif sys.argv[1] == 'extracterror':
        extract_error(sys.argv[2])
    elif sys.argv[1] == 'corrections':
        error_list(sys.argv[2])
    else:
        print('invalid statement')