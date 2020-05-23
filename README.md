# sumsize
A command-line utility that sums the given sizes. It can read from both stdin and a file. To use it effectively, add it to your path so that you can execute it anywhere.

Execute `sumsize -h` to get more information:
```
usage: sumsize [-h] [-b] [-u] [-f FIGURE] [-c COLUMN] [-i INPUT] 
Sum sizes. 
optional arguments: 
  -h, --help            show this help message and exit 
  -b, --useb            print in B instead of iB 
  -u, --unitless        total size is given unitless 
  -f FIGURE, --figure FIGURE 
                        significant figure count after the dot (default 2) 
  -c COLUMN, --column COLUMN 
                        which column to consider as sizes (default 1) 
  -i INPUT, --input INPUT 
                        read from file instead of stdin 
```
