program parcial;
 const
   max=100;
   N=7;
   diasp=5;
 type
   st5=string[5];
   Tmat=array[1..N, 1..max] of real;
   Tvec=array[1..max] of st5;
   Tvecr=array[1.. max] of record
     codigo:st5;
     montof:real;
   end;

 procedure lecrubros(var vec:Tvec;var M:byte);
  var
   arch:Text;

  begin
   M:=0;
   Assign(arch,'Rubros.TXT');
   Reset(arch);
   While not eof(arch) do
   begin
    M:=M+1;
    Readln(arch,vec[M]);
   end;
   Close(arch);
 end;
procedure iniciarmatriz(var mat:Tmat;M:byte);
 var
  i,j:byte;

 begin
  for i:=1 to N do
   for j:=1 to M do
    mat[i,j]:=0;
 end;
function busca(vec:Tvec;cod:st5;M:byte):byte;
 var
  i:byte;
 begin
 i:=1;
  While (i<=M) and (cod<>vec[i]) do
    i:=i+1;
       busca:=i;
     end;
 procedure lecventas(var mat:Tmat;M:byte;var cod:st5;vec:Tvec);
  var
   arch:text;
   dia:byte;
   montov:real;
   pos:byte;
  begin

  Assign(arch,'Ventas.TXT');
  Reset(arch);
  While not eof(arch) do
    begin
     Readln(arch,cod,dia,montov);
     pos:=busca(vec,cod,M);
     mat[dia,pos]:=mat[dia,pos]+montov;
    end;
  Close(arch);
end;

 function ventaprom5(mat:Tmat;vec:Tvec;M:byte):byte;
 var
  prom,promin:real;
  i,j:byte;
 begin
  promin:=10000;
 for j:=1 to M do
  begin
   prom:=0;
   for i:=1 to diasp do
     prom:=prom+mat[i,j];
    prom:=prom/diasp;
   if prom<promin then
    begin
     promin:=prom;
     ventaprom5:=j;
    end;
  end;
 end;
procedure iniciarvector(var vecr:Tvecr;M:byte);
 var
  i,j:byte;

 begin
  for i:=1 to M do
   begin
   vecr[i].montof:=100000;
   vecr[i].codigo:='';
   end;
 end;
procedure finderubro(mat:Tmat;vec:Tvec;M:byte;var vecr:Tvecr;X:real;var con2:byte);
var
 suma1,suma2:real;
 nombre1,nombre2:st5;
 i,cont:byte;
begin
cont:=1;
con2:=0;
 iniciarvector(vecr,M);
 for i:=1 to M do
  begin
   suma1:=mat[6,i]+mat[7,i];
   nombre1:=vec[i];
 if suma1>X then
 begin
   con2:=con2+1;
   While cont<=M do
     begin
       if suma1<vecr[cont].montof then
         begin
            suma2:=vecr[cont].montof;
            nombre2:=vecr[cont].codigo;
            vecr[cont].montof:=suma1;
            vecr[cont].codigo:=nombre1;
            cont:=cont+1;
            if cont<=M then
               begin
                 nombre1:=vecr[cont].codigo;
                 suma1:=vecr[cont].montof;
                 vecr[cont].montof:=suma2;
                 vecr[cont].codigo:=nombre2;
               end;
         end
       else cont:=cont+1;
     end;
   cont:=1;
 end;
end;
 end;
procedure mostrararreglo(vecr:Tvecr;con2:byte);
var
 i:byte;

begin
Writeln('muestro arreglo mayor a X');
 for i:=1 to con2 do
  begin
   Writeln('codigo de rubro: ',vecr[i].codigo,'. monto total vendido en fin de semana: ',(vecr[i].montof):2:2);
end;
end;






var
 vec:Tvec;
 vecr:Tvecr;
 M,con2:byte;
 cod:st5;
 mat:Tmat;
 X:real;

begin
 lecrubros(vec,M);
 iniciarmatriz(mat,M);
 lecventas(mat,M,cod,vec);
 Writeln('El rubro con menor venta promedio diario en los primeros 5 dias es ',vec[ventaprom5(mat,vec,M)]);
 Writeln('ingrese un X');
 Readln(X);
 finderubro(mat,vec,M,vecr,X,con2);
 mostrararreglo(vecr,N);
 Readln();
end.

