program final;
const
  max=50;
 type
   st6=string[6];
   st30=string[30];
   TR=record
     id:st6;
     genero:char;
     nombretema:st30;
     disp:char;
     cantmg:integer;
   end;
  FTR=file of TR;
  TR2=record
    id:st6;
    nombre:st30;
    cat:char;
Tvec=array[1..max] of st6;
 FTR2=file of TR2;

 procedure listado(var arch:FTR;var arch2:FTR2;vec:Tvec;N:byte;X,Y:char);
  var
   i:byte;
   aux:TR;
   aux2:TR2;
   flag,flag2:boolean;
   promMG:real;
   cont,contsc,erroneo:byte;
   acum:integer;

  begin
       Reset(arch);
       Reset(arch2);
       contsc:=0;
       erroneo:=0;
       Writeln('LISTADO CATEGORIA ',X);
       read(arch,aux);
       read(arch2,aux2)
       While (not eof(arch)) and (not eof(arch2)) do
        begin
           if aux2.cat<>X then
             While (aux2.cat<>X) do
              read(arch2,aux2);
           else
            begin
             flag:=false;
             flag2:=false;
             cont:=0;
             acum:=0;
             Writeln('nombre interprete: ',aux2.nombre);
             if aux.id=aux2.id then
              begin
                    if aux.disp='S' then
                      begin
                       if not flag2 then
                        Writeln('      nombre de los temas del genero ',Y);
                           flag2:=true;
                           Writeln('         ',aux.nombretema);
                           flag:=true;
                           cont:=cont+1;
                           acum:=acum+aux.cantmg;
                      end;
                    Read(arch,aux);
              end;
            else
             if not flag then
              begin
               Writeln('         no tiene contrato');
               contsc:=contsc+1;
              end
             else begin
                       promMG:=acum/cont;
                       Writeln('Cantidad promedio de MG: ',promMG:8:2);
                  end;
            end;
        end;




begin
end.

