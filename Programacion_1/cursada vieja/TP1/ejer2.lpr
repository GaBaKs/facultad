program ejer2;
var K, Kes : real;
begin
  repeat
  Writeln('ingrese un valor de K');
  Readln(K);
  until K>0 ;
  Kes:=1+3*(K-1);
  Writeln('el K-esimo termino es', Kes: 8:3);
  Readln;
end.

