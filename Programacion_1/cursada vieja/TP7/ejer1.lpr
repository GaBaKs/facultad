program ejer1;
type
  st20=string[20];
  emp=record
   nom: st20;
   dia,mes:byte;
   anio:word;
  end;
  vec=array[1..30]of emp;

 procedure lec (var vecemp:vec;var i:byte);
  var
   res:char;
   begin
    i:=1;
    Writeln('ingresa datos?(S para ingresar y cualquier otra letra para terminar)');
    Readln(res);
    while res='S' do
     begin
      with vecemp[i] do
       begin
        Writeln('ingrese nombre del empleado');
        Readln(nom);
        repeat
         Writeln('ingrese dia de nacimiento');
         Readln(dia);
        until (dia<=31) and (dia>=1);
        repeat
         Writeln('ingrese mes de nacimiento');
         Readln(mes);
        until (mes<=12) and (mes>=1);
        repeat
         Writeln('ingrese anio de nacimiento');
         Readln(anio);
        until (anio<=2023) and (anio>1900);
       end;
      i:=i+1;
      Write('ingresa datos?(S para ingresar y cualquier otra letra para terminar)');
      Readln(res);
   end;
   end;
 function masfestejos(vecemp:vec;i:byte):st20;
 var
  j:byte;
  o,inv,p,v: byte;
  begin
   o:=0;
   inv:=0;
   p:=0;
   v:=0;
   for j:=1 to i do
    begin
     with vecemp[j] do
      begin
       case mes of
        1..2: v:=v+1;
        3: if dia<21 then
            v:=v+1
            else o:=o+1;
        4..5:o:=o+1;
        6: if dia<21 then
            o:=o+1
           else inv:=inv+1;
        7..8:inv:=inv+1;
        9: if dia<21 then
            inv:=inv+1
            else p:=p+1;
        10..11: p:=p+1;
        12: if dia<21 then
            p:=p+1
            else v:=v+1;
       end;
      end;
    end;
   if (v>o) and (v>p) and (v>inv) then
       masfestejos:='verano';
   if (o>v) and (o>p) and (o>inv) then
       masfestejos:='otonio';
   if (inv>v) and (inv>p) and (inv>o) then
       masfestejos:='invierno';
   if (p>v) and (p>inv) and (p>o) then
       masfestejos:='primavera';
  end;

var
 i:byte;
 vecemp:vec;
begin
 lec(vecemp,i);
 Writeln('se festejan mas cumpleaños en ',masfestejos(vecemp,i));
 Readln();
end.

