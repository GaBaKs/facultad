program ejer8;
const
  max=30;
 type
   matriz=array[1..max,1..max]of byte;
   vec=array[1..max]of byte;
 function anashe(mat:matriz;n,m:byte;vector:vec): byte;
 var
   maximo:byte;
 begin
     if m>0 then
        maximo:=anashe(mat,n,m-1,vector);
     if maximo<mat[n,m] then
         maximo:=mat[n,m];
     anashe:=maximo;
   end
  else maximo:=0;
 end;
procedure anashe2
 begin

 var
   mat:matriz;
   n,m:byte;
begin
  mat[1,1]:=1;
  mat[1,2]:=2;
  mat[1,3]:=3;
  mat[2,1]:=4;
  mat[2,2]:=2;
  mat[2,3]:=5;
  anashe(mat,2,3,vector);
  readln();
end.

