program parcial;
 const
   max=30;

  type
    st10=string[10];
    Tvecr=array[1..max] of record
      nombre: st10;
      precio: word;
    end;
    Tmat=array[1..max,1..max] of word;
    Tvec=array[1..max] of record
      codigo:byte;
      precio:real;
    end;

Procedure lectura1(var Vreg:Tvecr;var N:byte);
var
 arch:text;
 aux:char;
 begin
   N:=0;
   Assign(arch,'CEREALES.TXT');
   Reset(arch);
   While not eof(arch) do
    begin
      N:=N+1;
      Read(arch,aux);
      While aux<>' ' do
       begin
        Vreg[N].nombre:=Vreg[N].nombre+aux;
        Read(arch,aux);
       end;
      readln(arch,Vreg[N].precio);
    end;
  close(arch);
  Writeln('lectura 1 completada');
 end;

procedure lectura2(var mat:Tmat;N:byte;var imax:byte;Vreg:Tvecr);
var
 arch:text;
 aux:char;
 j:byte;
 i:word;
 nom:st10;
 ton:word;
 flag:boolean;
begin
 flag:=false;
Assign(arch,'EXPORTACIONES.TXT');
Reset(arch);
imax:=0;
j:=1;
nom:='';

While not eof(arch) do
 begin
  read(arch,i,aux,aux);
  While aux<>' ' do
  begin
   nom:=nom+aux;
   read(arch,aux);
  end;
  readln(arch,ton);
   if i>imax then
   imax:=i;
    While (not flag) and (j<=N) do
     begin
      if Vreg[j].nombre=nom then
       begin
        mat[i,j]:=mat[i,j]+ton;
        Flag:=true;
       end;
      j:=j+1;
     end;
    Flag:=false;
    j:=1;
    nom:='';
   end;
Close(arch);
end;

function incisoa(Vreg:Tvecr;mat:Tmat;N:byte;imax:byte;C:st10):byte;
 var
  cont:byte;
  j,i:byte;
  flag:boolean;
begin
j:=1;
cont:=0;
flag:=false;
 While (not flag) and (j<=N) do
  begin
   if Vreg[j].nombre=C then
    begin
     flag:=true;
     for i:=1 to imax do
       if mat[i,j]<>0 then
        cont:=cont+1;
    end;
   j:=j+1;
  end;
 incisoa:=cont;
end;

procedure incisob(Vreg:Tvecr;mat:Tmat;N:byte;imax:Byte);
var
 Z,acum:word;
 j,i,k:byte;

 Vpesos:Tvec;
 begin
  i:=1;
  Writeln('ingrese un valor de toneladas Z entero positivo');
  Readln(Z);
  k:=0;
  While i<=imax do
   begin
    acum:=0;
    for j:=1 to N do
     acum:=acum+mat[i,j];
    if acum>Z then
     begin
      k:=k+1;
      for j:=1 to N do
       Vpesos[k].precio:=Vpesos[k].precio+mat[i,j]*Vreg[j].precio*360;
      Vpesos[k].codigo:=i;
     end;
    i:=i+1;
   end;
  for j:=1 to k do
   begin
    if Vpesos[j].precio>100000000 then
     Vpesos[j].precio:=Vpesos[k].precio*1.25
     else Vpesos[j].precio:=Vpesos[j].precio*0.95;
    Writeln('codigo de silo: ',Vpesos[j].codigo,'. Importe total en PESOS del silo: ',(Vpesos[j].precio):8:2);
   end;
 end;

var
 Vreg:Tvecr;
 N,imax:byte;
 mat:Tmat;
 C:st10;



begin
  lectura1(Vreg,N);
  lectura2(mat,N,imax,Vreg);
  Writeln('ingrese un tipo de cereal C');
  Readln(C);
  if incisoa(Vreg,mat,N,imax,C)<>0 then
  Writeln('El cereal ',C,' se encuentra guardado en ',incisoa(Vreg,mat,N,imax,C),' silo/s')
  else Writeln('El cereal ',C,' no se encuentra guardado en ningun silo o el tipo de cereal no es valido.');
  incisob(Vreg,mat,N,imax);
  Readln();

end.

