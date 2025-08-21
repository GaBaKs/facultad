program final2dotry;
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
    end;
 FTR2=file of TR2;

 procedure listado(var arch:FTR;var arch2:FTR2;X,Y:char);
  var
   erroneo,flag:boolean;
   idaux:st6;
   aux:TR;
   aux2:TR2;
   cont,contnoc:byte;
   cantmeg:integer;
  begin
     Reset(arch);
     Reset(arch2);
     erroneo:=false;
     flag:=false;
     cont:=0;
     cantmeg:=0;
     contnoc:=0;
     Writeln('LISTADO CATEGORIA ',X);
     read(arch,aux);
     read(arch2,aux2);
     While (not eof(arch)) and (not eof(arch2)) do
     begin
     if aux2.cat=x then
      begin
      if aux.id=aux2.id then
       begin
         Writeln('Nombre interprete: ',aux2.nombre);
         While aux.id=aux2.id do
          begin
           if aux.genero=Y then
             begin
             if aux.disp='S' then
              begin
               if not flag then
                 begin
                  Writeln('Nombre de los temas del genero ',Y);
                  flag:=true;
                 end;
               Writeln('   ',aux.nombretema);
               cont:=cont+1;
               cantmeg:=cantmeg+aux.cantmg;
              end;
             end;
           read(arch,aux);
          end;
         if not flag then
            begin
            Writeln('NO TIENE CONTRATO');
            contnoc:=contnoc+1;
            end
         else
          Writeln('Promedio de me gusta: ',(cantmeg/cont):6:2);
       end;
    end
     else

     While aux.id=aux2.id do
       read(arch,aux);

       read(arch2,aux2);
      if aux2.id>aux.id then
          erroneo:=true;
       flag:=false;
       cont:=0;
       cantmeg:=0;

     end;
   Writeln('interpretes sin contrato: ',contnoc);
   if erroneo then
      Writeln('se detectaron interpretes con contrato erroneo')
      else Writeln('no se detectaron interpretes con contrato erroneo');

  end;

  var
   arch:FTR;
   arch2:FTR2;
   X,Y:char;


begin
   Assign(arch,'ARCHIVOTEMAS.DAT');
   Assign(arch2,'INTERPRETES.DAT');
   Writeln('ingrese un X');
   readln(X);
   Writeln('Ingrese un Y');
   Readln(y);
   listado(arch,arch2,X,Y);
   readln();
end.

