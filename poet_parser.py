''' Script for parsing and operating on the 'POET' log file '''

import argparse
import log_parser as LP
import config
import time
import math
import plotting.PoetPlotter as pp

from decimal import Decimal
log_data = {}

# Returns the hearbeat index deltas between rows
def heartbeat_window(log_data = log_data):
    ret = []
    key = 'HB_NUM'
    try:
        assert key in log_data, 'Log data does not contain \'%s\n\'' % key
        ret = list()

        prev = 0
        for idx, t in enumerate(log_data[key]):
            if idx == 0:
                prev = int(t)
                continue
            curr = int(t)
            diff = curr - prev
            prev = curr
            ret.append(diff)

    except Exception as e:
        print(e)
        ret = []

    return ret

# Returns a list of differences between the row values of two rows
def poet_difference(log_data, first_key, second_key, flip_first = False, flip_second = False):
    ret = []
    try:
        assert first_key in log_data, 'Log data does not contain \'%s\n\'' % first_key
        assert second_key in log_data, 'Log data does not contain \'%s\n\'' % second_key
        assert len(log_data[first_key]) == len(log_data[second_key]), "Not the same amount of (%s) and (%s)\n"

        for idx in range(len(log_data[first_key])):
            a = Decimal(log_data[first_key][idx])
            b = Decimal(log_data[second_key][idx])
            if flip_first:
                a = - a
            if flip_second:
                b = - b
            ret.append(a - b)

    except Exception as e:
        print(e)
        ret = []
        
    return ret

def plot_wanted_speed(log_data, normalize = False, window_size = 0) :
    x_key = 'HB_NUM'
    work_key = 'WORKLOAD'
    error_key = 'ERROR'
    try:
        assert x_key in log_data, 'Log data does not contain \'%s\n\'' % x_key
        assert work_key in log_data, 'Log data does not contain \'%s\n\'' % work_key
        assert error_key in log_data, 'Log data does not contain \'%s\n\'' % error_key

        x = list()
        y = list()
        if normalize :
            ws = window_size
            if ws == 0 :
                ws = int(log_data[x_key][1]) - int(log_data[x_key][0])

            for element in log_data[x_key] :
                x.append(int(element) / ws)
        else :
            x = log_data[x_key]

        for idx in range(len(log_data[work_key])) :
            dw = Decimal(log_data[work_key][idx])
            de = Decimal(log_data[error_key][idx])
            y.append(dw * de)

        pp.create_simple_fig(x, y)

    except Exception as e:
        print(e)

# Main function used when operating solely from this script
# UNSTABLE: Will change as tests are done on the script
def main():
    global log_data
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log_file_path', type=str,
                        help='Enter the path to the logfile you want to parse', default=config.POET_LOG)

    args = parser.parse_args()
    path = args.log_file_path        

    file = open(path, 'r')
    log_data = LP.parse_data(file)
    file.close()

    hb_num_differences = heartbeat_window(log_data)

    #for diff in hb_num_differences:
        #    d = diff % 30
        #    if d != 0:
        #        print (d)

    diff_rate_err = poet_difference(log_data, 'HB_RATE', 'ERROR', flip_second=True)
    plot_wanted_speed(log_data, normalize = True)

if __name__ == '__main__':
	main()
