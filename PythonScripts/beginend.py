def beginend(inputlist):
    input_list = [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1]

    zeros_beginnings = []
    zeros_endings = []

    start_index = None

    for i in range(len(input_list)):
        element = input_list[i]
        if element == 0 and start_index is None:
            start_index = i
        elif element == 1 and start_index is not None:
            zeros_beginnings.append(start_index)
            zeros_endings.append(i-1)
            start_index = None

    if start_index is not None:
        zeros_beginnings.append(start_index)
        zeros_endings.append(len(input_list)-1)
    
    return zeros_beginnings, zeros_endings