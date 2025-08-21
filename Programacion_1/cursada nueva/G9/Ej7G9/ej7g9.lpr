program ej7g9;
const
  ZON=10;
type
  ST4=string[4];
  ST3=string[3];
  TRS=record
    codcine:ST4;
    zona:byte;
    capacidad:integer;
  end;
  TRP=record
    codcine:ST4;
    codpel:ST3;
    loc:integer;
  end;

  TarchS = file of TRS;
  TarchP = file of TRP;

  TVZ = array [1..ZON] of integer;

procedure cargaSALAS(var archS:TarchS);
var
  arch:TEXT;
  aux:TRS;
begin
  assign(arch, 'SALAS.TXT');
  reset(arch);
  reset(archS);
  while not eof (arch) do
    begin
      readln(arch,aux.codcine);
      readln(arch,aux.zona);
      readln(arch,aux.capacidad);
      write(archS,aux);
    end;
  close(arch);
  close(archS);
end;

procedure cargaPROYECCIONES(var archP:TarchP);
var
  arch:TEXT;
  aux:TRP;
begin
  assign(arch, 'PROYECCIONES.TXT');
  reset(arch);
  reset(archP);
  while not eof (arch) do
    begin
      readln(arch,aux.codcine);
      readln(arch,aux.codpel);
      readln(arch,aux.loc);
      write(archP, aux);
    end;
  aux.codcine:='ZZZZ';
  write(archP,aux);
  close(arch);
  close(archP);
end;

procedure inicializaZonas (var zonas:TVZ);
var
  i:byte;
begin
  for i:=1 to ZON do
      zonas[i]:=0;
end;

procedure lista1 (var archP:TarchP; var archS:TarchS; var zonas:TVZ);
var
  auxP:TRP;
  auxS:TRS;
  cineact:ST4;
  pelact:ST3;
  contPel,contFun,NoPel:byte;
  totLoc:integer;
begin
  reset(archP);
  reset(archS);
  NoPel:=0;
  writeln('Cine            cant.Peliculas             cant.funciones               Tot Loc.vendidas            %Ocup prom');
  read(archP, auxP);
  while not eof (archP) do
    begin
      cineact:=auxP.codcine;
      contPel:=0;
      contFun:=0;
      totLoc:=0;
      while (auxP.codcine = cineact) do
        begin
          pelact:=auxP.codpel;
          contPel:=contPel+1;
          while (auxP.codpel = pelact) and (auxP.codcine = cineact) do
            begin
              contFun:=contFun+1;
              totLoc:=totLoc+auxP.loc;
              read(archP, auxP);
            end;
        end;
      read(archS, auxS);
      while(auxS.codcine <> cineact) do
        begin
        read(archS,auxS);
        NoPel:=NoPel+1;
        end;
      zonas[auxS.zona]:=zonas[auxS.zona]+totLoc;
      writeln(cineact, contPel:12, contFun:12, totLoc:12, 100*totLoc/(auxS.capacidad*contFun):10:2);
    end;
  while not eof (archS) do
    begin
      read(archS,auxS);
      NoPel:=NoPel+1;
    end;
  writeln('Cantidad de cines que no proyectaron ninguna pelicula: ', NoPel);
end;

procedure lista2 (zonas:TVZ);
var
   i:byte;
begin
  writeln('Total de localidades vendidas por zona:');
  for i:=1 to ZON do
        writeln('Zona ',i,': ',zonas[i]);
end;

var
  archS:TarchS;
  archP:TarchP;
  zonas:TVZ;

begin
  assign(archS, 'SALAS.DAT');
  assign(archP, 'PROYECCIONES.DAT');
  cargaSALAS(archS);
  cargaPROYECCIONES(archP);
  inicializaZonas(zonas);
  lista1(archP,archS,zonas);
  lista2(zonas);

  readln;
end.

