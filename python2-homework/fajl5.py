with open('adat.txt', 'r') as f:
    for line in f:
        with open('real_time.txt', 'a') as r_t_f:  # Appends to the file
            r_t_f.write(line)