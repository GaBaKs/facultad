program creabinario;

type
    ST15 = string[15];
    TR = record
      desc: ST15;
      codD: byte;
    end;
    TArch = file of TR;


var
   arch: TArch;
   archT: TEXT;
   aux: TR;

begin
  assign(archT, 'DESTINO.TXT');
  reset(archT);
  assign(arch, 'DESTINO.DAT');
  reset(arch);
  while not eof(archT) do
    begin
      readln(archT, aux.codD);
      readln(archT, aux.desc);
      write(arch, aux);
    end;
  //seek(arch, 0);
  //read(arch, aux);
  //writeln(aux.codD);

  close(arch);
  close(archT);

  readln;
end.
