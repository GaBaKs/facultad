program ej8g9;
const
  max=50;
type
  ST4=string[4];
  ST6=string[6];
  TR=record
    cod:ST4;
    talle:char;
    color:char;
    cant:integer;
    precio:real;
  end;
  TRP=record
    cod:ST4;
    talle:char;
    color:char;
    cant:integer;
  end;

  TArchP = file of TRP;
  TArchS = file of TR;

  TV = array [1..MAX] of  ST6;


procedure cargaSTOCK (var archS:TArchS);
var
  arch:TEXT;
  aux:TR;
begin
  assign(arch,'STOCK.TXT');
  reset(arch);
  reset(archS);
  while not eof(arch) do
    begin
      readln(arch,aux.cod);
      readln(arch,aux.talle);
      readln(arch,aux.color);
      readln(arch,aux.cant);
      readln(arch,aux.precio);
      write(archS, aux);
    end;
  close(arch);
  close(archS);
end;


procedure cargaPEDIDO (var archP:TArchP);
var
  arch:TEXT;
  aux:TRP;
begin
  assign(arch,'PEDIDO.TXT');
  reset(arch);
  reset(archP);
  while not eof (arch) do
    begin
      readln(arch,aux.cod);
      readln(arch,aux.talle);
      readln(arch,aux.color);
      readln(arch,aux.cant);
      write(archP,aux);
    end;
  close(arch);
  close(archP);
end;

procedure cargaVec (var archS:TArchS; var productos:TV; var n:byte);
var
  aux:TR;

begin
  reset(archS);
  n:=0;
  while not eof (archS) do
    begin
      read(archS, aux);
      n:=n+1;
      productos[n]:= aux.cod+aux.talle+aux.color;
    end;
  close(archS);
end;

procedure actualiza (var archS:TArchS; var archP:TArchP; productos:TV; n:byte);
var
  auxS:TR;
  auxP:TRP;
  h:byte;
  busca:ST6;
begin
  reset(archS);
  reset(archP);
  h:=1;
  while not eof (archP) do
    begin
      read(archP,auxP);
      busca:=auxP.cod+auxP.talle+auxP.color;
      while (h <= n) and (busca <> productos [h]) do
        h:=h+1;
      seek(archS,h-1);
      read(archS,auxS);
      if (auxS.cant <= auxP.cant) then
        begin
          auxS.cant:=auxS.cant-auxP.cant;
          seek(archS,h-1);
          write(archS,auxS);
        end
      else
        begin
          writeln('Producto insuficiente: ', busca, ' (Faltante: ', auxP.cant-auxS.cant,')');
          auxS.cant:=0;
          seek(archS,h-1);
          write(archS,auxS);
        end;
    end;
  close(archS);
  close(archP);
end;

{
procedure lista (var archS:TArchS);
var
  aux:TR;
  codact:ST4;
  talleact:char;
  cantT,TOTAL,cantN:integer;
  costoact:real;
begin
  reset(archS);
  writeln('Stock de Prendas');
  read(archS, aux);
  TOTAL:=0;
  cantN:=0;
  while not eof (archS) do
    begin
      codact:=aux.cod;
      writeln('Codigo: ', codact);
      writeln('   Talle         Cantidad         Precio  ');
      while (aux.cod = codact) do
        begin
          talleact:=aux.talle;
          costoact:=aux.precio;
          cantT:=0;
          while (aux.talle = talleact) and (aux.cod = codact) do
            begin
              cantT:=cantT+aux.cant;
              if (aux.color = 1) then
                cantN:=cantN+aux.cant;
              read(archS,aux);
            end;
          TOTAL:=TOTAL+cantT;
          writeln(talleact, cantT:7, costoact:9:2);
        end;
    end;
  writeln('Cant total: ', TOTAL);
  if (TOTAL <> 0) then
    writeln('Porcentaje prendas negras: ', 100*cantN/TOTAL:8:2);
end;
 }


var
  archS:TArchS;
  archP:TArchP;
  productos:TV;
  n:byte;

begin
  assign(archS, 'STOCK.DAT');
  assign(archP,'PEDIDO.DAT');
  cargaSTOCK(archS);
  cargaPEDIDO(archP);
  cargaVec(archS,productos,n);
  actualiza(archS,archP,productos,n);

  readln;
end.

