\\STACK 100


    slen: push bp
          mov bp,sp
          push edx
          mov edx,[BP+8];puntero a string
          cmp b[edx],0
          jz fin
          add edx,1
          push edx
          call slen
          add sp,4
    
    fin: add ecx,1
         pop edx
         pop bp
         ret
    
          










main:   mov edx,DS
        sys 0xF
        mov ecx,-1
        sys 3
        mov edx,DS
        mov ecx,-1
        push edx
        call slen; devuelve en ecx la cant de caracteres
        add sp,4
        mov [edx],ecx
        mov eax,0x1
        LDH ecx,0x04
        LDL ecx,0x01
        mov edx,DS
        SYS 2
        ret