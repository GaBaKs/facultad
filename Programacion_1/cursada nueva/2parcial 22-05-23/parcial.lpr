program parcial;
const
  max=30;
 type
   Tmatr=array[1..3, 1..3] of real;
   Tmat=array[1..3,1..3] of byte;
    Tvecr=array[1..3] of record
      nivel: byte;
      Totautos:byte;
      Tpromedio:real;
      end;
procedure matrices(var matautos:Tmat;var M:byte;var N:byte;Var mathoras:Tmatr);
 var
   i,j:byte;
 begin
  Writeln('ingrese N');
  Readln(N);
  Writeln('ingrese M');
  Readln(M);
 for  i:=1 to N do
  for j:=1 to M do
   begin
    Writeln('ingrese los autos en el espacio ',i,', ',j);
    Readln(matautos[i,j]);
    Writeln('cantidad de horas en el espacio ',i,', ',j);
    Readln(mathoras[i,j]);
   end;
 Writeln('lectura completada');
end;

procedure incisoa(matautos:Tmat;mathoras:Tmatr;M,N:byte;var Vniveles:Tvecr;var k:byte);
 var
  i,j:byte;
  flag:boolean;
  acuma:byte;
  acumh:real;
 begin
  k:=0;
   for i:=1 to N do
     begin
       flag:=false;
       j:=1;

       acuma:=0;
       acumh:=0;
          While (j<=M) and (not flag) do
           begin
             if matautos[i,j]<>0 then
               begin
                 acuma:=acuma+matautos[i,j];
                 acumh:=acumh+mathoras[i,j];
               end
             else flag:=true;
             j:=j+1;
           end;
          if not flag then
            begin
             k:=k+1;
             with Vniveles[k] do
              begin
                nivel:=i;
                Totautos:=acuma;
                Tpromedio:=acumh/acuma;
              end;
            end;
     end;
 for i:=1 to k do
  Writeln('Nivel: ',Vniveles[i].nivel,'. Total de autos: ',Vniveles[i].Totautos,'. Tiempo promedio de ocupacion por auto(h): ',(Vniveles[i].Tpromedio):3:2);
 end;

function incisob(matautos:Tmat;i,j,N,M:byte;X:byte):byte;

 begin
  if i=0 then
   incisob:=0
  else
           if matautos[i,j]>X then
             incisob:=incisob(matautos,i-1,M,N,M,X)+1
           else
               if j<>0 then
                  incisob:=incisob(matautos,i,j-1,N,M,X)
               else
                incisob:=incisob(matautos,i-1,M,N,M,X);
end;


var
 matautos:Tmat;
 X,M,N,k:byte;
 mathoras:Tmatr;
 Vniveles:Tvecr;
 begin
   matrices(matautos,M,N,mathoras);
   incisoa(matautos,mathoras,M,N,Vniveles,k);
   repeat
   Writeln('ingrese un valor de X');
   Readln(X);
   Writeln('la cantidad de niveles que tienen una plaza con una cant de vehiculos mayor a X es de ', incisob(matautos,N,M,N,M,X));

   until X=0;
   Readln();
 end.

