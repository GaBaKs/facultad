numero equ 0
izq equ 4
der equ 8
null equ -1

push < -> -> root abb>      bp+12
push < -> root arbol no ordenado>   bp+8
call merge_tree
add sp,8


push < -> -> root abb>  bp+12
push < -> nodo >        bp+8
call agrega_abb
add sp,8


merge_tree:
            push bp
            mov bp,sp
            push eax
            push ecx
            mov eax,[bp+8]; -> nodo actual
            mov ecx,[bp+12]; -> -> root abb
            cmp [eax],null
            jz fin
            
            ;llamo por izq
            push ecx
            push [eax+izq]
            call merge_tree
            add sp,8

            ;llamo por der
            cmp [eax+der],null
            jz comparo
            push ecx
            push [eax+der]
            call merge_tree
            add sp,8

            ;meto el nodo al abb
            push ebx
            mov ebx,[ecx]
            push ebx
            push eax
            call agrega_abb
            add sp,8
            pop ebx

    fin:   
            pop eax
            mov sp,bp
            pop bp
            ret

agrega_abb:
            push bp
            mov bp,sp
            push eax
            push ebx
            push ecx
            mov eax,[bp+8]; -> a nodo
            mov ecx,[bp+12]; -> -> a abb
            mov ebx,[ecx]; -> a abb
            
            cmp eax,null
            jz fin
            cmp ebx,null
            jz agregaraiz
            cmp [ebx+numero],[eax+numero]
            JN recorreder
            ;avanza a la izquierda
            cmp [ebx+izq],null
            jz agregaizq
            push [ebx+izq]
            push eax
            call agrega_abb
            add sp,8
            JMP fin

recorreder: cmp [ebx+der],null
            jz agregader
            push [ebx+der]
            push eax
            call agrega_abb
            add sp,8
            JMP fin

agregaraiz:
            mov [ecx],eax
            mov [eax+izq],null
            mov [eax+der],null
            jmp fin

agregaizq:  mov [ebx+izq],eax
            mov [eax+izq],null
            mov [eax+der],null
            jmp fin

agregader:  mov [ebx+der],eax
            mov [eax+izq],null
            mov [eax+der],null

fin:        pop ebx
            pop eax
            mov sp,bp
            pop bp
            ret
            
