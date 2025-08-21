program ej6g9;
const
  MAX=50;
type
  ST4=string[4];
  ST10=string[10];
  TRE=record
    legajo:ST4;
    nom:ST10;
    ventas:integer;
    numFmax:ST4;
    max:real;
  end;
  TRV=record
    legajo:ST4;
    numF:ST4;
    importe:real;
  end;

  TArchE = file of TRE;
  TArchV = file of TRV;

  TV = array [1..MAX] of ST4;

procedure cargaEMPLEADOS (var archE:TArchE);
var
  arch:TEXT;
  aux:TRE;
begin
  assign(arch,'EMPLEADOS.TXT');
  reset(arch);
  reset(archE);
  while not eof (arch) do
    begin
      readln(arch, aux.legajo);
      readln(arch, aux.nom);
      readln(arch, aux.ventas);
      readln(arch, aux.numFmax);
      readln(arch, aux.max);
      write(archE,aux);
    end;
  close(arch);
  close(archE);
end;

procedure cargaVENTAS (var archV:TArchV);
var
  arch:TEXT;
  aux:TRV;
begin
  assign(arch,'VENTAS.TXT');
  reset(arch);
  reset(archV);
  while not eof (arch) do
    begin
      readln(arch,aux.legajo);
      readln(arch,aux.numF);
      readln(arch,aux.importe);
      write(archV,aux);
    end;
  aux.legajo:='zzzz';
  write(archV,aux);
  close(arch);
  close(archV);
end;

procedure cargaVec (var archE:TArchE; var legajos:TV; var n:byte);
var
  aux:TRE;
begin
  n:=0;
  reset(archE);
  while not eof (archE) do
    begin
      read(archE,aux);
      n:=n+1;
      legajos[n]:= aux.legajo;
    end;
  close(archE);
end;

procedure actualiza (var archE:TArchE; var archV:TArchV; legajos:TV; n:byte);
var
  auxE:TRE;
  auxV:TRV;
  legact:ST4;
  h:byte;
begin
  reset(archE);
  reset(archV);
  read(archV,auxV);
  h:=1;
  while not eof (archV) do
    begin
      legact:=auxV.legajo;
      while (h<=n) and (legajos[h]<>legact) do
        h:=h+1;
      seek(archE, h-1);
      read(archE, auxE);
      while (legact = auxV.legajo) do
        begin
          if (auxV.importe > auxE.max) then
            begin
              auxE.max:=auxV.importe;
              auxE.numFmax:=auxV.numF;
            end;
          read(archV,auxV);
        end;
       seek(archE, h-1);
       write(archE,auxE);
    end;
  close(archE);
  close(archV);
end;

procedure lista (var archE:TArchE);
var
  auxE:TRE;
begin
  reset(archE);
  while not eof (archE) do
    begin
      read(archE,auxE);
      writeln('Legajo: ', auxE.legajo, '. Comision: ', auxE.max*0.005:7:2);
    end;
  close(archE);
end;

var
  archE:TArchE;
  archV:TArchV;
  legajos:TV;
  n:byte;
begin
  assign(archE, 'EMPLEADOS.DAT');
  assign(archV, 'VENTAS.DAT');
  cargaEMPLEADOS(archE);
  cargaVENTAS(archV);
  cargaVec(archE,legajos,n);
  actualiza(archE,archV,legajos,n);
  lista(archE);

  readln;
end.

