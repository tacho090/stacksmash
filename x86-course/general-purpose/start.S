.global _start
.intel_syntax noprefix

_start:
    mov edx, 0x456

_exit:
    mov eax, 1
    mov ebx, 0
    int 0x80
