program recursividad;
const
  max=30;
type
  Tmat=array[1..3, 1..3] of word;
  Tvec=array[1..3] of word;

function ejer2(mat:Tmat;vec:Tvec;i,j,N,M:byte):byte;
 begin
 if i=0 then
  ejer2:=0
  else
    begin
      if (j>0) then
         if (mat[i,j] mod vec[i])=0 then
             ejer2(mat,vec,i,j-1,N,M)
         else ejer2(mat,vec,i-1,M,N,M)
      else
        begin
         if j=0 then
             ejer2:=ejer2(mat,vec,i-1,M,N,M)+1
         else ejer2:=ejer2(mat,vec,i-1,M,N,M);

    end;
 end;
end;
 var
   mat:Tmat;
   vec:Tvec;
   N,M:byte;
   i,j:byte;
begin
Writeln('ingrese N');
Readln(N);
Writeln('ingrese M');
Readln(M);

 for i:=1 to N do
  for j:=1 to M do
   begin
     Writeln('ingrese el numero en el espacio ',i,' ',j);
     Readln(mat[i,j]);
   end;

 for i:=1 to N do
  begin
   Writeln('ingrese el numero en el espacio para el vector: ',i);
   Readln(vec[i]);
  end;

 Writeln('anashe');
 Writeln('la cantidad de filas de la matriz que cumplen que todos sus elementos son multiplos del elemento correspondiente en el vector vec es de ',ejer2(mat,vec,N,M,N,M));
 Readln();
end.

