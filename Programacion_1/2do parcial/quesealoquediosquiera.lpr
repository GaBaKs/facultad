program quesealoquediosquiera;
const
  max=30;
type
  trec=array[1..max]of record
    nivel:byte;
    totaut:byte;
    tprom:real;
  end;
  matriz=array[1..max,1..max] of integer;
  matriz2=array[1..max,1..max] of real;
procedure arreglo(var VNiveles:trec;N,M:byte;matautos:matriz;mathoras:matriz2;var s:byte;);
 var
 i,j:byte;
 bool:boolean;
 acumaut:word;
 acumt:real;
 begin
  s:=0
  acumaut:=0;
  acumt:=0;
  for i:=1 to N do
   begin
  bool:=false;
    for j:=1 to M do
     begin
      if matautos[i,j]<>0 then
       acumaut:=acumaut+matautos[i,j];
       acumt:=acumt+mathoras[i,j];
      else bool;
     end;
      if not bool then
      begin
       s:=s+1;
       VNiveles[s].Nivel:=i;
       VNiveles[s].totaut:=acumaut;
       VNiveles[s].tprom:=acumt/acumaut;
      end;
      acumt:=0;
      acumaut:=0;
   end;

 end;
function ejerciciob(matautos:matriz;i,j,m,x:byte;flag:boolean):integer;
 begin
  if i>0 then
   begin
    if j>0 then
     begin
      if (matautos[i,j]>x) and (not flag) then
       ejerciciob:=ejerciciob(matautos,i,j-1,m,x,true)+1;
      else
       if matautos[i,j]>x then
        ejerciciob:=ejerciciob(matautos,i-1,m,m,x,false)-1
       else
        ejerciciob:=ejerciciob(matautos,i,j-1,m,x,true);
     end;
   else
    ejerciciob:=ejerciob(matautos,i-1,m,m,x,false);
  else
   ejerciciob:=0;
 var
 N,M:byte;
 matautos:matriz;
 mathoras:matriz2;
begin
 N:=2;
 M:=2;
 matautos[1,1]:=1;
 matautos[1,2]:=2;
 matautos[2,1]:=3;
 matautos[2,2]:=0;
 mathoras[1,1]:=2;
 mathoras[1,2]:=3;
 mathoras[2,1]:=6;
 mathoras[2,2]:=7;
 end.

