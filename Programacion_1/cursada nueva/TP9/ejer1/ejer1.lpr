program ejer1;
 type
   ST5 = string[5];
    TR = record
      codP: ST5;
      peso, monto: real;
      codD: byte;
    end;
    TArch = file of TR;
 function pesopromedio(var arch:TArch):real;
  var
    acum: real;
    cont:byte;
    aux: TR;
 begin
   acum:=0;

   cont:=filesize(arch);
   seek(arch,0);
   While not eof(arch) do
     begin
      read(arch,aux);
      acum:=acum+aux.peso;
     end;
   pesopromedio:=acum/cont;
 end;
var
 nice:byte;
 arch: TArch;
begin
  Assign(arch,'PAQUETES.DAT');
  Reset(arch);
  Writeln('el peso promedio es ',pesopromedio(arch):4:2);
  Readln();
end.

