program ejer20;
 var
   arch:text;
   cont:byte;
   acumsuma:word;
   prom:real;
     lect:integer;
begin
 cont:=0;
 prom:=0;
 acumsuma:=0;
 assign (arch,'ejer20.TXT');
 reset(arch);
 Read(arch,lect);
 While not eof(arch) do
  begin
    while lect>=0 do
     Read(arch,lect);
    while lect<0 do
     begin
       Read(arch,lect);
       if lect>=0 then
          begin
               While lect>=0 do
                begin
                  cont:=cont+1;
                  acumsuma:=acumsuma+lect;
                 if lect=0 then
                    cont:=cont-1;
                  Read(arch,lect);
                end;
            prom:=acumsuma/cont;
            Write(prom:2:2,' ');
            cont:=0;
            acumsuma:=0;
          end;
     end;
  end;
 readln();
end.

