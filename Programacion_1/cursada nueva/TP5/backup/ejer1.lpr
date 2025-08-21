program ejer1;
 type
   sv=array[1..100] of real;
   procedure lectura(var N:byte;var vec:sv);
    var
      i:byte;
     begin
       Writeln('ingrese N');
       Readln(N);
       for i:=1 to N do
        begin
         Writeln('ingrese el numero en el espacio ',i);
         Readln(vec[i]);
        end;
   end;
Function suma(vec:sv;N:byte):real;
  var
    i:byte;
    Sum:real;
 begin
 Sum:=0;
  for i:=1 to N do
   begin
   sum:=sum+vec[i];
   end;
  Suma:=Sum;
  end;

  procedure pares(vec:sv;N:byte);
   var
     i:byte;
   begin
     i:=2;
     Write('los numeros en posiciones pares son:');
     While i<N do
      begin
       Writeln(' ',vec[i]);
       i:=i+2;
      end;
    end;

  function max(vec:sv;N:byte):real;
   var
     i:byte;
   begin
     for i:=1 to N do
       if max<vec[i] then
        max:=vec[i];
   end;
   function min(vec:sv;N:byte):real;
   var
     i:byte;
   begin
     for i:=1 to N do
       if min>vec[i] then
        min:=vec[i];
   end;

 procedure invertir(vec:sv;N:byte;var vecB:sv);
  var
    i:byte;
    M:byte;
  begin
    M:=N;
   for i:=1 to N do
    begin
     vecB[i]:=vec[M];
     M:=M-1;
     Write(' ',vecB[i]);
    end;
  end;

var
  N:byte;
  vec,vecB:sv;
begin

  lectura(N,vec);
  Writeln('la suma es ',suma(vec,N):2:2);
  pares(vec,N);
  Writeln('el maximo elemento es ',max(vec,N):2:2,' y el minimo elemento es ',min(vec,N):2:2);
  invertir(vec,N,vecB);
  Readln();
end.

