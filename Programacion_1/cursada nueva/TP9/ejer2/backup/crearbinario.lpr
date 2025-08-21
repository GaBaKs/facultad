program crearbinario;

type
    ST5 = string[5];
    ST10= string[10];
    TR = record
      numt: st5;
      nombre: st10;
      tope,gasto:real;
    end;
    TArch = file of TR;


var
   arch: TArch;
   archT: TEXT;
   aux: TR;

begin
  assign(archT, 'TARJETAS.TXT');
  reset(archT);
  assign(arch, 'TARJETAS.DAT');
  reset(arch);
  while not eof(archT) do
    begin
      readln(archT, aux.numt);
      readln(archT, aux.nombre);
      readln(archT, aux.tope);
      readln(archT, aux.gasto);
      write(arch, aux);
    end;
  //seek(arch, 0);
  //read(arch, aux);
  //writeln(aux.codD);

  close(arch);
  close(archT);

  readln;
end.
