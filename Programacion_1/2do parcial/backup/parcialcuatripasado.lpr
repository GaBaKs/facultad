program parcialcuatripasado;
const
  max=30;
 type
   registro= record
     nivel:byte;
     totaut:word;
     tprom:real;
     end;
   vecreg= array[1..max] of registro;
   matriza=array[1..max,1..max] of byte;
   matrizb=array[1..max,1..max] of real;
 procedure arreglo(var VNiveles:vecreg;N:byte;M:byte;var z:byte;matautos:matriza;mathoras:matrizb);
 var
  i,j:byte;
  acum:word;
  acumt:real;
  bool: boolean;
 begin
 acum:=0;
 acumt:=0;
 z:=1;
  for i:=1 to N do
   begin
    for j:=1 to M do
     begin
     if matautos[i,j]<>0 then
      begin
       acum:=matautos[i,j]+acum;
       acumt:=acumt+mathoras[i,j];
      end
     else bool:=true;
     end;
    if not bool then
     begin
      with Vniveles[z] do
       begin
        nivel:=i;
        totaut:=acum;
        tprom:=(acumt/acum);
        end;
       z:=z+1;
     end;
    acum:=0;
    acumt:=0;
   end;
end;
function masx(matautos:matriza;M,i,j:byte;x:word;flag:boolean):word;
begin
  if i>0 then
   begin
    if j>0 then
     begin
      if (matautos[i,j]>x) and (not flag) then
      masx:=masx(matautos,M,i,j-1,x,true)+1
      else
       if matautos[i,j]>x then
        masx:=masx(matautos,M,i-1,M,x,false)-1
      else
       masx:=masx(matautos,M,i,j-1,x,true);
     end
     else
      masx:=masx(matautos,M,i-1,M,x,false);
    end
   else
   masx:=0;
   end;




  var
   i,j:byte;
   matautos:matriza;
   mathoras:matrizb;
   N,M,z:byte;
   x:word;
   VNiveles:vecreg;
  begin
   N:=2;
   M:=2;
   matautos[1,1]:=1;
   matautos[1,2]:=2;
   matautos[2,1]:=1;
   matautos[2,2]:=2;
   mathoras[1,1]:=9.5;
   mathoras[1,2]:=15;
   mathoras[2,1]:=6;
   mathoras[2,2]:=0;
   arreglo(VNiveles,N,M,z,matautos,mathoras);
   Writeln('ingrese un X');
   Readln(x);
   Writeln(masx(matautos,M,N,M,x,false));
   Readln();
end.

