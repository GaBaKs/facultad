program ejer5;
  type
   st4=string[4];
   TR=record
     mat:st4;
     Nmat:byte;
     Nfis:byte;
     Nquim:byte;
   end;
 FTR=file of TR;
   TR2=record
     mat:st4;
     quimins:char;
     fisins:char;
   end;
 FTR2=file of TR2;

 procedure lista(var arch:FTR;var arch2:FTR2);

   var
     aux:TR;
     aux2:TR2;
 begin
   Reset(arch);
   Reset(arch2);
  Writeln('ALUMNOS QUE NO CUMPLEN REQUISITOS');
   While (not eof(arch)) and (not eof(arch2)) do
    begin
     Read(arch,aux);
     Read(arch2,aux2);
       if (aux.Nmat<4) or (aux.Nfis<4) then
         if aux2.fisins='1' then
         Writeln(aux.mat);
      if (aux.Nquim<4) and (aux2.quimins='1') then
        Writeln(aux.mat);
    end;
 end;

var
 arch:FTR;
 arch2:FTR2;

begin
  Assign(arch,'ALUMNOS.DAT');
  Assign(arch2,'INSCRIPTOS.DAT');
  lista(arch,arch2);
  Close(arch);
  Close(arch2);
  Readln();
end.

