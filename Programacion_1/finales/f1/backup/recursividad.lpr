program recursividad;
 const
   max=100;

  Type
    Tmat=array[1..max,1..max] of word;

      procedure cargarmatriz(var mat:Tmat;var N,M:byte);
   var
     i,j:byte;
   begin
     for i:=1 to N do
      for j:=1 to M do
        mat[i,j]:=1;
     mat[1,1]:=0];
   end;
  function empleadosx(mat:Tmat;N,M,i,j:byte;X,acum:word):byte;
    begin
     if j=0 then
      empleadosx:=0
    else
        begin
             if i>0 then
               begin
                 acum:=acum+mat[i,j];
                 empleadosx:=empleadosx(mat,N,M,i-1,j,X,acum);
               end
              else
                  begin
                       if acum>=X then
                        empleadosx:=1+empleadosx(mat,N,M,N,j-1,X,0)
                        else empleadosx:=empleadosx(mat,N,M,N,j-1,X,0);
                  end;
        end;
 end;

var
  mat:Tmat;
  N,M,i,j:byte;
  X,acum:word;

begin
  Readln(N,M);
  Writeln('Ingrese un x');
  Readln(X);
  cargarmatriz(mat,N,M);
  Writeln(' la cantidad de sucursales que tienen al menos ',X,' empleados en total es de ',empleadosx(mat,N,M,N,M,X,0));
  Readln();
end.

