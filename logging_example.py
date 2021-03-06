import logging


def analyze_data_file(filename): 
    in_file = open(filename, 'r')
    keep_reading = True 
    line_number = 0
    while keep_reading: 
        data_line = in_file.readline()
        if data_line == "":
            keep_reading = False
        else:
            line_number += 1 
            process_line(data_line)
    in_file.close()


def process_line(data_line):
    data_points = data_line.strip('\n').split(',')
    print(data_line)
    if len(data_points) < 5:
        logging.warning("This line has less than 5 data points".formate(line_no))
    data_numbers = [float(i) for i in data_points]
    if any(i < 0 for i in data_numbers):
        logging.error("the line {} had a negative number".format(line_no))
    if all(1.0 <= i <= 4.0 for i in data_numbers):
        pass 
    else: 
        logging.info("Line {} was out of range".formate(line_no))


if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    analyze_data_file("logging_data.txt")