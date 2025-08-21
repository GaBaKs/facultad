program ejer16;
  function Esletra(Car:Char): boolean;
  begin
   car:=Upcase(car);
   Esletra:= car>='A'
  end;

  var
    car: char;
begin
  Writeln('escriba un caracter');
  Readln(Car);
  If Esletra(car) then
  Writeln('es una letra')
  else Writeln('es un caracter');
  Readln();
end.

