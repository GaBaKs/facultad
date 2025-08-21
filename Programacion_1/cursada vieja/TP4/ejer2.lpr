program ejer2;
 function factorial(n:integer): integer;
 var fact: integer;
  i: integer;
 begin
  fact:=1;
  for i:=1 to n do
   fact:=fact*i;
  factorial:=fact;
  end;
var
   n:integer;
begin
  repeat
  Writeln('ingrese un numero');
  Readln(n);
  until n>0;
  Writeln('el factorial es ',factorial(n));
  Readln();
end.

