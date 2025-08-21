program ejer8;
// Un club cobra a sus socios una cuota básica por mes que incluye dos deportes, su costo depende de la edad del socio:
//Si es mayor de 18: $1800 Si está entre 13 y 18: $1200 Si tiene entre 5 y 12 años: $750 En otro caso no paga
//Además, se cobra $250 por cada deporte adicional que realiza, excepto pileta escuela que cuesta $800. Si la cuota se abona después del día 15 tiene
//un recargo del 5%. Determinar los datos a ingresar, para calcular e informar cuánto paga un socio.
var
 pago:real;
 costobase:word;
 edad,depext,diapago:byte;
 sn:char;

begin
 repeat
  Writeln('ingrese edad del socio');
  Readln(edad);
 until edad>0;
 repeat
  Writeln('va a realizar pileta escuela?(s para si n para no)');
  Readln(sn);
 until (sn='s') or (sn='n');
 repeat
 Writeln('cuantos deportes extra(sin pileta escuela)va a realizar(0 si no se realiza deporte extra)');
 Readln(depext);
 until depext>=0;
 Writeln('que dia va a abonar la cuota cada mes(despues del dia 15 tiene 5% de recargo)');
 Readln(diapago);

 case edad of
  1..4:costobase:=0;
  5..12 : costobase:=750;
  13..18: costobase:=1200;
  19..255:costobase:=1800;
 end;

 if sn='s' then
  pago:=costobase+depext*250+800
  else pago:=costobase+depext*250;
 if diapago>=15 then
  pago:=pago*1.05;
 Writeln('el socio debe pagar ',pago:2:0,' pesos mensualmente');
 Readln();
end.

