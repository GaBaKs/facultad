program crearb;
 type
 st6=string[6];
   st30=string[30];
   TR=record
     id:st6;
     genero:char;
     nombretema:st30;
     disp:char;
     cantmg:integer;
   end;
  FTR=file of TR;
  TR2=record
    id:st6;
    nombre:st30;
    cat:char;
Tvec=array[1..max] of st6;
 FTR2=file of TR2;
var
  arch:text;
  arch2:FTR;
  arch3:text;
  arch4:FTR2;
  aux:TR;
  aux2:TR2;
begin
  Assign(arch,'ARCHIVOTEMAS.TXT');
  Assign(arch2,'ARCHIVOTEMAS.DAT');
  Assign(arch3,'INTERPRETES.TXT');
  Assign(arch4,'INTERPRETES.DAT');
  Reset(arch);
  Rewrite(arch2);
  Reset(arch3);
  Rewrite(arch4);
  While not eof(arch) do
   begin
     Readln(arch,aux.id);
     Readln(arch,aux.genero);
     Readln(arch,aux.nombretema);
     Readln(arch,aux.disp);
     Readln(arch,aux.cantmg);
     Write(arch2,aux);
   end;
  While not eof(arch3) do
   begin
    Readln(arch3,aux2.id);
    Readln(arch3,aux2.nombre);
    Readln(arch3,aux2.cat);
    Write(arch4,aux2);
   end;

  Writeln('nase');
  Readln();
 end.
