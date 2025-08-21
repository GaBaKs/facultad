program ejer13;
const
  dolar=120.8;
  euro=150.10;
  realbr=26.50;
var
  pesos,valf : Real;
  Moneda: Char;
begin
  repeat
   Writeln('ingrese cantidad de pesos');
   Readln(pesos);
  until pesos>0;
  Writeln('A que moneda desea cambiar?(D,E o R)');
  Readln(Moneda);
  Case Moneda of
   'D' : valf:=pesos/dolar;
   'E' : valf:=pesos/euro;
   'R' : valf:=pesos/realbr;
  else Writeln('no se ingreso una moneda valida');
  end;
  if valf>0 then
  Writeln('la cantidad de divisa ingresada es de ',valf:6:2);
  Readln();
end.

