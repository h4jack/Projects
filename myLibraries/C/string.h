#include <stdio.h>
#include <stdlib.h>
#define inputs() input("")
//a dynamic string using linked list.
typedef struct ListString{
    char data;
    struct ListString *next;
}string;

int isEmpty(string *head){
    if(!head){
        return 1;
    }
    return 0;
}

int len(string *head){
    int count = 0;
    while(head){
        head = head->next;
        count++;
    }
    return count;
}

int count(string *head, char key){
    int count = 0;
    while(head){
        if(head->data == key){
            count++;
        }
        head = head->next;
    }
    return count;
}

int item_at(string *head,int index){
    int l = len(head);
    if(index >= l){
        printf("index out of range.\n");
        return -1;
    }
    if(index == -1) index = l-1;
    int count = 1;
    while(count <= index){
        head = head->next;
        count++;
    }
    return head->data;
}

int top(string *head){
    item_at(head,0);
}

int bottom(string *head){
    item_at(head,-1);
}

void insert_back(string **st, char data){
    string *new_node = malloc(sizeof(string));
    new_node->data = data;
    if(!*st){
        new_node->next = *st;
        *st = new_node;
        return;
    }
    new_node->next = NULL;
    string *temp = *st;
    while(temp->next){
        temp = temp->next;
    }
    temp->next = new_node;
}

string *input(char str[]){
    printf("%s",str);
    string *head = NULL;
    char c;
    while(1){
        scanf("%c",&c);
        if(c == 10)break;
        insert_back(&head,c);
    }
    return head;
}

string *to_string(char arr[]){
    string *newStr = NULL;
    int i = 0;
    while(arr[i] != '\0'){
        insert_back(&newStr, arr[i]);
        i++;
    }
    return newStr;
}

void string_show(string *head) {
    while (head != NULL) {
        printf("%c", head->data);
        head = head->next;
    }
}

string *substr(string *head,int from, int to){
    int l = len(head);
    if(from > to || from < 0 || to > l-1){
        printf("index out of range.\n");
        return NULL;
    }
    int i = 0;
    while(i < from){
        head = head->next;
        i++;
    }
    string *temp = NULL;
    while(i <= to){
        insert_back(&temp,head->data);
        head = head->next;
        i++;
    }
    return temp;
}