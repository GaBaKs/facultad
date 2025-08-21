program ejer13;
 procedure hora(h,m,s:byte);
  var
   stras:byte;
  begin
    Writeln('ingrese una hora');
    Readln(h);
    Writeln('ingrese un minuto');
    Readln(m);
    Writeln('ingrese un segundo');
    Readln(s);
    Writeln('ingrese unos segundos a sumar');
    Readln(stras);
   s:=s+stras;
   if s>=60 then
    begin
     s:=s-60;
     m:=m+1;
     if m>=60 then
      begin
       m:=m-60;
       h:=h+1;
      end;
    end;
   Writeln('la hora resultante es ',h,' horas, ',m,' minutos y ',s,' segundos');
  end;
var
 h,m,s:byte;
begin
 hora(h,m,s);
 Readln();
end.

