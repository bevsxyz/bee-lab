from pathlib import Path
import sys, re
output = open("/home/chain-ed-reaction/project/Result.csv", "a+")
with open( '/home/chain-ed-reaction/Videos/Bevan/Part_1.txt','r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('\tIteration'):
            temp = re.search(r'\d+', str(line.strip())).group()
            Iteration = ""
            Iteration = list(Iteration.join(temp))
            row1 = lines[i + 1].splitlines()
            row2 = lines[i + 2].splitlines()
            row3 = lines[i + 3].splitlines()
            row4 = lines[i + 4].splitlines()
            row5 = lines[i + 5].splitlines()
            row6 = lines[i + 6].splitlines()
            row7 = lines[i + 7].splitlines()
            row8 = lines[i + 8].splitlines()
            Onetime = Iteration + row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8
            s = ""
            s = s.join(Onetime)
            output.write(s + "\n")
            print(Iteration)
            #print(lines)
            print(line,s)
