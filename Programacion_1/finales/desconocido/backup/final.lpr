program final;


type
  st3=string[3];
  st8=string[8];
  st20=string[20];
  TR=record
    cod:st3;
    fecha:st8;
    cantent:word;
  end;
FTR=file of TR;
  TR2= record
    cod:st3;
    ciudad:st20;
    capmax:word;
    valor:real;
  end;
FTR2=file of TR2;
Tvec=array[1..max] of TR2;
procedure generarvector(var vec:Tvec;var i:byte;var arch2:FTR2 );
begin
  reset(arch2);
  i:=o;
  While not eof(arch2) do
   begin
     i:=i+1;
     read(arch2,vec[i]);
   end;
end;
 function busca(vec:Tvec;i:byte;aux:TR):byte;
 var
   j:byte;
 begin
      j:=1;
      While (aux.cod<>vec[j]) and (j<=i) do
          j:=j+1;
      busca:=j;
 end;

procedure listado(var arch:FTR;vec:Tvec;i:byte);
 var
   aux:TR;
   j:byte;
   nova:byte;
   imptot,promg:real;
   fecham:st8;
   recmax:real;
   entradasv:word;
   ocupacion:real;
 begin
   Reset(arch);
    imptot:=0;
    recmax:=-1;
   While not eof(arch) do
     begin
       promg:=0;
       entradasv:=0;
       Read(arch,aux);
       nova:=busca(vec,i,aux);
       Writeln('Nombre ciudad: ',vec[nova].ciudad);
       Writeln('     Fecha carrera      Entradas vendidas             % Ocupacion');
       While aux=vec[nova].cod do
        begin
         ocupacion:=aux.cantent/vec[nova].capmax;
         Writeln(aux.fecha,'         ',aux.cantent,'       ',ocupacion:3:2);
        end;
     end;
 end;



begin
end.

