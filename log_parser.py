import argparse
import config

def parse_line(line):
    data = line.strip().strip('\n').split(' ')
    data = list(filter(None, data))
    return data


def parse_data(file):
    line = file.readline()
    headers = parse_line(line)

    if len(headers) < 1:
        return None
    for h in headers:
        if type(h) != str or len(h) < 1:
            return None
    data = dict()
    for h in headers:
        data[h] = list()

    # Parse
    lines = file.readlines()
    for l in lines:
        l = parse_line(l)
        for i, item in enumerate(l):
            if i > len(headers) - 1:
                raise Exception('Unable to parse logfile: unknown header')
            data[headers[i]].append(item)

    return data


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
