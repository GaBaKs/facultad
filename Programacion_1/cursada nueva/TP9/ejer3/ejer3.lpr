program ejer3;
const
  max=50;

 type
  st3=string[3];
  st15=string[15];
  Tvecex= array[1..max] of st3;
  TR=record
    cod:st3;
    desc:st15;
    prebase:real;
    precom:real;
  end;
  FTR= file of TR;
 TR2=record
   cod:st3;
   nrob:word;
   com:char;
  end;
 FTR2= file of TR2;
 procedure lecturacodigos (var vecex:Tvecex;var N:byte;var arch:FTR);
   var
    aux:TR;
   begin
    Reset(arch);
    N:=0;
    While not eof(arch) do
     begin
       N:=N+1;
       Read(arch,aux);
       vecex[N]:=aux.cod;
     end;
   end;
 procedure lista (vecex:Tvecex;N:byte;var arch2:FTR2;var arch:FTR);
  var
  aux:TR2;
  aux2:TR;
   codact:st3;
  contb,contc,contotalb,contotalc:byte;
  i:byte;
  monto:real;
  begin
   Reset(arch2);
   Reset(arch);
   Read(arch2,aux);
   contotalb:=0;
   contotalc:=0;
   Writeln('Excursion      Cantidad de boletos     Cantidad de comida     Monto');
   While not eof(arch2) do
    begin
         i:=1;
         contb:=0;
         contc:=0;
         codact:=aux.cod;
          While codact=aux.cod do
           begin
            contb:=contb+1;
            if aux.com='S' then
             contc:=contc+1;
            read(arch2,aux);
           end;
         While (i<=N) and  (vecex[i]<>codact) do
          i:=i+1;
         Seek(arch,i-1);
         read(arch,aux2);
         monto:=contb*aux2.prebase+contc*aux2.precom;
         contotalc:=contotalc+contc;
         contotalb:=contotalb+contb;
         Writeln(codact,'     ',contb,'        ',contc,'             ',monto:4:2);
    end;
   Close(arch);
   Close(arch2);
   Writeln('% de turistas que contrataron excursion con comida: ',((contotalc/contotalb)*100):3:2,'%');
  end;



  var
 vecex:Tvecex;
 N:byte;
 arch:FTR;
 arch2:FTR2;

begin
 Assign(arch,'EXCURSIONES.DAT');
 Assign(arch2,'BOLETERIA.DAT');
 lecturacodigos(vecex,N,arch);
 lista(vecex,N,arch2,arch);
 Readln();
end.

