valor equ 0
next equ 4
null equ -1


push < valor>
call new_node
add sp,4
;retorna en eax -> a nodo nuevo


push < -> -> lista>
call clone
add sp,4
;retorna en eax -> cabeza de la lista nueva


clone:
        push bp
        mov bp,sp
        push ebx
        push ecx
        push edx

        mov eax,null

        mov ebx,[bp+8]; -> -> a nodo
        mov ecx,[ebx]; -> a nodo
        cmp ecx,null
        jz fin
        push [ecx+valor]
        call new_node
        add sp,4

        mov edx,eax
        add ecx,next
        push ecx
        call clone
        add sp,4
  
        mov [edx+next],eax
        mov eax,edx
fin:    pop edx
        pop ecx
        pop ebx
        mov sp,bp
        pop bp
        ret


clone:

        push bp
        mov bp,sp
        push ebx
        push ecx
        mov eax,null
        mov ebx,[bp+8]; -> -> nodo o anterior
        mov ecx,[ebx]; -> nodo actual

        cmp ecx,null
        jz fin

        push [ecx+valor]
        call new_node
        add sp,4
        ; en eax tengo cabeza de nueva lista
        
        mov ebx,eax
        add ecx,next
        push ecx
        call clone
        add sp,4

        ;enlazo lista
        mov [ebx+next],eax
        mov eax,ebx

fin:    pop ecx
        pop ebx
        mov sp,bp
        pop bp
        ret


exists: push bp
        mov bp,sp
        push ebx
        push ecx
        mov ebx,[bp+8]; -> header lista a
        mov ecx,[bp+12]; -> nodo buscado
        mov eax,0

        cmp ecx,null
        jz fin
while:  cmp ebx,null
        jz fin
        cmp ebx,ecx
        jz existe
        mov ebx,[ebx+next]
        jmp while

existe: mov eax,1

fin:    pop ecx
        pop ebx
        mov sp,bp
        pop bp
        ret


split:      push bp
            mov bp,sp
            push eax
            push ebx
            push ecx
            mov eax,0
            mov ebx,[bp+8]; -> -> a lista a
            mov ecx,[bp+12]; -> -> a lista b

while:      push [ecx]
            push [ebx]
            call exists
            add sp,8
            cmp eax,1
            jz encontro
            mov ecx,[ecx]
            add ecx,next
            jmp while

encontro:   push ebx
            call clone
            add sp,4
            mov [ecx],eax

fin:       
            pop ecx
            pop ebx
            pop eax
            mov sp,bp
            pop bp
            ret