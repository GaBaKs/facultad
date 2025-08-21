program ejer3;
var
 x,sb,sn : real ;
begin
  Repeat
  Writeln('ingrese cantidad de horas trabajadas');
  Readln(x);
  until x>0;
  sb:=x*200;
  sn:=x*200*0.84;
  Writeln('el sueldo bruto es de',sb:8:2,' y el sueldo neto es de ',sn:8:2);
  Readln;
end.

