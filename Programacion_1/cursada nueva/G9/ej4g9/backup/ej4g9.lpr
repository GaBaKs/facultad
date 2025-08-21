program ej4g9;
type
  ST4=string[4];
  TR=record
    cod:ST4;
    talle:char;
    color:byte;
    cant:integer;
    precio:real;
  end;
  TArchS = file of TR;


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
  aux.cod:='ZZZZ';
  write(archS,aux);
  close(arch);
  close(archS);
end;

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
                cantN:=cantN+1;
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

var
  archS:TArchS;

begin
  assign(archS, 'STOCK.DAT');
  cargaSTOCK(archS);
  lista(archS);

  readln;
end.

