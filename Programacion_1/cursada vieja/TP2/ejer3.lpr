program ejer3;
     var
       temp : integer  ;
begin
  Readln(temp);
   if (temp>=0)and(temp<20) then
   writeln('Hace frio')
   Else
   if (temp>=20)and(temp<29) then
   writeln('Barbaro')
   Else
   if(temp>=29) then
   writeln('Qué calor!!')
   Else
   Writeln('no salgo de casa');
   Readln();
end.

