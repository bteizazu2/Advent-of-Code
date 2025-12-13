####DAY 7 (finished)######

 
with open(r"C:\Users\bonss\Downloads\Day_7.txt", "r") as file:

    first_pass = True
    split_sum = 0
    for line in file:

        # line includes the newline character (\n) at the end

        # Use .strip() to remove leading/trailing whitespace, including newline

        row = line.strip()

        #print(row)

        if first_pass:

            r_len = len(row)

            beams = '0'*len(row)

            assert row[len(row)//2] == "S"

            beams = beams[0:len(row)//2] + '1' + beams[len(row)//2+1:]
            beams=int(beams,2)

            first_pass = False

           

            continue

       

        def left_shift(num,size):

            return (num << 1) % 2**size

        def right_shift(num,size):

            return (num >> 1) % 2**size

        def bitwise_not(num, size):

            return (2**size - 1) - num

        binary_mask = row.replace('.', '0')
        binary_mask = int(binary_mask.replace('^', '1'),2)
        #print(f"{beams:0{r_len}b}\n{binary_mask:0{r_len}b}\n")
        splits = beams & binary_mask
        

        beams = left_shift(splits,r_len) | right_shift(splits,r_len) | (beams & bitwise_not(binary_mask,r_len))
        
        while (splits != 0) :
            split_sum += splits % 2
            splits = splits >> 1

        #print(f"{newNum:0{r_len}b}")

        print(split_sum)
