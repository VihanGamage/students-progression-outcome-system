#PART-1
ranges = [0, 20, 40, 60, 80, 100, 120]  #initialize credit ranges in array

progress = 0   #initialize progress count variable
trailer = 0    #initialize trailer count variable
exclude = 0    #initialize exclude count variable
retriever = 0  #initialize retriever count variable
count = 0      #initialize total outcomes count variable

progress_inputs = []    #initialize progress credit inputs array
trailer_inputs = []     #initialize trailer credit inputs array
exclude_inputs = []     #initialize exclude credit inputs array
retriever_inputs = []   #initialize retriever credit inputs array

while True:
    while True:
        try:
            Pass = int(input("Please enter your credits at pass : "))   #getting pass credit
            if Pass not in ranges:   #check input credits are in the range
                print("Out of range\n")
            else:
                break   #break the loop & go to next step
        except ValueError:
            print("Integer required\n")   #print Integer required

    while True:
        try:
            Defer = int(input("Please enter your credit at defer : "))  #getting defer credit
            if Defer not in ranges:  #check input credits are in the range
                print("Out of range\n")
            else:
                break   #break the loop & go to next step
        except ValueError:
            print("Integer required\n")   #print Integer required

    while True:
        try:
            Fail = int(input("Please enter your credit at fail : "))    #getting fail credit
            if Fail not in ranges:   #check input credits are in the range
                print("Out of range\n")
            else:
                break   #break the loop & go to next step
        except ValueError:
            print("Integer required\n")   #print Integer required

    total = Pass+Defer+Fail
    if total == 120:
        count = count+1   #increment count
        if Pass == 120:
            print("Progress")  #print progress
            progress_inputs.append([Pass, Defer, Fail])    #append to progress array
            progress = progress+1  #increment progress
        elif Pass == 100:
            print("Progress(module trailer)")  #print progress(module trailer)
            trailer_inputs.append([Pass, Defer, Fail])     #append to trailer array
            trailer = trailer+1   #increment trailer
        elif Fail >= 80:
            print("Exclude")  #print exclude
            exclude_inputs.append([Pass, Defer, Fail])    #append to exclude array
            exclude = exclude+1   #increment exclude
        else:
            print("Do not progress – module retriever")   #print module retriever
            retriever_inputs.append([Pass, Defer, Fail])    #append to retriever array
            retriever = retriever+1   #increment retriever
        print("\nWould you like to enter another set of data?")
        n = input("Enter 'y' for yes or 'q' to quit and view results: ")  #getting input to break or continue the loop
        print("")
        if n.lower() == "q":    #quit loop
            break
        elif n.lower() == "y":  #continue loop
            continue
    else:
        print("Total incorrect\n")  #print total incorrect

print("\nHorizontal Histogram")  #print Horizontal Histogram
print("Progress ", progress, "   : ", "*"*progress)    #print progress star
print("Trailer ", trailer, "    : ", "*"*trailer)      #print trailer star
print("Retriever ", retriever, "  : ", "*"*retriever)  #print retriever star
print("Excluded ", exclude, "   : ", "*"*exclude)      #print exclude star
print(f"\n{count} outcomes in total.")   #print total outcomes

#PART-2
print("\nProgress",progress,"  | Trailing",trailer,"  | Retriever",retriever,"  | Excluded",exclude)  #print vertical Histogram
while count > 0:
    if progress > 0:
        print(f"{'*':>5}", end="")    #print progress star
        progress = progress-1
        count = count-1
    else:
        print(f"{' ':>5}", end="")    #print progress blank

    if trailer > 0:
        print(f"{'*':>15}", end="")   #print trailer star
        trailer = trailer-1
        count = count-1
    else:
        print(f"{' ':>15}", end="")   #print trailer blank

    if retriever > 0:
        print(f"{'*':>15}", end="")   #print retriever star
        retriever = retriever-1
        count = count-1
    else:
        print(f"{' ':>15}", end="")   #print retriever blank

    if exclude > 0:
        print(f"{'*':>15}")    #print exclude star
        exclude = exclude-1
        count = count-1
    else:
        print(f"{' ':>15}")    #print exclude blank
print()

#PART-3
for p in progress_inputs:   #print progress credit inputs from respective array
    print("Progress - ", p)
for q in trailer_inputs:    #print trailer credit inputs from respective array
    print("Progress (module trailer) - ", q)
for r in retriever_inputs:  #print retriever credit inputs from respective array
    print("Module retriever - ", r)
for s in exclude_inputs:    #print exclude credit inputs from respective array
    print("Exclude - ", s)


#PART-4
def out_file():   #define function for save input data to text file
    output = open('output data.txt', 'w')     #open text file for write
    for a in progress_inputs:    #write progress credit inputs from respective array
        output.write("Progress - " + str(a)+'\n')
    for b in trailer_inputs:     #write trailer credit inputs from respective array
        output.write("Progress (module trailer) - " + str(b)+'\n')
    for c in retriever_inputs:   #write retriever credit inputs from respective array
        output.write("Module retriever - " + str(c)+'\n')
    for d in exclude_inputs:     #write exclude credit inputs from respective array
        output.write("Exclude - " + str(d)+'\n')
    output.close()   #close text file

    read_file = open('output data.txt', 'r')   #open text file for read
    print("\nstored data from output text file:")
    for line in read_file:
        print('\t'+line, end="")   #print stored credit inputs from saved text file
    read_file.close()  #close text file

out_file()   #calling function
