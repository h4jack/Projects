#include <stdlib.h>
#include <math.h>
int isNumber(char c){
    return (c >= 48 && c <= 57) || c == 46;
}

int isOperator(char c){
    return (c == 45 || c == 43 || c == 42 || c == 47 || c == 37 || c == 94);
}

int isBrace(char c){
    return (c == 40 || c == 41);
}

int opPref(char c){
    switch(c){
        case 94:
            return 6;
        case 47:
            return 4;
        case 37:
        case 42:
            return 3;
        case 43:
        case 45:
            return 1;
        case 40:
        case 41:
            return 0;
        default:
            exit(0);
    }
}

double calculate(double num1, char op, double num2){
    switch(op){
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            if(num2 == 0){
                printf("Division is not Possible with 0.");
                exit(0);
            }
            return num1 / num2;
        case '%':
            printf("modulo(%%) function is not available.\n");
            exit(0);
            // while(num1 >= num2){
            //     num1 -= num2;
            // }
            // return num1;
        case '^':
            return pow(num1,num2);
        default:
            printf("Invalid Operator.\n");
            return 0;
    }
    return 0;
}