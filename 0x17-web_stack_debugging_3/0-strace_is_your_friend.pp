#print paths and more info associated with file descriptors

openat(AT_FDCWD, "/dev/null", O_RDONLY) = 3</dev/null<char 1:3>>
fstat(3</dev/null<char 1:3>>, {st_mode=S_IFCHR|0666, st_rdev=makedev(0x1, 0x3),
...}) = 0
fadvise64(3</dev/null<char 1:3>>, 0, 0, POSIX_FADV_SEQUENTIAL) = 0
read(3</dev/null<char 1:3>>, "", 131072) = 0
