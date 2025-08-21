program ejer3;
 function suma(n:integer):integer;
 var i,resultado:integer;
 begin
  for i:=1 to n do
   begin
   resultado:=resultado+i;
   end;
  suma:=resultado;
  end;
   var
   n:integer;
begin
  Writeln('escriba por numero');
  Readln(n);
  Writeln('la suma de los ',n,' primeros numeros naturales es ',suma(n));
  Readln();
end.

