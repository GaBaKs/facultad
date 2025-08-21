program ejer4;
var
  numant,num,nums,i,dif,par1,par2:integer;

  begin
   par2:=1;
 Writeln('cuantos numeros desea ingresar');
 Readln(nums);
   Writeln('ingrese un numero');
   Readln(numant);
 For i:=1 to nums-1 do
   begin
   Writeln('ingrese un numero');
   Readln(num);
   if numant-num>dif then
   begin
     dif:=numant-num;
     par1:=par2;
   end;
   numant:=num;
   par2:=par2+1;
   end;
 Writeln('la maxima diferencia es de ',dif,' y corresponde al par ',par1);
 Readln();
end.

