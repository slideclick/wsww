// intAscii.cpp : Defines the entry point for the console application.
//

#include <stdio.h>



int main(int argc, char* argv[])
{
	char over = 128;
    int i = over;
    printf("%d %x %b\n",i,i,i);

    int over32 = 0x80000000;

    printf("%d %x %b\n",over32,over32,over32);
    over32++;
    printf("%d %x %b\n",over32,over32,over32);

    char cArray []={0x41,0x42,0x00};
    printf("%s\n",cArray);

    char sArray []="\x61\x62\x00";
    printf("%s\n",sArray);


    for (int j = 2147483646; j != -2147483645;j ++ ){
    
        printf("%d\n",j);
    }
    char chinese936[] = "\xca\xd4";//��
    char chinese65001[] = "\xe8\xaf\x95";//�� utf-8

    for (int a = 0; a<256; a++){
    
        printf("%c  %d %x %c\n",a,a,a,a);// chcp 1252���Դ�ӡ����0x81�Ժ�ģ�����0xA0�Ժ�Ĳ���latin-1��(iso8859-1)
      
    }

    return 0;
}

