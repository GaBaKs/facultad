program recursividad;
const
  max=30;
 type
   Tmat=array[1..max,1..max] of integer;
   Tvec=array[1..max] of byte;



  procedure cargarmatriz(var mat:Tmat;var n:byte);
   var
     i,j:byte;
   begin
     for i:=1 to n do
      for j:=1 to n do
        mat[i,j]:=1;
   end;

  procedure generarvector(mat:Tmat;n:byte;i,j,cont:byte;var Vec:Tvec;var k:byte);
    begin
   if i>0 then
      begin
         if j>0 then
          begin
            if mat[i,j]>0 then
            generarvector(mat,n,i,j-1,cont+1,Vec,k)
            else generarvector(mat,n,i,j-1,cont,Vec,k);
          end
             else if cont>0 then
               begin
                 k:=k+1;
                 Vec[k]:=cont;
               end
                 generarvector(mat,n,i-1,n,0,Vec,k);
      end;
    end;

 procedure mostrarvector(Vec:Tvec;k:byte);
  var
   i:byte;

  begin
   for i:=1 to k do
    Writeln(Vec[k]);
  end;
 var
   k,cont,n,i,j:byte;
   vec:Tvec;
   mat:Tmat;
begin
  Writeln('ingrese un N');
  Readln(n);
  cargarmatriz(mat,n);
  k:=0;
  generarvector(mat,n,n,n,0,Vec,k);
  mostrarvector(vec,k);
  readln();
end.
