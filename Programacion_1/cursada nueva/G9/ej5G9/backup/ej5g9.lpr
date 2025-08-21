program ej5g9;
const
  MAX=50;

type
  ST4=string[4];
  TRA=record
    mat:ST4;
    nM,nF,nQ:integer;
  end;
  TRI=record
    mat:ST4;
    Q,F:char;
  end;

  TArchA = file of TRA;
  TArchI = file of TRI;

  TV = array [1..MAX] of ST4;

procedure cargaALUMNOS (var archA:TArchA);
var
  arch:TEXT;
  aux:TRA;
begin
  assign(arch, 'ALUMNOS.TXT');
  reset(arch);
  reset(archA);
  while not eof(arch) do
    begin
      readln(arch, aux.mat);
      readln(arch, aux.nM);
      readln(arch, aux.nF);
      readln(arch, aux.nQ);
      write(archA, aux);
    end;
  close(arch);
  close(archA);
end;

procedure cargaVec (var archA:TArchA; var matriculas:TV; var n:byte);
var
  aux:TRA;
begin
  n:=0;
  reset(archA);
  while not eof (archA) do
    begin
      read(archA,aux);
      n:=n+1;
      matriculas[n]:=aux.mat;
    end;
  close(archA);
end;

procedure cargaINSCRIPTOS (var archI:TArchI);
var
  arch:TEXT;
  aux:TRI;
begin
  assign(arch,'INSCRIPTOS.TXT');
  reset(arch);
  reset(archI);
  while not eof (arch) do
    begin
      readln(arch,aux.mat);
      readln(arch,aux.Q);
      readln(arch,aux.F);
      write(archI, aux);
    end;
  close(arch);
  close(archI);
end;

procedure procesa (var archA:TArchA;var archI:TArchI; matriculas:TV; n:byte);
var
  auxA:TRA;
  auxI:TRI;
  h:byte;
begin
  reset(archA);
  reset(archI);
  while not eof (archI) do
    begin
      read(archI, auxI);
      h:=1;
      while (h<=n) and (matriculas[h]<>auxI.mat) do
        h:=h+1;
      seek(archA,h-1);
      read(archA,auxA);
      if ((auxI.Q = '1') and (auxA.nQ<4)) or ((auxI.F = '1') and ((auxA.nM<4) or (auxA.nF<4))) then
        writeln('Rechazado: ', auxI.mat);
    end;
  close(archA);
  close(archI);
end;

var
  archA: TArchA;
  archI: TArchI;
  matriculas:TV;
  n:byte;
begin
  assign(archA, 'ALUMNOS.DAT');
  assign(archI, 'INSCRIPTOS.DAT');
  cargaALUMNOS(archA);
  cargaVec(archA,matriculas,n);
  cargaINCRIPTOS(archI);
  procesa(archA, archI, matriculas,n);


  readln;
end.

