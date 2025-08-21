program ejer6a;
   var
     n,divi: integer ;
begin
  repeat
   Writeln('escribe el valor de n');
   Readln(n);
    until n>=1000  ;
    Writeln('el valor de n sin las 3 ultimas cifras es ',n div 1000);
    Readln;
end.

