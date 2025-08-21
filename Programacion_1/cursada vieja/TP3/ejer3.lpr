program ejer3;
var
  numant,num,cont,nums,i:integer;
  begin
 Writeln('numeros enteros a ingresar:');
 Readln(nums);
 Writeln('Ingresa un numero entero');
 Readln(numant);
 For i:=1 to nums-1 do
  begin
 Writeln('ingresa un numero entero');
 Readln(num);
  if num>numant then
    begin
    numant:=num;
    cont:=cont+1;
    end;
  end;
  Writeln('los numeros superaron al anterior ',cont,' veces.');
  Readln();
end.

