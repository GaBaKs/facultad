program ejer4;

uses unit1;

 function potencia(X,N:word):word;
  var
    i:byte;
  begin
    potencia:=1;
    for i:=1 to N do
     potencia:=potencia*X;
  end;
var
  X,N:word;
begin
  Writeln('ingrese X');
  Readln(X);
  Writeln('ingrese N');
  Readln(N);
  Writeln('la potencia de ',x,' elevado a la ',N,' es de ',potencia(X,N));
  Readln();
end.

