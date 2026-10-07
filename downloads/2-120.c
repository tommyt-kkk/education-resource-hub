/* CS100 Fall 2026 - HW1 Problem 2: Find Bugs!
 *
 * BinB's buggy program is in the handout. Put your FIXED program here.
 * Do not rename this file: the autograder builds p2.c.
 */
#include <stdio.h>

int main(void){
    /* TODO: your fixed code here */


    printf("How many students are there?\n");
    int num;

    if(scanf("%d", &num) != 1){
        return 1;
    }

    printf("What are their scores?\n");

    // We programmers count from zero!
    double sum, score;
    sum = 0.0;
    for (int i = 0; i <= num-1; i++){
       
        scanf("%lf",&score);

        sum += score;
    }

    double average = sum / num;
    if (average == 60.00){
        printf("Good!\n");
    }
    else if (average > 60.00){
        printf("Excellent!\n");
    }
    else{
        printf("Bad!\n");}

    printf("Average score is %.2f.\n", average);

    return 0;
}
