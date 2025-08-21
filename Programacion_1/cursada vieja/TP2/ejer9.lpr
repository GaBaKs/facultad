program ejer9;
 var
  vensup,ventas,falt,valven : integer ;
    sueldo : real ;
begin
  Writeln('cant de ventas a superar');
  Readln(vensup);
  Writeln('cantidad de ventas totales');
  Readln(ventas);
  Writeln('valor de las ventas');
  Readln(valven);
  Writeln('dias faltados al trabajo');
  Readln(falt);
  sueldo:=(8000+valven*ventas)*1.05;
   if ventas>vensup then
    sueldo:=sueldo*1.03;
   if falt<=2 then
     begin
    if ventas*1.02>1000 then
    sueldo:=sueldo*1.02
    else sueldo:=sueldo+1000;
     end
   else sueldo:=sueldo*0.93;
  Writeln('el vendedor debe de cobrar ',sueldo:6:2, 'pesos');
  Readln();
end.

