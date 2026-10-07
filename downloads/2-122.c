/* CS100 Fall 2026 - HW1 Problem 4: Second maximum and second minimum
 *
 * No arrays or dynamic memory allocation (the last 5 test cases require
 * O(1) extra space). Do not rename this file.
 */
#include <stdio.h>

int main(void)
{
    /* TODO: your code here */
    int total_num ;
    scanf("%d",&total_num);

    
        int maximum = -101;
        int second_maximum = -102;
        int minimum = 102;
        int second_minimum = 101;
    for(int i = 0; i <= total_num - 1; i++){
        int num;
        if(scanf("%d",&num) != 1){
            return 1;
        }
        if(num > maximum){
            second_maximum = maximum;
            maximum = num;
        }
        else if(num > second_maximum && num < maximum ){
            second_maximum = num;
        }
        if(num < minimum){
            second_minimum = minimum;
            minimum = num;
        }
        else if(num > minimum && num < second_minimum){
            second_minimum = num;
        }

    }
    printf("%d %d\n", second_maximum,second_minimum);
    

    
}
