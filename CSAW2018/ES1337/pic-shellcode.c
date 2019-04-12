//
// PIC Shellcode
//
// gcc -ggdb -m64 -O3 -fno-stack-protector -o pic-shellcode pic-shellcode.c
//

#include <stdio.h>
#include <unistd.h>


void main()
{
    char path[15] = { '/', 'u', 's', 'r', '/', 'b', 'i', 'n', '/', 'x', 'c', 'a', 'l', 'c', 0 };
    char env[13] = { 'D', 'I', 'S', 'P', 'L', 'A', 'Y', '=', ':', '0', '.', '0', 0 };
    
    char *envp[] = { env, NULL };
    char *argv[] = { path, NULL };

    if (fork() == 0)
    {
    	execve(path, argv, envp);
    }
    
    return;
}
