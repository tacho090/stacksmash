.global _start
.intel_syntax noprefix

_start:
    push 0x1
    push 0x2
    push 0x3

_exit:
    mov eax, 1
    mov ebx, 0
    int 0x80
