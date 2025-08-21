program crearb;
 type
   st4=string[4];
   st30=string[30];
   TR=record
     legajo:st4;
     nomap:st30;
     totfac:real;
     facmayor:word;
     impmayor:real;
   end;
 FTR=file of TR;
   TR2=record
     legajo:st4;
     Nfac:word;
     importe:real;
   end;
 FTR2=file of TR2;
var
  arch:text;
  arch2:FTR;
  arch3:text;
  arch4:FTR2;
  aux:TR;
  aux2:TR2;
begin
  Assign(arch,'ORIGINAL.TXT');
  Assign(arch2,'ORIGINAL.DAT');
  Assign(arch3,'ACTUALIZAR.TXT');
  Assign(arch4,'ACTUALIZAR.DAT');
  Reset(arch);
  Rewrite(arch2);
  Reset(arch3);
  Rewrite(arch4);
  While not eof(arch) do
   begin
     Readln(arch,aux.legajo);
     Readln(arch,aux.nomap);
     Readln(arch,aux.totfac);
     Readln(arch,aux.facmayor);
     Readln(arch,aux.impmayor);
     Write(arch2,aux);
   end;
  While not eof(arch3) do
   begin
    Readln(arch3,aux2.legajo);
    Readln(arch3,aux2.Nfac);
    Readln(arch3,aux2.importe);
    Write(arch4,aux2);
   end;

  Writeln('nase');
  Readln();
 end.
