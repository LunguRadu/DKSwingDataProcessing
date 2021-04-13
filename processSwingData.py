# This is a submission for the Diamond Kinetics codding challenge by Radu Lungu.
# This script processes the data from a three-axis accelerometer and a three-axis gyroscope.
# Run the main method to see the output results
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from numpy import genfromtxt


def processData(path):
    """
    Method to copy the data from the CSV file into a numpy array
    :param path:
    :return: numpy array
    """
    my_data = genfromtxt(path, delimiter=',')
    my_data = np.array(my_data, order='F')
    return my_data


def searchContinuityAboveValue(data, index_begin, index_end, threshold, win_length):
    """
    From indexBegin to indexEnd, this function searches data for values that are higher than threshold.
    :param data: data input
    :param index_begin
    :param index_end
    :param threshold
    :param win_length
    :return: the first index where data has values that meet this criteria for at least winLength samples in a row.
             None if the criteria is not meet
    """
    start_pointer = index_begin
    end_pointer = index_begin
    continuity_count = 0

    while start_pointer < index_end and end_pointer < index_end:
        current_value = data[end_pointer]
        if current_value > threshold:  # if threshold condition, move pointer up, increase the count
            end_pointer += 1
            continuity_count += 1
        else:  # else, reset the start and end pointer and the count
            end_pointer += 1
            start_pointer = end_pointer
            continuity_count = 0
        if continuity_count == win_length:
            return start_pointer
    return None


def backSearchContinuityWithinRange(data, index_begin, index_end, threshold_lo, threshold_hi, win_length):
    """
    From indexBegin to indexEnd (where indexBegin is larger than indexEnd), search data for values that are higher than
    thresholdLo and lower than thresholdHi.
    :param data: data input
    :param index_begin
    :param index_end
    :param threshold_lo
    :param threshold_hi
    :param win_length
    :return: the first index where data has values that meet this criteria for at least winLength samples in a row,
             None if the criteria is not meet
    """
    start_pointer = index_begin
    end_pointer = index_begin
    continuity_count = 0

    while start_pointer >= index_end and end_pointer >= index_end:
        current_value = data[end_pointer]
        if threshold_lo < current_value < threshold_hi:  # if threshold condition, move pointer down increase the count
            end_pointer -= 1
            continuity_count += 1
        else:  # else, reset the start and end pointer and the count
            end_pointer -= 1
            start_pointer = end_pointer
            continuity_count = 0
        if continuity_count == win_length:
            return start_pointer
    return None


def searchContinuityAboveValueTwoSignals(data1, data2, index_begin, index_end, threshold_1, threshold_2, win_length):
    """
    From indexBegin to indexEnd, search data1 for values that are higher than threshold1 and also search data2 for values
    that are higher than threshold2.
    :param: data1
    :param: data2
    :param: index_begin
    :param: index_end
    :param: threshold_1
    :param: threshold_2
    :param: win_length
    Return the first index where both data1 and data2 have values that meet these criteria for at least winLength
    samples in a row. Return None if the condition is not meet
    """
    start_pointer = index_begin
    end_pointer = index_begin
    continuity_count = 0
    while start_pointer < index_end and end_pointer < index_end:
        current_value1 = data1[end_pointer]
        current_value2 = data2[end_pointer]
        if current_value1 > threshold_1 and current_value2 > threshold_2:
            end_pointer += 1
            continuity_count += 1
        else:
            end_pointer += 1
            start_pointer = end_pointer
            continuity_count = 0
        if continuity_count == win_length:
            return continuity_count
    return None


def searchMultiContinuityWithinRange(data, index_begin, index_end, threshold_lo, threshold_hi, win_length):
    """
    From indexBegin to indexEnd, search data for values that are higher than thresholdLo and lower than thresholdHi.
    :param index_end
    :param data
    :param index_begin
    :param threshold_lo
    :param threshold_hi
    :param win_length
    Return the the starting index and ending index of all continuous samples that meet this criteria for at least
    winLength data points.
    """
    start_pointer = index_begin
    end_pointer = index_begin
    continuity_count = 0
    index_list = []
    while start_pointer < index_end and end_pointer < index_end:
        current_value = data[end_pointer]
        if threshold_lo < current_value < threshold_hi:
            end_pointer += 1
            continuity_count += 1
        else:
            end_pointer += 1
            start_pointer = end_pointer
            continuity_count = 0

        if continuity_count == win_length:
            start_end_index = (start_pointer, end_pointer)  # put the information into a tuple
            index_list.append(start_end_index)

            start_pointer += 1
            continuity_count -= 1

    return index_list


def extract_column(data, column_index):
    """

    :param data:
    :param column_index:
    :return: a separate, specific column from the dataset
    """
    if column_index == 0:
        return [int(item) for item in data[:, 0]]  # function to normalize the timestamp after modified by numpy
    else:
        return data[:, column_index]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    To retrieve the columns use the following indices for the extract column function:
    0 -> timestamp 
    1 -> ax
    2 -> ay
    3 -> az
    4 -> wx
    5 -> wy
    6 -> wz
    """
    data_path = "data/latestSwing.csv"
    swing_data = processData(data_path)

    # Examples of calling the function
    print(searchContinuityAboveValue(extract_column(swing_data, 1), 0, 1200, 1.1, 5))
    print(backSearchContinuityWithinRange(extract_column(swing_data, 2), 500, 100, 0.3, 0.5, 5))
    print(
        searchContinuityAboveValueTwoSignals(extract_column(swing_data, 3), extract_column(swing_data, 4), 0, 1250, -1,
                                             1.5, 15))
    print(searchMultiContinuityWithinRange(extract_column(swing_data, 5), 0, 1250, -5, 1, 50))
