
ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
invalid_IDs = []
for someRange in (ranges.split(",")):
    
    bound = someRange.split("-")
    print(bound)

    lowBound = int(bound[0])

    for i in range(len(bound[0]), len(bound[1])+1):
        repeats=[]
        highBound = int("9" * i)
        sub_bound = [str(lowBound),str(min(highBound,int(bound[1])))]
        lowBound = 10**i
        print("\t",sub_bound)

        #print(f"\tDigits: {[len(sub_bound[0]),len(sub_bound[1])]}")
    
        if len(sub_bound[0]) != len(sub_bound[1]):
            print("\tSKIP for now...")
            continue
        else:
            digits = len(sub_bound[0])
            if digits % 2 == 0:
            
                repeat_masks = [str(10**(digits//2-1))+"1"]
                print(f"\tMasks : {repeat_masks}")
                for mask in repeat_masks:
                    for whole_div in range(int(sub_bound[0])//int(mask),int(sub_bound[1])//int(mask)):
                        repeats.append(int((whole_div+1)*int(mask)))
                if int(sub_bound[0])%int(mask)==0:
                    repeats.append(int(sub_bound[0]))
                if int(sub_bound[1])%int(mask)==0:
                    repeats.append(int(sub_bound[1]))
                repeats.sort()
                repeats = list(dict.fromkeys(repeats))
                print(f"\tRepeats: {repeats}")
                invalid_IDs += repeats

invalid_IDs = list(dict.fromkeys(invalid_IDs))
invalid_IDs.sort()
print(f"Invalid ID list: {invalid_IDs}")
print(f"sum: {sum(invalid_IDs)}")
REAL_invalid_IDs = []
for invalidID in invalid_IDs:
    throwaway = str(invalidID)
    if (throwaway[0:(len(throwaway)//2)] == throwaway[(len(throwaway)//2):]):
        REAL_invalid_IDs.append(int(throwaway))

REAL_invalid_IDs = list(dict.fromkeys(REAL_invalid_IDs))
REAL_invalid_IDs.sort()
print(f"REAL Invalid ID list: {REAL_invalid_IDs}")
print(f"sum: {sum(REAL_invalid_IDs)}")
