# sumsize
A command-line utility that sums the given sizes. It can read from both stdin and files. To use it effectively, you can add it to your path:
```
ln -s dir_of_sumsize/main.py path_to_PATH/sumsize
```

Examples:
```
[xphyro@archlinux ~]$ alias pacman-list="LC_ALL=C pacman -Qi | awk "/^Name/{name=\$3} /^Installed Size/{print \$4\$5, name}""
[xphyro@archlinux ~]$ pacman-list | tail -n 5
396.52MiB texlive-core
488.44MiB go
499.03MiB wine
516.18MiB linux-firmware
4.04GiB cuda
[xphyro@archlinux ~]$ pacman-list | sumsize
20.62GiB
[xphyro@archlinux ~]$ pacman-list | sumsize -u 
22140504940 
[xphyro@archlinux ~]$ pacman-list > sizes
[xphyro@archlinux ~]$ sumsize -bf 3 sizes
22.141GB
[xphyro@archlinux ~]$ pacman-list | sumsize -df 4 sizes 
41.2399GiB 
[xphyro@archlinux ~]$ pacman-list | awk '{print $2,$1}' | sumsize -c 2
20.62GiB
```

Execute `sumsize -h` to get more information:
```
usage: sumsize [-h] [-b] [-u] [-f FIGURE] [-c COLUMN] [-d] [files [files ...]] 
Sum sizes. 
positional arguments: 
  files                 paths to files that contain the sizes. files have precedence over stdin unless -d option is given 
optional arguments: 
  -h, --help            show this help message and exit 
  -b, --useb            print in B instead of iB 
  -u, --unitless        total size is given unitless 
  -f FIGURE, --figure FIGURE 
                        significant figure count after the dot (default 2) 
  -c COLUMN, --column COLUMN 
                        which column to consider as sizes (default 1) 
  -d, --double-input    use both stdin and file if present 
```
