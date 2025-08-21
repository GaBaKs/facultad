program ejer4;
 type
   mat= array [1..30,1..30] of byte;
 procedure nym (var arch:text;var N:byte;var M:byte);
    var
   aux:byte;
  begin
    N:=0;
    M:=0;
    assign(arch,'ejer4.TXT');
    reset(arch);
    while not eof(arch) do
     begin
      read(arch,aux);
      if aux>N then
       N:=aux;
      read(arch,aux);
      if aux>M then
       M:=aux;
      readln(arch,aux);
     end;
  end;
 procedure leerarch(var arch:text;N:byte;M:byte;var matriz:mat);
  var
   i,j,val:byte;
  begin
   for i:=1 to N do
    for j:=1 to M do
     matriz[i,j]:=0;
  reset(arch);
  while not eof(arch) do
   begin
      read(arch,i);
      read(arch,j);
      readln(arch,val);
      matriz[i,j]:=val;
   end;
   close(arch);
  end;
 procedure mostrarmatriz(matriz:mat;N:byte;M:byte);
  var
   i,j:byte;
  begin
   for i:=1 to N do
    begin
     for j:=1 to M do
      Write(matriz[i,j],' ');
     Writeln('');
    end;
   end;
procedure trinf(matriz:mat;N:byte;M:byte);
 var
  i,j:byte;
  bol:boolean;
 begin
 if N=M then
  begin
  for i:=1 to N do
   begin
   for j:=1 to M do
    begin
     if i<j then
      if matriz[i,j]<>0 then
       bol:=true;
    end;
   end;
  if bol then
   Writeln('la matriz no es triangular inferior')
   else Writeln('la matriz es triangular inferior');
 end
 else Writeln('la matriz no es cuadrada por lo tanto no se puede analizar si es triangular inferior');
 end;

var
 matriz:mat;
 N,M:byte;
 arch:text;
begin
 nym(arch,N,M);
 leerarch(arch,N,M,matriz);
 mostrarmatriz(matriz,N,M);
 trinf(matriz,N,M);
 Readln();
end.

