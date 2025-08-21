program ejer4;
 var
    d1,m1,a1,d2,m2,a2 : integer ;
begin
  repeat
   Writeln('indique fecha 1(dia mes y year separados con enter)');
   Readln(d1,m1,a1);
  until
   (d1<=31) and (m1<=12) and (a1>0) ;
  repeat
   Writeln('indique fecha 2');
   Readln(d2,m2,a2);
  until
  (d2<=31) and (m2<=12) and (a2>0);
  if a1>a2 then
   Writeln('la fecha 2 es mas antigua que la 1')
  else if a1=a2 then
   begin
    if m1>m2 then
    Writeln('la fecha 2 es mas antigua que la 1')
    else if m1=m2 then
     begin
      if d1>d2 then
      Writeln('la fecha 2 es mas antigua que la 1')
      else
      Writeln('la fecha 1 es mas antigua que la 2');
     end;
  Readln();
end.

