program ejer2;
 function factorial(n:word):word;
 var
   i:byte;
   acum:word;
 begin
  acum:=1;
  for i:=1 to n do
   acum:=acum*i;
  factorial:=acum;
 end;
 var
   n:word;
begin
  Writeln('ingrese un n');
  Readln(n);
  Writeln('el factorial del numero ingresado es ',factorial(n));
  Readln();
end.

