\\stack 1024
\\extra 1024



;recursivo:
;    push <base>
;    push <exponente>
;    mov eax,1
;    call potencia
;    add sp,8

potencia: push bp
          mov bp,sp
          push eex
          push ebx

          mov eex,[bp+12];exponente
          mov ebx,[bp+8];base
          cmp eex,0
          JZ fin
          JN pot_neg
    rec:  sub eex,1
          push eex
          push ebx
          call potencia
          add sp,8
          mul eax,ebx; acum*base

    fin:  pop ebx
          pop eex
          pop bp
          ret

pot_neg:  push edx
          mov edx,1
          div edx,ebx
          mov ebx,edx
          pop edx
          mul eex,-1
          jmp rec


main:      SYS 0xF
           push bp
          mov bp,sp 
          mov ebx,3;base
          mov eex,4;exp
          push eex
          push ebx
          mov eax,1
          call potencia
          add sp,8
          mov edx,DS
          mov [edx],eax
          mov eax,0x1
          LDH ecx,0x04
          LDL ecx,0x01
          SYS 2
          pop bp
          ret