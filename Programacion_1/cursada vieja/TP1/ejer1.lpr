program ejer1;
var
  M,pb : real;
begin
  repeat
  Writeln('¿cuanta pintura negra tiene?');
 Readln(M);
 until M>0;
  pb:=M*0.47368   ;
  Writeln('la cantidad de pintura blanca a comprar es ',pb:8:3) ;
  Writeln('hola');
end.

