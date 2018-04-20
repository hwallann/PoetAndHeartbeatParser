import argparse
import log_parser as LP
import config
import time
import math

log_data = {}

def convert_hearbeat_time_to_dates(log_data = log_data):
    ret = []
    key = 'Timestamp'

    try:
        assert key in log_data, 'Log data does not contain \'%s\n\'' % key
        ret = list()

        for t in log_data[key]:
            tmp = float(t)
            tmp = tmp / (math.pow(10,9))
            tmp_time = time.localtime(tmp)
            s_time = time.strftime("%a, %d %b %Y %H:%M:%S Localtime", tmp_time)
            ret.append(s_time)

    except Exception as e:
        print(e)
        ret = []

    return ret

def main():
    global log_data
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log_file_path', type=str,
                        help='Enter the path to the logfile you want to parse', default=config.HEARTBEAT_LOG)

    args = parser.parse_args()
    path = args.log_file_path        

    file = open(path, 'r')
    log_data = LP.parse_data(file)
    file.close()

    times = convert_hearbeat_time_to_dates(log_data)

    #if len(times) > 0:
    #    print ("First and last: %s\t%s\n" % (ret[0], ret[-1]))

if __name__ == '__main__':
	main()
