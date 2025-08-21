program parcial;
  const
    max=100;

  type
    st10=string[10];
    st4=string[4];
    Tvecr=array[1..max] of record
      nombre:st10;
      precio:real;
     end;
    Tvec=array[1..max] of st4;
    Tmat=array[1..max,1..max] of word;
    Tvec2=array[1..max] of real;
  Tvecr2=array[1..max] of record
    codigo:st4;
    tipocomb:st10;
  end;

procedure lecturacomb(var vecr:Tvecr;var N:byte);
   var
     i:byte;
     arch:Text;
  begin

   Assign(arch,'Combustible.TXT');
   Reset(arch);
   Readln(arch,N);
   for i:=1 to N do
    Readln(arch,vecr[i].nombre,vecr[i].precio);
   close(arch);
  end;

procedure lecturaventas(var mat:tmat;N:byte;var vec:Tvec;var k:byte);
   var
    arch:text;
    i:byte;
  begin
   assign(arch,'Ventas.TXT');
   Reset(arch);
   k:=0;
  While not eof(arch) do
   begin
    k:=k+1;
     read(arch,vec[k]);
     for i:=1 to N do
      begin
       read(arch,mat[k,i]);
      end;
     readln(arch);
    end;
  close(arch);
 end;

procedure buscalitros(mat:Tmat;vec:Tvec;N,k:byte;vecr:Tvecr);
 var
  i,j,L:byte;
  max:word;
  C:st4;
 begin
 Writeln('ingrese un codigo de surtidor');
Readln(C);
i:=0;
 max:=0;
  While (i<k) and (vec[i]<>C) do
   begin
     i:=i+1;
     if vec[i]=C then
      begin
        for j:=1 to N do
            if mat[i,j]>max then
             begin
              max:=mat[i,j];
              L:=j;
             end;
       end;
    end;
 if vec[i]<>C then
  Writeln('el codigo ingresado no es valido')
 else Writeln('el combustible mas vendido en el surtidor ',C,' es ',vecr[L].nombre);
 end;

procedure porcentajeven(mat:Tmat;vecr:Tvecr;N,k:byte);
 var
  i,j:byte;
  acumtot,acum:real;
  porcentaje:real;
  vecacum:Tvec2;
 begin
 acumtot:=0;
 acum:=0;
 for i:=1 to N do
  begin

   for j:=1 to k do

    begin
      acum:=acum+mat[j,i];
    end;
   acum:=acum*vecr[i].precio;
   acumtot:=acumtot+acum;

   vecacum[i]:=acum;
   acum:=0;
  end;
for i:=1 to N do
 begin
  porcentaje:=(vecacum[i]/acumtot)*100;
  Writeln(vecr[i].nombre,'=',(porcentaje):2:2,'%');
 end;
end;

procedure generararreglo(mat:Tmat;vec:Tvec;vecr:Tvecr;N,k:byte;var vecrcod:Tvecr2;var H:byte);
 var
  i,j:byte;
  X:real;
 begin
 H:=0;
  Writeln('ingrese una cantidad de litros X a superar');
  Readln(X);

   for i:=1 to k do
    begin                             //k es la cant de codigos(filas)
     for j:=1 to N do
      begin
       if mat[i,j]>X then
        begin
         H:=H+1;
         vecrcod[H].tipocomb:=vecr[j].nombre;
         vecrcod[H].codigo:=vec[i];
        end;
      end;
    end;
 end;

procedure mostrararreglo(vecrcod:Tvecr2;H:byte);
 var
  i:byte;

 begin
  for i:=1 to H do
   Writeln(vecrcod[i].codigo,',',vecrcod[i].tipocomb);
 end;

function busquedar(vec:Tvec;k:byte;C:st4):byte;
 var
  i:byte;

 begin
 i:=0;
  While (i<k) and (vec[i]<>C) do
   begin
    i:=i+1;
    if vec[i]=C then
      busquedar:=i;
  end;
  if vec[i]<>C then
   busquedar:=0;


 end;

function maximorecursivo(mat:Tmat;i,N,j:byte;max:real;posmax:byte):byte;

 begin
  if j=0 then
   maximorecursivo:=posmax
  else
   begin
    if mat[i,j]>max then
     begin
      max:=mat[i,j];
      posmax:=N;
     end;
    maximorecursivo:=maximorecursivo(mat,i,N,j-1,max,posmax);
  end;

   end;

procedure incisoarecursivo(mat:Tmat;vec:Tvec;i,N,k:byte;vecr:Tvecr;var C:st4);
 var
  aux:byte;
  posmax:byte;

 begin

  Writeln('ingrese un codigo de surtidor');
  Readln(C);
  aux:=busquedar(vec,k,C);
  if aux<>0 then
  Writeln('el tipo de combustible que se vendio mas en el surtidor ',vec[aux],' es ',vecr[maximorecursivo(mat,aux,N,N,-1,posmax)].nombre)
  else Writeln('el codigo ingresado no es valido');
 end;




var
 vecr:Tvecr;
 i,H,N,k:byte;
 mat:Tmat;
 vec:Tvec;
 vecrcod:Tvecr2;
 C:st4;
begin
  lecturacomb(vecr,N);
  lecturaventas(mat,N,vec,k);
  //buscalitros(mat,vec,N,k,vecr);
  //porcentajeven(mat,vec,vecr,N,k);
  //generararreglo(mat,vec,vecr,N,k,vecrcod,H);
  //mostrararreglo(vecrcod,H);
  incisoarecursivo(mat,vec,i,N,k,vecr,C);


  Readln();
end.

