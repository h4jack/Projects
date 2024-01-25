#include <stdio.h>
#include "string.h"

int main(){
    string *name = inputs();
    string_show(name);
    printf("\n");
    string *name2 = substr(name,4,11);
    string_show(name2);
    string_show(name);
    return 0;
}