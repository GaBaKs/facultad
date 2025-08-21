program ejer2;
const
  base=15000;
var
    anios,cont: integer ;
    nombre,nombremax: string ;
    promedio,sueldo,sueldomax,acumsuel: real;
begin
  sueldomax:=-1000;
  cont:=0;
  Writeln('nombre del empleado(escribir "finalizar" para terminar)');
  Readln(nombre);
  While nombre<>'finalizar' do
  begin
  repeat
   Writeln('antiguedad:');
   Readln(anios);
  until anios>=0;
   case anios of
    0..5: sueldo:=base*1.05*0.89-500;
    6..10:sueldo:=base*1.08*0.89-500;
    11..15:sueldo:=base*1.12*0.89-500;
    16..100:sueldo:=base*1.2*0.89-500;
   end;
   acumsuel:=sueldo+acumsuel;
   if sueldo>sueldomax then
    begin
      sueldomax:=sueldomax;
      nombremax:=nombre;
    end;
   cont:=cont+1;
  Writeln('nombre:',nombre,',sueldo:',sueldo:8:2);
  Writeln('nombre del empleado(escribir "finalizar" para terminar)');
  Readln(nombre);
  end;
  promedio:=acumsuel/cont;
  Writeln('el empleado que mas cobra es ',nombremax);
  Writeln('el sueldo promedio es de ',promedio:6:2);
  Readln();
end.

