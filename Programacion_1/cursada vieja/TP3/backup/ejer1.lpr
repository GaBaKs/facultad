program ejer1;
  var
   N,contmax,num,max,pos,i : integer;
begin
  max:=0 ;
  contmax:=0 ;
  pos:=1 ;
  Writeln('Cuantos numeros enteros desea ingresar');
  Readln(N);
  Writeln('ingrese un numero');
  Readln(max);
  for i:=1 to N-1 do
   begin
   Writeln('ingrese un numero');
   Readln(num);
    if num>max then
    begin
    contmax:=1;
    max:=num;
    pos:=pos+1;
    end ;
    if num=max then
    contmax:=contmax+1;
   end;
  Writeln('el primer numero ingresado ocupa el lugar ',pos);
  Writeln('el numero maximo es ',max,' y aparece ',contmax,'veces');
  Readln();
end.

