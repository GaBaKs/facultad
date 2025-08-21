program crearb;
  type
     st5=string[5];
     st8=string[8];
     st20=string[20];
     TR=record
       esc:st5;
       nom:st20;
       tiempo:word;
     end;
    FTR= file of TR;
    TR2=record
      esc:st5;
      cantot:byte;
      mejort:word;
    end;
  FTR2=file of TR2;
  TR3=record
    nombremax:st20;
    esc:st5;
    tiempo:word;
    end;
var
  arch:text;
  arch2:FTR;
  arch3:text;
  arch4:FTR2;
  aux:TR;
  aux2:TR2;
begin
  Assign(arch,'CARRERAS.TXT');
  Assign(arch2,'CARRERAS.DAT');
  Assign(arch3,'HISTORICO.TXT');
  Assign(arch4,'HISTORICO.DAT');
  Reset(arch);
  Rewrite(arch2);
  Reset(arch3);
  Rewrite(arch4);
  While not eof(arch) do
   begin
     Readln(arch,aux.esc);
     Readln(arch,aux.nom);
     Readln(arch,aux.tiempo);
     Write(arch2,aux);
   end;
  While not eof(arch3) do
   begin
    Readln(arch3,aux2.esc);
    Readln(arch3,aux2.cantot);
    Readln(arch3,aux2.mejort);
    Write(arch4,aux2);
   end;

  Writeln('nase');
  Readln();
 end.
