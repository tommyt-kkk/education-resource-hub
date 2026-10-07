/* CS100 Fall 2026 - HW1 Problem 3: Sum and maximum
 *
 * Read integers until a 0; print the sum and the maximum.
 * No arrays or dynamic memory allocation. Do not rename this file.
 */
#include <stdio.h>

int main(void)
{
    /* TODO: your code here */
    int sum = 0;
    int num;
    int maximum = -101;
    int flag = 0;
    while(1){  

    scanf("%d",&num);

    flag += 1;
    if(flag == 1 && num == 0){
        maximum = num;
    }



    if(num == 0){
        break;
    }

    if(maximum - num < 0){
        maximum = num;
    }

    sum += num;
    }
    printf("sum: %d\n",sum);
    printf("maximum: %d\n",maximum);

    return 0;
}
