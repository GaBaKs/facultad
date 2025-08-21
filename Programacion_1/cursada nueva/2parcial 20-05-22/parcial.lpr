program parcial;
const
  max=100;
 type
  st30=string[30];
  st2=string[2];
  st8=string[8];
  Tmat=array[1..max, 1..max] of byte;
  Tvecr=array[1..max] of record
    nombre:st30;
    codigo:st2;
    end;
procedure lectura1(var Vreg:Tvecr;var N:byte);
 var
  arch:text;
  aux:char;
  flag:boolean;
begin
 N:=0;
 Assign(arch,'PROVINCIAS.TXT');
 Reset(arch);
 While not eof(arch) do
  begin
    flag:=false;
    N:=N+1;
    Read(arch,Vreg[N].codigo,aux);
    Vreg[N].nombre:='';
    While not flag do
     begin
      Read(arch,aux);
      if aux<>' ' then
       Vreg[N].nombre:=Vreg[N].nombre+aux
      else
        begin
          read(arch,aux);
          if upcase(aux) in['A'..'Z'] then
            Vreg[N].nombre:=Vreg[N].nombre+aux
          else flag:=true
        end;
      if flag then
       Readln(arch);
     end;
  end;
 Close(arch);
 Writeln('lectura 1 completada');
end;

procedure lectura2(var mat:Tmat;Vreg:Tvecr;N:byte);
 var
  arch:text;
  aux:char;
  edad:byte;
  cod:st2;
  i:byte;
  dni:st8;
 begin

  Assign(arch,'INSCRIPTOS.TXT');
  Reset(arch);
   While not eof(arch) do
    begin
     i:=1;
     Readln(arch,dni,aux,edad,aux,cod);
      While (Vreg[i].codigo<>cod) and (i<=N) do
        i:=i+1;
      case edad of
       1..9: mat[1,i]:=mat[1,i]+1;
       10..19: mat[2,i]:=mat[2,i]+1;
       20..29: mat[3,i]:=mat[3,i]+1;
       30..39: mat[4,i]:=mat[4,i]+1;
       40..49: mat[5,i]:=mat[5,i]+1;
       50..59: mat[6,i]:=mat[6,i]+1;
       60..69: mat[7,i]:=mat[7,i]+1;
       70..79: mat[8,i]:=mat[8,i]+1;
       80..89: mat[9,i]:=mat[9,i]+1;
       90..100: mat[10,i]:=mat[10,i]+1;
      end;
    end;
  Close(arch);
  Writeln('lectura 2 completada');
 End;

procedure incisoa(Vreg:Tvecr;mat:Tmat;N:byte;X:st2;i:byte;var cont:byte);
 begin
  if (i=0) or (N=0) then
   if cont=0 then
    Writeln('no hay rangos etareos sin inscriptos en el codigo ingresado')
    else Writeln('la cantidad de rangos sin inscriptos es de ',cont)
  else if Vreg[N].codigo=X then
   begin
    if mat[i,N]=0 then
     cont:=cont+1;
    incisoa(Vreg,mat,N,X,i-1,cont);
   end
   else
   incisoa(Vreg,mat,N-1,X,i,cont);
end;

procedure incisob(Vreg:Tvecr;mat:Tmat;N:byte;X:st2;cont:byte);
 var
  R,T,j,i,k,m:byte;
  flag:boolean;
  min,aux:byte;
  nomprov:st30;
 begin
 While not flag do
  begin
   Writeln('b)ingrese el limite inferior de un rango');
   Readln(R);
   case R of
    1:i:=1;
    10:i:=2;
    20:i:=3;
    30:i:=4;
    40:i:=5;
    50:i:=6;
    60:i:=7;
    70:i:=8;
    80:i:=9;
    90:i:=10;
    else flag:=true
   end;
   if flag then
    begin
    Writeln('el codigo ingresado no es valido');
    flag:=false;
    end else flag:=true;
   end;
  flag:=false;
  While not flag do
  begin
   Writeln('b)ingrese el limite inferior de un rango T');
   Readln(T);
   case T of
    1:m:=1;
    10:m:=2;
    20:m:=3;
    30:m:=4;
    40:m:=5;
    50:m:=6;
    60:m:=7;
    70:m:=8;
    80:m:=9;
    90:m:=10;
    else flag:=true
   end;
   if (flag) or (R>T) then
    begin
    Writeln('el codigo ingresado no es valido');
    flag:=false;
    end else flag:=true;
   end;
   min:=0;
     for k:=i to m do
    min:=min+mat[i,1];
    nomprov:=Vreg[1].nombre;

     for j:=2 to N do
      begin
       aux:=0;
       for k:=i to m do
        aux:=aux+mat[i,j];
      if aux<min then
       begin
        min:=aux;
        nomprov:=Vreg[j].nombre;
       end;
      end;
  Writeln('la provincia con menos cantidad de inscriptos en el rango R es ',nomprov);
  end;

 var
  cont,i:byte;
  Vreg:Tvecr;
  N:byte;
  mat:Tmat;
  X:st2;
begin
  i:=10;
  cont:=0;
  lectura1(Vreg,N);
  lectura2(mat,Vreg,N);
 Writeln('ingrese un codigo de provincia');
 Readln(X);
 incisoa(Vreg,mat,N,X,i,cont);
 Writeln('nashe');
 incisob(Vreg,mat,N,X,cont);
 Readln();
end.

