program Project1;
  function natural(N:word):word;
   var
     i:byte;
     acum:word;
   begin
    acum:=0;
    for i:=1 to N do
     acum:=acum+i
   end;
var
  N:word;
begin
 Writeln('ingrese un numero');
 Readln(N);
 Writeln('la suma de los primeros N naturales es de ',natural(N));
 Readln();
end.

