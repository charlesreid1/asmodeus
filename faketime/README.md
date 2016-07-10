# Libfaketime Stuff

This contains a few files for testing out libfaketime functionality. For more info
on what libfaketime is, see the [libfaketime repo on Github](https://github.com/wolfcw/libfaketime).

`what_time_is_it.c` is a simple C program that prints the current date and time.

To run it like normal, just compile with gcc and run:

```
$ gcc what_time_is_it.cc -o whattime
$ ./whattime
The current date is: 2016-07-09
The current time is: 20:09:02
```

To run it through libfaketime to set a custom date and time, use the faketime wrapper:

```
$ gcc what_time_is_it.cc -o whattime
$ faketime '2002-12-25 08:01:15' ./whattime
The current date is: 2002-12-25
The current time is: 08:01:15
```


