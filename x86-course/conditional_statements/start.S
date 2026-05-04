.global _start
.intel_syntax noprefix

.section .data
a: .long 10
b: .long 20
msg_gt: .asciz "a > b\n"
msg_lt: .asciz "a < b\n"
msg_eq: .asciz "a == b\n"

.section .text
_start:
  mov eax, [a]
  mov ebx, [b]
  cmp eax, ebx
  jg greater
  jl less
  je equal

greater:
  mov eax, 4
  mov ebx, 1
  lea ecx, [msg_gt]
  mov edx, 6
  int 0x80
  jmp done

less: 
  mov eax, 4
  mov ebx, 1
  lea ecx, [msg_lt]
  mov edx, 6
  int 0x80
  jmp done

equal:
  mov eax, 4
  mov ebx, 1
  lea ecx, [msg_eq]
  mov edx, 8
  int 0x80
  jmp done

done:
    mov eax, 1
    mov ebx, 0
    int 0x80
