#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//NOTE APACHE IS NOT WORKING SO I CAN NOT TEST UNTIL BACK AT UNIVERSITY SERVERS

void decodeMsg(char *src, char *dest, int *i);

int main(int argb, char* args[]){
    //get msg size
    int size = atoi(getenv("CONTENT_LENGTH"));
    //blank string to hold input
    char* input = (char*)(malloc(size));
    //holding index
    int i = 0;
    //send data to input via STDIN
    scanf("%s",input);
    
    //decode and send to decodedData
    char* decodedData = (char*)(malloc(size));
    decodeMsg(input, decodedData, &i);
    
    //test for conditions
    if(!strcmp("download",input)){
        //to show all text
        printf("Content-Type:text/html\n\n");
        printf("<html>\n");
        scanf(
        printf("</html>\n");
    }
    else if(!strcmp("reset",input)){
        //delete text file
        remove("messageFile.txt");
    }
    else if(!strcmp("password",input)){
        //change password
        //NO TIME
    }
    
    return 0;
}

//Sample input need to decode:
//SendMessage=This+is+a+test&
void decodeMsg(char *src, char *dest, int *i){
    char c = ' ';
    //cut everything out until "="
    for(;c!='=';(*i)++)
    c = src[*i];
    c = src[*i];
    (*i)++;
    
    //give dest all info until "&"
    int j = *i;
    for(;c!='&'&&c!='\0';(*i)++){
        dest[*i-j] = c;
        c = src[*i];
    }
    dest[*i-j] = '\n\0';
}
