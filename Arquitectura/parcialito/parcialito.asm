clave equ 0
izq equ 2
der equ 6
nivel equ 0
parbol equ 2
next equ 6
null equ -1

push < -> root> ;bp+8
call get_leafs
add sp,4
; devuelve en eax -> a lista

push <nivel>; BP+16
push <ptr ptr header lista> ;BP+12
push < ptr root>    ;BP+8
call _get_leafs
add sp,12



get_leafs: push bp
           mov bp,sp
           sub sp,4
           mov eax,bp
           sub eax,4
           mov [eax],null
           
           cmp [bp+8],null
           jz end
        
            push 0
            push eax
            push [bp+8]
            call _get_leafs
            add sp,12

            mov eax,[eax]; transformo a puntero simple

       end: mov sp,bp
            pop bp
            ret

_get_leafs: push bp
            mov bp,sp
            push eax
            push ebx
            push ecx
            push edx
            mov ebx,[bp+8]; * a root
            mov edx,[bp+12]; ** a lista
            mov cx, w[bp+18]; nivel
            add cx,1

            cmp ebx,null
            jz end
            cmp [ebx+izq],null
            jz test_der

            ;llamo por izq
            push cx
            push edx
            push [ebx+izq]
            call _get_leafs
            add sp,12
            jmp llamader


test_der:   cmp [ebx+der],null
            jz agrega

llamader:   push cx
            push edx
            push [ebx+der]
            call _get_leafs
            add sp,12
            jmp end

agrega:     push ebx
            push w[bp+18]; nivel
            call node_new
            add sp,8
            push eax
            push edx
            call add_sort
            add sp,8

end:        pop edx
            pop ecx
            pop ebx
            pop eax
            mov sp,bp
            pop bp
            ret

            
