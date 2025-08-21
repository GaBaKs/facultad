program crearb;

type
    ST5 = string[5];
    TR = record
      codP: ST5;
      peso, monto: real;
      codD: byte;
    end;
    TArch = file of TR;


var
   arch: TArch;
   archT: TEXT;
   aux: TR;

begin
  assign(archT, 'PAQUETES.TXT');
  reset(archT);
  assign(arch, 'PAQUETES.DAT');
  reset(arch);
  while not eof(archT) do
    begin
      readln(archT, aux.codP);
      readln(archT, aux.peso);
      readln(archT, aux.codD);
      readln(archT, aux.monto);
      write(arch, aux);
    end;
  //seek(arch, 0);
  //read(arch, aux);
  //writeln(aux.codD);

  close(arch);
  close(archT);

  readln;
end.
