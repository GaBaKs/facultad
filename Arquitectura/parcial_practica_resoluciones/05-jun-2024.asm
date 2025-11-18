
inicial equ 0
nombre equ 1
next equ 5
null equ -1
nodo equ 9
SIZE_ES equ <tamaño ES>


push <nombre>
call nnom_create
add sp,4
;devuelve en eax el nodo creado

push <bytes>
call alloc
add sp,4


alloc:  push bp
        mov bp,sp
        push ebx

        mov ebx,[ES]
        add ebx,[bp+8]
        mov eax,null
        cmp ebx,SIZE_ES
        JNP fin
        mov eax,[ES]
        add [ES],[bp+8]

fin:    pop ebx
        mov sp,bp
        pop bp
        ret
        


nnmom_create:
            push bp
            mov bp,sp
            push ebx
            push nodo
            call alloc
            add sp,4
            cmp eax,null
            jz fin
            mov [Eax+nombre],[bp+8]
            mov ebx,[eax+nombre]
            mov b[eax+incial],b[ebx]
           
            mov [eax+next],null

        fin:pop ebx
            mov sp,bp
            pop bp
            ret

id equ 0
dni equ 2
nombre equ 12
nacimiento equ 33
next2 equ 4
persona equ 0
año equ 0
mes equ 2
dia equ 3
edad equ 18

push < -> listapersonas> ;BP+12
push <fecha>        ;BP+8
call GET_MAYORES
add sp,8
;devuelve en efx

GET_MAYORES: push bp
             mov bp,sp
             sub sp,4
             mov efx,bp
             mov [efx],null
             push eax
             push eex
             push ebx
             push ecx
             push edx
             
             
             mov eex,[bp+8]; fecha ingresada
             mov ebx,[bp+12]; nodo actual
    while:   cmp ebx,null
             jz fin
             mov ecx,[ebx+fecha]; guardo en ecx -> a fecha
             mov dx,w[ecx+año]
             sub dx,ah; año lista - año parametro
             cmp dx,edad;
             JP agrega
             JN nextnodo
             ;comparo el mes xq tiene 18
             cmp b[eex+mes],b[ecx+mes]; mes ingresado > mes nacimiento
             JP agrega
             JN nextnodo
             cmp b[eex+dia],b[ecx+dia]; dia ingresado > dia nacimiento
             JNN agrega
    nextnodo:
             mov ebx,[ebx+next2]
             jmp while

    agrega: 
            push [ebx+nombre]
            call nnom_create
            add sp,4
            push efx
            push eax
            call nnom_add
            add sp,8
            jmp nextnodo
    
    fin:    pop edx
            pop ecx
            pop ebx
            pop eex
            pop eax
            mov sp,bp
            pop bp
            ret

            



             
