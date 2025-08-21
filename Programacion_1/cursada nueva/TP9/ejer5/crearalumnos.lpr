program crearalumnos;
 type
   st4=string[4];
   TR=record
     mat:st4;
     Nmat:byte;
     Nfis:byte;
     Nquim:byte;
   end;
 FTR=file of TR;
   TR2=record
     mat:st4;
     quimins:char;
     fisins:char;
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
  Assign(arch,'ALUMNOS.TXT');
  Assign(arch2,'ALUMNOS.DAT');
  Assign(arch3,'INSCRIPTOS.TXT');
  Assign(arch4,'INSCRIPTOS.DAT');
  Reset(arch);
  Reset(arch2);
  While not eof(arch) do
   begin
     Readln(arch,aux.mat);
     Readln(arch,aux.Nmat);
     Readln(arch,aux.Nfis);
     Readln(arch,aux.Nquim);
     Write(arch2,aux);
   end;
  Readln();
 Close(arch);
 Close(arch2);
 //
  Reset(arch3);
  Reset(arch4);
  While not eof(arch3) do
   begin
     Readln(arch3,aux2.mat);
     Readln(arch3,aux2.quimins);
     Readln(arch3,aux2.fisins);
     Write(arch4,aux2);
   end;
  Readln();
 Close(arch3);
 Close(arch4);
 end.
