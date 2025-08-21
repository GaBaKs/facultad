program final;
  const
    max=30;

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
  procedure listado(var arch:FTR;var arch2:FTR2;var arch3:FTR2);
    var
      aux:TR;
      aux2:TR2;
    tiempo:word;
    cantcar:byte;
    mejor:TR3;
   begin
    Reset(arch);
    reset(arch2);
    rewrite(arch3);
    Read(arch,aux);
    read(arch2,aux2);
    mejor.tiempo:=30000;
     While (not eof(arch)) and (not eof(arch2)) do
       begin
        if aux.esc=aux2.esc then
         begin
          tiempo:=0;
          cantcar:=0;
          While aux.esc=aux2.esc do
           begin
            aux2.cantot:=aux2.cantot+1;
            cantcar:=cantcar+1;
            tiempo:=tiempo+aux.tiempo;
            if aux.tiempo<mejor.tiempo then
              begin
               mejor.tiempo:=aux.tiempo;
               mejor.nombremax:=aux.nom;
               mejor.esc:=aux.esc;
              end;
            read(arch,aux);
           end;
          tiempo:=tiempo div cantcar;
          if tiempo<aux2.mejort then
            aux2.mejort:=tiempo;
          write(arch3,aux2);
          read(arch2,aux2);
          end
         else
           if aux.esc>aux2.esc then
            begin
             if aux2.cantot>0 then
             Writeln(aux2.esc,' no gano ninguna carrera este año pero si el anterior, terribles bots');
             write(arch3,aux2);
             read(arch2,aux2);
            end;
        end;
    Writeln(mejor.nombremax,' de la escuderia ',mejor.esc,' tuvo el mejor tiempo en el ultimo año de ',mejor.tiempo);

    Close(arch);
    Close(arch2);
    Close(arch3);
    erase(arch2);
    rename(arch3,'HISTORICO.DAT');
    Writeln('Archivo actualizado');
    reset(arch3);
    while not eof (arch3) do
     begin
      read(arch3,aux2);
      Writeln('escuderia: ',aux2.esc);
      Writeln('cantotoal de carreras: ',aux2.cantot);
      Writeln('mejor tiempo: ',aux2.mejort);
     end;
   end;
  var
   arch:FTR;
   arch2:FTR2;
   arch3:FTR2;
begin
 Assign(arch,'CARRERAS.DAT');
 Assign(arch2,'HISTORICO.DAT');
 Assign(arch3,'tmp.dat');
 listado(arch,arch2);
 readln();
end.

