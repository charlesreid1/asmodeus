#include <stdio.h>
#include <time.h>

/*
 * This program prints the current date and the current time.
 */

int main(void) {

    // get the current time, C time type
    time_t t = time(NULL);

    // chunk it up into a struct 
    struct tm tm = *localtime(&t);

    // print each chunk
    printf("The current date is: %0.04d-%0.02d-%0.02d\n", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday);
    printf("The current time is: %0.02d:%0.02d:%0.02d\n", tm.tm_hour, tm.tm_min, tm.tm_sec);

    return 0;
}
