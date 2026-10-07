#include <stdio.h>

int main(void)
{
    int x , y;
    char op;
    scanf("%d %c %d",&x,&op,&y);     //这里 %c 前面的空格表示：跳过零个或多个空白字符，然后再读取一个字符。

    if(op == '+'){
        printf("%d\n",x + y);
    }
    else if(op == '-'){
        printf("%d\n",x - y);
    }
    else if(op == '*'){
        printf("%d\n",x * y);
    }
    else if(op == '/'){
        printf("%d\n",x / y);
        return 0;
    }
}