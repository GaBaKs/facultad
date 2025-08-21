program g9e1;

type
  ST5 = string[5];
  ST15 = string[15];
  TR1 = record
    codP: ST5;
    peso, monto: real;
    codD: byte;
  end;

  TR2 = record
    codD: byte;
    desc: ST15;
  end;

  Tarch1 = file of TR1;
  Tarch2 = file of TR2;


procedure promedio (var arch1:Tarch1);
var
  cont: byte;
  acum: real;
  aux: TR1;
begin
   cont:=0;
   acum:=0;
   reset(arch1);
   while not eof(arch1) do
     begin
       read(arch1, aux);
       cont:=cont+1;
       acum:=acum + aux.peso;
     end;
   close(arch1);
   if cont<>0 then
     writeln('El promedio de pesos es: ', acum/cont:4:2)
   else
     writeln('El promedio de pesos es: 0') ;
end;

procedure montoT (var arch1:Tarch1);
var
  acum: real;
  aux: TR1;
begin
   acum:=0;
   reset(arch1);
   while not eof(arch1) do
     begin
       read(arch1,aux);
       acum:=acum + aux.monto;
     end;
   writeln('Monto total: ', acum);
   close(arch1);
end;

var
  arch1: Tarch1;
  arch2: Tarch2;


begin
   assign(arch1, 'PAQUETES.DAT');
   assign(arch2, 'DESTINO.DAT');
   promedio(arch1);
   montoT(arch1);

   readln;
end.

