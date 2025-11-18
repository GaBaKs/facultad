key equ 0
texto equ 4
left equ 8
right equ 12
data equ 4
push < -> -> raiz>
push < -> nodo>
call btn_add
add sp,8
;devuelve en eax si se pudo meter el nodo

btn_add:    push bp
            mov bp,sp
            push ebx
            push ecx
            push edx
            push eex
            push efx
            mov eax,0
            mov ebx,[bp+8]; -> nodo a agregar
            mov efx,[ebx+data]
            mov ecx,[bp+12]; -> -> a la raiz
            mov edx,[ecx]; -> a raiz
            
 while:      cmp edx,null
            jz if

            mov eex,[edx+data]
            cmp [eex+key],[efx+key]
            jz if
            JN recorroder
            ;recorro por izq
            mov ecx,edx
            add ecx,izq
            mov edx,[edx+izq]
            JMP while

 recorroder: mov ecx,edx
            add ecx,der
            mov edx,[edx+der]            
            jmp while

 if:         cmp edx,null
            jnz fin
            mov [ecx],edx
            mov eax,1

 fin:        pop efx
            pop eex
            pop edx
            pop ecx
            pop ebx
            mov sp,bp
            pop bp
            ret

push < -> -> arbol a>
push < -> -> arbol b>
call merge_tree
add sp,8
;mete arbol b en a

merge_tree:
            push bp
            mov bp,sp
            push eax
            push ebx
            push ecx
            push edx
            mov ebx,[bp+12]; -> -> arbol a
            mov ecx,[bp+8]; -> -> arbol b

            cmp [ecx],null
            jz fin
            ;recorroizq
            mov edx,[ecx]
            add edx,izq
            push edx
            push ebx
            call merge_tree
            add sp,8
            
            ;recorroder
            mov edx,[ecx]
            add edx,der
            push edx
            push ebx
            call merge_tree
            add sp,8

            ;inserto nodo actual
            mov edx,[ecx]
            push ebx
            push edx
            call btn_add
            add sp,8
            
fin:        pop edx
            pop ecx
            pop ebx
            pop eax
            mov sp,bp
            pop bp
            ret
    
            
            