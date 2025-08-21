program recursivo;
const
  max=30;
type
  Tmat=array[1..max,1..max] of real;

  procedure iniciarmatriz(var mat:Tmat);
   begin
     mat[1,1]:=2;
     mat[1,2]:=3;
     mat[2,1]:=-4;
     mat[2,2]:=1;
     mat[3,1]:=1;
     mat[3,2]:=1;
   end;

  function vermat(mat:Tmat;N,M,i,j:byte;flag:boolean):boolean;
   begin
   if i=0 then
     vermat:=flag
  else
   begin
     if j>0 then
       begin
            if ((mat[N,M]*mat[i,j])>0) and (not flag)then
              vermat:=vermat(mat,N,M,i,j-1,false)
            else vermat:=vermat(mat,N,M,0,0,true);
       end else vermat:=vermat(mat,N,M,i-1,M,false);
   end;
 end;



  var
    mat:Tmat;
    N,M:byte;
    Nmitad:real;
    i,j:byte;

begin
  Repeat
    Writeln('ingrese un N impar');
    Readln(N);
  until N mod 2 <>0;
  Writeln('ingrese un M');
  Readln(M);
  Nmitad:=N/2-0.5;
  N:=byte(round(Nmitad));
  iniciarmatriz(mat);
  if vermat(mat,N,M,N,M,false) then
    Writeln('Los elementos sobre la fila del medio de la matriz no tienen el mismo signo')
  else
    Writeln('Los elementos sobre la fila del medio de la matriz tienen el mismo signo');
 Readln();
end.

