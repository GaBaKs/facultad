program parcial;
 const
   max=3;
   max2=60;
 type
   Tmat=array[1..max,1..max2] of byte;
   Tvecr=array[1..max2] of record
     dia:byte;
     turno:char;
   end;
procedure iniciarmatriz(var mat:Tmat;i,j:byte);
 begin
  if j>0 then
   begin
     if i>0 then
      begin
       mat[i,j]:=0;
       iniciarmatriz(mat,i-1,j);
      end
     else iniciarmatriz(mat,max,j-1);
   end;
 end;
 procedure lecturaventas(var mat:Tmat;var N:byte;var vecr:Tvecr);
   var
    arch:text;
    cantprom,prom,i:byte;
    aux:char;

   begin

    N:=0;
    Assign(arch,'VENTAS.TXT');
    Reset(arch);
    While not eof(arch) do
     begin
      N:=N+1;
      Read(arch,vecr[N].dia,aux,vecr[N].turno,cantprom);
      for i:=1 to cantprom do
       begin
        Read(arch,prom);
        mat[N,prom]:=mat[N,prom]+1;
       end;
      Readln(arch);
     end;
    Close(arch);
   end;


 procedure recaudaciontdia(mat:Tmat;N:byte;vecr:Tvecr);
  var
   Dias:byte;

  begin
   Writeln('ingrese un dia');
   Readln(Dias);


  end;


begin
  iniciarmatriz(mat,max2,max);
end.

