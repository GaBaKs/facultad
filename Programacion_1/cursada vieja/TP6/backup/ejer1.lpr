program ejer1;
 type
   Tipomatriz=array[1..10,1..10] of integer;
   Vec=array[1..10] of integer;
   procedure lectura(var matriz:Tipomatriz;var N:integer;var M:integer);
    var
     arch: text;
    i,j:integer;
    aux:integer;
    begin
     Assign(arch,'ejer1.TXT');
     Reset(arch);
     Read(arch,N);
     Readln(arch,M);
     for i:=1 to N do
      begin
       for j:=1 to M do
        begin
         Read(arch,aux);
         matriz[i,j]:=aux;
         end;
      Readln(arch);
      end;
    end;

  procedure maxfila(matriz:tipomatriz;N:integer;M:integer);
   var
    i,j,max,actual:integer;
    vector: vec;
   begin
    max:=-99999;
    for i:=1 to N do
     begin
      for j:=1 to M do
       begin
        actual:=matriz[i,j];
        if actual>max then
         max:=actual;
        end;
       vector[i]:=max;
       end;
    Writeln('cada maximo de las filas es');
    for j:=1 to M do
     Write(' ',vector[j]);
    Writeln();
    end;

  function promedio(matriz:tipomatriz; N:integer; X:integer):real;
   var
    i:byte;
    acum:integer;
   begin
    acum:=0;
      for i:=1 to N do
        acum:=acum+matriz[i,X];
    promedio:=acum/N;
   end;

  var
   matriz:tipomatriz;
   N,M,X:integer;
begin
  lectura(matriz,N,M);
  maxfila(matriz,N,M);
  Writeln('ingrese una columna para calcular el promedio:');
  Readln(X);
  Writeln('el promedio es: ',promedio(matriz,N,X));

end.

