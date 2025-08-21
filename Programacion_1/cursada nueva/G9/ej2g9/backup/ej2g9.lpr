program ej2g9;
const
  MAX = 50;
type
  ST4=string[4];
  ST10=string[10];
  TR1=record
    num: ST4;
    nombre: ST10;
    tope,gasto: real;
    end;
  TR2=record
    num:ST4;
    cod:ST4;
    monto:real;
  end;

  TArch1 = file of TR1;
  TArch2 = file of TR2;

  TV = array [1..MAX] of ST4;



procedure cargaTARJETAS (var archT:TArch1);
var
  aux:TR1;
  arch:TEXT;
begin
  assign(arch, 'TARJETAS.TXT');
  reset(arch);
  reset(archT);
  while not eof(arch) do
    begin
      readln(arch, aux.num);
      readln(arch, aux.nombre);
      readln(arch, aux.tope);
      readln(arch, aux.gasto);
      write(archT, aux);
    end;
  close(arch);
  close(archT);
end;

procedure cargaVec(var archT:TARch1; var tarjetas:TV; n:byte);
var
  aux:TR1;
begin
  n:=0;
  reset(archT);
  while not eof(archT) do
    begin
      read(archT,aux);
      n:=n+1;
      tarjetas[n]:=aux.num;
    end;
  close(archT);
end;

procedure procesa (var archT:TArch1; var archR:TArch2; tarjetas:TV; n:byte);
var
  arch:TEXT;
  aux:TR2;
  auxT:TR1;
  h:byte;
begin
  assign(arch, 'Ingresos.txt');
  reset(arch);
  reset(archT);
  reset(archR);
  while not eof (arch) do
    begin
      readln(arch, aux.num);
      readln(arch, aux.monto);
      readln(arch, aux.cod);
      h:=1;
      while (h<=n) and (tarjetas[h]<>aux.num) do
        h:=h+1;
      seek(archT, h-1);
      read(archT, auxT);
      if (auxT.gasto + aux.monto > auxT.tope) then
        write(archR,aux)
      else
        begin
          seek(archT, h-1);
          auxT.gasto := auxT.gasto + aux.monto;
          write(archT, auxT);
        end;
    end;

  seek(archR, 0);
  while not eof (archR) do
    begin
      read(archR, aux);
      writeln(aux.cod);
    end;

  close(arch);
  close(archT);
  close(archR);
end;

var
  archT:TArch1;
  archR:TArch2;
  archI:TEXT;
  tarjetas:TV;
  n:byte;

begin
  assign(archT, 'TARJETAS.DAT');
  assign(archR, 'RECHAZADOS.DAT');
  cargaTARJETAS(archT);
  cargaVec(archT, tarjetas, n);
  procesa(archT, archR, tarjetas,n);

  readln;
end.

