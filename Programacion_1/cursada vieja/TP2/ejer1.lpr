program ejer1;
    var
      x: char;
begin
  Writeln('ingrese un caracter');
  Readln(x);
  if x=Upcase(x) then
  Writeln('el caracter ingresado es una Mayuscula')
  else
  Writeln('el caracter ingresado es una minuscula');
  Readln();
end.

