import argparse
import config

'''
Function for parsing a singe line from a "standard" log file.
The standard being the way 'POET' logs and 'Heartbeat' logs are set up.
'''
def parse_line(line):
    data = line.strip().strip('\n').split(' ')
    data = list(filter(None, data))
    return data


def parse_data(file):
    line = file.readline()

    # Parse headers
    headers = parse_line(line)

    # Make sure headers are as expected
    if len(headers) < 1:
        return None
    for h in headers:
        if type(h) != str or len(h) < 1:
            return None
    data = dict()

    # Create a list for each header
    for h in headers:
        data[h] = list()

    # Parse data
    lines = file.readlines()
    for l in lines:
        l = parse_line(l)
        for i, item in enumerate(l):
            if i > len(headers) - 1:
                raise Exception('Unable to parse logfile: unknown header')
            data[headers[i]].append(item)

    return data

'''
Opens a log file and creates a dictionary of lists.
The keys are the header of a row and 'value[i]' is the value of row 'i' for  'dict[key]'
Returns an empty dictionary if something fails
'''
def collect_log_data(path) :
    log_data = dict()

    try:
        file = open(log_file, 'r')
        log_data = parse_data(file)
        file.close()
    except:
        log_data = dict()

    return log_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--log_type', type=str,
                        help='Choose between heartbeat (h) or poet (p) log', default='p')
    parser.add_argument('-l', '--log_file_path', type=str,
                        help='Enter the path to the logfile you want to parse', default=None)
    args = parser.parse_args()
    log_type = args.log_type.lower()
    path = args.log_file_path

    if path == None:
        log_file = config.HEARTBEAT_LOG
        if log_type == 'p' or log_type == 'poet':
            log_file = config.POET_LOG

    file = open(log_file, 'r')
    log_data = parse_data(file)
    file.close()

    # print(log_data)

if __name__ == '__main__':
    main()
