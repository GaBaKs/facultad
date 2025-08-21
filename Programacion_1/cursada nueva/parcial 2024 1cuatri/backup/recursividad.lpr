program recursividad;
 const
   max=100;
type
 Tmat=array[1..max,1..max] of integer;
 Tvec=array[1..max] of record
   fila:byte;
   columna:byte;
  end;
procedure matriz(var mat:Tmat;var N:byte;var M:byte);
begin
 N:=3;
 M:=3;
 mat[1,1]:=1;
 mat[1,2]:=2;
 mat[1,3]:=3;
 mat[2,1]:=1;
 mat[2,2]:=22;
 mat[2,3]:=33;
 mat[3,1]:=0;
 mat[3,2]:=0;
 mat[3,3]:=0;

 end;


procedure recursividad(mat:Tmat;i,j,N,M:byte;suma,min:integer;imin:byte;jmin:byte;var vec:Tvec;var V:byte);
begin
if i>0 then
  begin
   if j>0 then
     begin
        suma:=mat[i,j]+suma;
        if mat[i,j]<min then
            begin
               min:=mat[i,j];
               imin:=i;
               jmin:=j;
            end;
        recursividad(mat,i,j-1,N,M,suma,min,imin,jmin,vec,V);
     end
   else begin
       if suma>0 then
         begin
          V:=V+1;
        vec[V].fila:=imin;
        vec[V].columna:=jmin;
         end;
   recursividad(mat,i-1,M,N,M,0,30000,imin,jmin,vec,V);
  end;
end;
end;
var
  mat:Tmat;
  V,i,j,N,M:byte;
  suma,min:integer;
  imin,jmin:byte;
  vec:Tvec;
  k:byte;
begin
  V:=0;
  matriz(mat,N,M);
  recursividad(mat,N,M,N,M,0,30000,imin,jmin,vec,V);
  for k:=1 to V do
   Write(vec[k].fila,' columna: ',vec[k].columna,' ');
  readln();
end.

