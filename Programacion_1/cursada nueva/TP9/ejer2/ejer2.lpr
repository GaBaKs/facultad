program ejer2;
const
  max=100;
 type
  st5=string[5];
  st10= string[10];
    TR = record
      numt: st5;
      nombre: st10;
      tope,gasto:real;
    end;
    TArch = file of TR;
    Tvec= array[1..max] of record
      numt:st5;
      tope:real;
      gasto:real;
      end;
   TR2= record
     numt:st5;
    monto:real;
    codop:byte;
   end;
   Tarch2= file of TR2;

  procedure lecturabin(var vec: Tvec;var N:byte);
    var
     aux: TR;
     arch:Tarch;
    begin
    N:=0;
     Assign(arch,'TARJETAS.DAT');
     reset(arch);
     While not eof(arch) do
      begin
       N:=N+1;
       read(arch,aux);
       vec[N].numt:=aux.numt;
       vec[N].tope:=aux.tope;
       vec[N].gasto:=aux.gasto;
      end;
  end;
 function busqueda(vec: Tvec;N:byte;aux:TR2):byte;
     var
      i: byte;
    begin
     i:=1;
       While (i<=N) and (vec[i].numt<>aux.numt) do
        begin
          i:=i+1;
        end;
       busqueda:=i;
     end;



 procedure lecturacompras(vec: Tvec;N:byte);
  var
    arch:text;
    arch2: Tarch2;
    aux: TR2;
    i:byte;
   begin
     Assign(arch,'DATOS.TXT');
     Reset(arch);
     Assign(arch2,'RECHAZADOS.DAT');
     Reset(arch2);
     Seek(arch2,0);
     While not eof(arch) do
      begin
       Readln(arch,aux.numt);
       Readln(arch,aux.monto);
       Readln(arch,aux.codop);
       i:=busqueda(vec,N,aux);
       vec[i].gasto:=vec[i].gasto+aux.monto;
       if vec[i].gasto>vec[i].tope then
        Write(arch2,aux);
      end;
   end;
 var
   vec: Tvec;
   N:byte;
begin
  lecturabin(vec,N);
  lecturacompras(vec,N);
  Readln();
end.

