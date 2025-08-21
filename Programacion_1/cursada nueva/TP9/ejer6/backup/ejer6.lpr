program ejer6;
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

 procedure enfrentamiento(var arch:FTR;var arch2: FTR2);
  var
   aux:TR;
   aux2:TR2;
   pos:byte;
  begin
   Reset(arch);
   Reset(arch2);

   Read(arch2,aux2);
  While (not eof(arch)) and (not eof(arch2)) do
   begin
     Read(arch,aux);
       While aux.legajo=aux2.legajo do
         begin
              aux.totfac:=aux.totfac+aux2.importe;
              if aux.impmayor<aux2.importe then
               begin
                 aux.impmayor:=aux2.importe;
                 aux.facmayor:=aux2.Nfac;
               end;
         if not eof(arch2) then
          begin
           Read(arch2,aux2);
           aux2.legajo:='0000';
          end;
         end;
        pos:=filepos(arch)-1;
        seek(arch,pos);
        Write(arch,aux);
   end;
close(arch);
close(arch2);
end;

procedure mostrar(var arch:FTR);
 var
  aux:TR;

 begin
  reset(arch);
  Writeln(' legajo             nombre                     totventas                Nfacturamayor         impmayor ');
  While not eof(arch) do
   begin
     read(arch,aux);
     Writeln(aux.legajo,'            ',aux.nomap,'                  ',aux.totfac:4:3,'                       ',aux.facmayor,'              ',aux.impmayor:4:3);
   end;
 Close(arch);
 end;
 var
  arch:FTR;
  arch2:FTR2;


begin
  Assign(arch,'ORIGINAL.DAT');
  Assign(arch2,'ACTUALIZAR.DAT');
  enfrentamiento(arch,arch2);
  mostrar(arch);
  Readln();
end.

