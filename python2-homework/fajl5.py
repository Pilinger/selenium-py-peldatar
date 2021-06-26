first_line = True

with open('adat.txt', 'r') as f: # opens adat.txt for reading (line by line)
    for line in f:
        if first_line:  # checking if first line and opening for writing to truncate the file
            first_line = False
            with open('real_time.txt', 'w') as r_t_f:
                r_t_f.write(line)
        else:  # otherwise opening in append mode
            with open('real_time.txt', 'a') as r_t_f:
                r_t_f.write(line)