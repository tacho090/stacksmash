.global _start
.intel_syntax noprefix

_start:
    mov ebx, 1337
    push ebx
    pop eax
    mov edx, ebx

_exit:
    mov eax, 1
    mov ebx, 0
    int 0x80
