program crearb;
 const
  max=30;
 type
  st3=string[3];
  st4=string[4];
  st15=string[15];
  st8=string[8];
  TR=record
    leg:st4;
    nombre:st15;
    sueldo:real;
  end;
 FTR=file of Temp;
 TR2=record
   leg:st4;
   fecha:st8;
   canth:byte;
   codp:st3
 end;
FTR2=file of TR2;
TR3=record
  codigo:st3;
  desc:st15;
  valh:real;
  end;
FTR3=file of TR3;
var
  arch:text;
  arch2:FTR;
  arch3:text;
  arch4:FTR2;
  arch5:text;
  arch6:FTR3;
  aux:TR;
  aux2:TR2;
  aux3:TR3;
begin
  Assign(arch,'EMPLEADOS.TXT');
  Assign(arch2,'EMPLEADOS.DAT');
  Assign(arch3,'HORASTRABAJO.TXT');
  Assign(arch4,'HORASTRABAJO.DAT');
  Assign(arch5,'POZOPETROLEO.TXT');
  Assign(arch6,'POZOPETROLEO.DAT');
  Reset(arch);
  Rewrite(arch2);
  Reset(arch3);
  Rewrite(arch4);
  reset(arch5);
  rewrite(arch6);
  While not eof(arch) do
   begin
     Readln(arch,aux.leg);
     Readln(arch,aux.nombre);
     Readln(arch,aux.sueldo);
     Write(arch2,aux);
   end;
  While not eof(arch3) do
   begin
    Readln(arch3,aux2.leg);
    Readln(arch3,aux2.fecha);
    Readln(arch3,aux2.canth);
    Readln(arch3,aux2.codp);
    Write(arch4,aux2);
   end;
  While not eof(arch5) do
    begin
     Readln(arch5,aux3.codigo);
     Readln(arch5,aux3.desc);
     Readln(arch5,aux3.valh);
     Write(arch6,aux3);
    end;
  Writeln('nase');
  Readln();
 end.
