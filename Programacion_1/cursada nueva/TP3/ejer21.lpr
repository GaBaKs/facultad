program ejer21;
 var
  arch:text;
  contsub,contel,contelmax,maxsub:byte;
  max,aux:integer;
begin
 Assign(arch,'ejer21.TXT');
 Reset(arch);
 contsub:=1;
 contel:=1;
 contelmax:=0;
 Read(arch,aux);
aa max:=aux;
  while (max<>0) or (aux<>0) do
   begin
    aux:=max;
    while aux<>0 do
     begin
      read(arch,aux);
      if aux<>0 then
       contel:=contel+1;
      if max<aux then
       max:=aux;
     end;
    if aux=0 then
      begin
       Writeln('subconjunto: ',contsub, '. Maximo: ',max);
       if contelmax<contel then
        begin
         maxsub:=contsub;
         contelmax:=contel;
        end;
       contsub:=contsub+1;
       contel:=1;
       read(arch,max);
      end;
   end;
 Writeln('el subconjunto con mas elementos es el ',maxsub);
 readln();
end.
