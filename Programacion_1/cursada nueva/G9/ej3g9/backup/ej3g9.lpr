program ej3g9;
const
  MAX=50;

type
  ST3=string[3];
  ST15=string[15];
  TRE=record
    cod:ST3;
    desc:ST15;
    precioB, precioC:real;
  end;
  TRB=record
    cod:ST3;
    Nbol:byte;
    comida:char;
  end;
  TArchE = file of TRE;
  TArchB = file of TRB;

  TV = array [1..MAX] of ST3;

procedure cargaEXCURSIONES (var archE: TArchE);
var
  arch:TEXT;
  aux:TRE;
begin
  reset(archE);
  assign(arch, 'EXCURSIONES.TXT');
  reset(arch);
  while not eof(arch) do
    begin
      readln(arch,aux.cod);
      readln(arch,aux.desc);
      readln(arch,aux.precioB);
      readln(arch,aux.precioC);
      write(archE, aux);
    end;
  close(arch);
  close(archE);
end;

procedure cargaVec (var archE: TArchE; var excursiones:TV; var n:byte);
var
  aux:TRE;
begin
  reset(archE);
  n:= 0;
  while not eof(archE) do
    begin
      read(archE, aux);
      n:=n+1;
      excursiones[n]:= aux.cod;
    end;
  close(archE);
end;

procedure cargaBOLETERIA (var archB: TArchB);
var
  arch:TEXT;
  aux:TRB;
begin
  reset(archB);
  assign(arch, 'BOLETERIA.TXT');
  reset(arch);
  while not eof (arch) do
    begin
      readln(arch, aux.cod);
      readln(arch, aux.Nbol);
      readln(arch, aux.comida);
      write(archB, aux);
    end;
  aux.cod:='ZZZ';
  write(archB, aux);
  close(arch);
  close(archB);
end;

procedure Lista (var archE: TArchE; var archB: TArchB; excursiones:TV; n:byte);
var
  auxB:TRB;
  auxE:TRE;
  codact:ST3;
  contB,contC:integer;
  monto:real;
  h:byte;
begin
  reset(archE);
  reset(archB);
  writeln('Excursion      cantidad de boletos     cantirdad de comida    monto total') ;
  read(archB, auxB);
  while not eof (archB) do
    begin
      codact:=auxB.cod;
      contB:=0;
      contC:=0;
      while (auxB.cod = codact) do
        begin
          contB:= contB+1;
          if (auxB.comida = 'S') then
            contC:=contC+1;
          read(archB, auxB);
        end;
      h:=1;
      while (h<=n) and (excursiones[h]<>codact) do
        h:=h+1;
      seek(archE, h-1);
      read(archE, auxE);
      monto:= contB * auxE.precioB + contC * auxE.precioC;
      write(auxE.desc, contB:7, contC:7, monto:9:2);
    end;
end;

var
  archE: TArchE;
  archB: TArchB;
  excursiones: TV;
  n:byte;

begin
  assign(archE, 'EXCURSIONES.DAT');
  assign(archB, 'BOLETERIA.DAT');
  cargaEXCURSIONES(archE);
  cargaVec(archE, excursiones, n);
  cargaBOLETERIA(archB);
  Lista(archE,archB,excursiones,n);

  readln;
end.

