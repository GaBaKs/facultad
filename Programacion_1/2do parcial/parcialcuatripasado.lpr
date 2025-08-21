program recu_junio_2022;
{a) Para un código de surtidor C, el tipo de combustible que más litros vendió. Puede no existir.
b) Porcentaje de importe de venta de cada tipo de combustible respecto de la venta total de combustible.
c) Para aquellos surtidores que vendieron más de X litros de un tipo de combustible, generar una estructura
con: código de surtidor y tipo de combustible. Luego listarlos}
const
  max=30;
type
  st10=string[10];
  st4=string[4];
  reg1 = record
    tipo:st10;
    imp:real;
  end;
  TV=array[1..max]of reg1;
  TM=array[1..max,1..max]of real;
  TVst4=array[1..max]of st4;
  TVR=array[1..max]of real;
procedure leer1(nt:byte;VAR k:byte;VAR ventas:TVst4;VAR mat:TM);
VAR
  arch:text;
  i,j:byte;
begin
  assign(arch,'VENTAS.txt');
  reset(arch);
  readln(arch,k);
  i:=0;
  while not eof(arch) do
    begin
      i:=i+1;
      read(arch,ventas[i]);
      for j:=1 to nt do
        read(arch,mat[i,j]);
      readln(arch);
    end;
  close(arch);
end;
procedure leer2(VAR comb:TV;VAR nt:byte);
VAR
  arch:text;
  n:byte;
begin
  assign(arch,'COMBUSTIBLES.txt');
  reset(arch);
  n:=0;
  readln(arch,nt);
  while not eof(arch) do
    begin
      n:=n+1;
      readln(arch,comb[n].tipo,comb[n].imp);
    end;
  close(arch);
end;
function sup(c:st4;k,nt:byte;mat:TM;comb:TV;ventas:TVst4):st10; //inciso a
VAR
  i,j,s:byte;
  maximo:real;
begin
  i:=0;
  maximo:=0;
  while(c<>ventas[i])and (i<k) do
    begin
      i:=i+1;
    end;
  if i=k then
    sup:=('no existe')
  else
    begin
      for j:=1 to nt do
        begin
          if maximo<mat[i,j]then
            begin
              maximo:=mat[i,j];
              s:=j;
            end;
        end;
      sup:=comb[s].tipo;
    end;
end;
procedure porc(k,nt:byte;mat:TM;comb:TV);  //inciso b
VAR
  i,j:byte;
  tot:real;
  vec:TVR;
begin
  tot:=0;
  for i:=1 to k do
    for j:=1 to nt do
      begin
        vec[j]:=vec[j]+(mat[i,j]*comb[j].imp);
        tot:=tot+(mat[i,j]*comb[j].imp);
      end;
  for j:=1 to nt do
    writeln('el porcentaje de combustible ',comb[j].tipo,' es de %',((vec[j]/tot)*100):8:2);
end;
procedure busca (ventas:TVst4;nt,k:byte;comb:TV;mat:TM);  //inciso c
VAR
  x:real;
  i,j:byte;
begin
  writeln('ingrese la cantidad de litros a superar');
  readln(x);
  for i:=1 to nt do
    for j:=1 to k do
      begin
        if mat[i,j]>x then
          begin
            writeln('el surtidor ',ventas[i],' vendio mas de ',x,' cantidad del combustible ',comb[j].tipo);
          end;
      end;
end;
VAR
  comb:TV;
  ventas:TVst4;
  nt,k:byte;
  c:st4;
  mat:TM;
begin
  leer1(nt,k,ventas,mat);
  leer2(comb,nt);
  writeln('ingrese el codigo del surtidor');
  readln(c);
  writeln('el surtidor ',c,' vendio una mayor cantidad de combustible ',sup(c,k,nt,mat,comb,ventas));
  porc(k,nt,mat,comb);
  busca(ventas,nt,k,comb,mat);
  readln;
end.
