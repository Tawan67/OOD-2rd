#include <stdio.h>

int plus(int,int);
int pow2(int base,int power){
    int result = 1;
    for(int i = 0;i<power;i++){
        result=result*base;
        printf("result = %d ,power = %d\n",result,i+1);
    }
    return result;
}
int sum(int* a,int len){
    int result = 0;
    for( int i = 0;i<len && *a != '\0';i++){
        result=result+*a;
        printf("element is %d\nsum result is %d\n",*a,result);
        a+=1;
    }
    return result;
}
int main(){
    int arr_2[20] ;
    int len2 =0;
    for(int i = 1;i<=10;i++){
        len2 ++;
        arr_2[i-1]=i;
    }
    int *point =  arr_2;
    int len = (sizeof(arr_2)/sizeof(arr_2[0]));
    
    printf("%d",len2);
    sum(point,len2);
    // int arr[10];
    // int c = 0;
    // c = plus(1,2);
    // printf("%d\n",c);
    // for(int i =0;i<10;i++){
    //     arr[i]=i;
    // }
    // for(int j = 9;j>=0;j--){
    //     printf("%d\n",arr[j]);
    // }
    int result  = 0;
    result = pow2(2,5);
    printf("%d \n",result);
    return 0;
}

int plus(int a,int b){
    return a+b;
}
