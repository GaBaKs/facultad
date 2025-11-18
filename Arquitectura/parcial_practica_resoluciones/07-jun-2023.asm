nombre equ 0
next equ 4
null equ -1
nodo equ 8

push < -> nombre>
call crear_nodo
add sp,4
;devuelve en eax -> al nodo
push <cant bytes>
call alloc
add sp,4
;devuelve en eax -> a memoria

crear_nodo:     push bp
                mov bp,sp

                push nodo
                call alloc
                add sp,4
                mov [eax+nombre],[bp+8]
                
                mov sp,bp
                pop bp
                ret

push < -> nodo>
push < -> -> head>
call insert_nodo
add sp,8

nom equ "pedro"

insert_nodo:    push bp
                mov bp,sp
                push ebx
                push edx

                mov ebx,[bp+8]; -> -> head
                mov edx,[bp+12]; -> nodo
                mov [edx+next],[ebx]
                mov [ebx],edx

                pop edx
                pop ebx
                mov sp,bp
                pop bp
                ret

main:           push bp
                mov bp,sp
                push eax
                mov eex,31

        while:  cmp eex,0
                jz finwhile
                mov ebx,sp
                sub sp,4
                mov [ebx],null
                
