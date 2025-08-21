program ejer6b;
var
  N: integer;
begin
  repeat
    Writeln('escribir el valor de N');
    Readln(N);
    until N>=1000;
    Writeln('la cifra en la posicion de las centenas es',N - ((N DIV 1000)*1000 DIV 100));
    Readln;
end.

