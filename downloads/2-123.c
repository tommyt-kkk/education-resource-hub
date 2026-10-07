/* CS100 Fall 2026 - HW1 Problem 5: Platinum Lion Dog's Bus Journey
 *
 * Input length is unknown: check the return value of scanf.
 * No arrays or dynamic memory allocation. Do not rename this file.
 */
#include <stdio.h>

int main(void)
{
    /* TODO: your code here */
    int original_num;
    scanf("%d",&original_num);
    int passenger_in,passenger_out;
    int station_counter = 0;
    while(scanf("%d%d",&passenger_out, &passenger_in) == 2){
        station_counter += 1;
    if(original_num < passenger_out){
        printf("Impossible.\n");
        return 0;       
    }
    original_num = original_num + passenger_in - passenger_out;
    }
    char command;
    if(scanf("%c",&command) == 1){
    if(command == 'p'){
        printf("%d\n",original_num);
    }
    else if(command == 's'){
        printf("%d\n",station_counter);
    }}
    return 0;
}
