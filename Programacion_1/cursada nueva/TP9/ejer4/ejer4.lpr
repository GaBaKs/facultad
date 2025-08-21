program ejer4;
 type
   st4=string[4];
   TR=record
     codart:st4;
     talle:char;
     color:byte;
     cantp:byte;
     precio:real;
   end;
 FTR=file of TR;
 procedure lista(var arch:FTR);
  var
   aux:TR;
   cent1:st4;
   cent2:char;
  cant,contn:byte;
  cantotal:word;
  precioact:real;
  begin
   Reset(arch);
   Writeln('             Stock de prendas');
   Read(arch,aux);
   contn:=0;
   cantotal:=0;
  While not eof(arch) do
   begin
    Writeln('Codigo: ',aux.codart);
    Writeln('Talle         Cantidad          Precio Costo');
    cent1:=aux.codart;
    While cent1=aux.codart do
     begin
     cant:=0;
     precioact:=0;
      cent2:=aux.talle;
      While (cent2=aux.talle) and (cent1=aux.codart) do
       begin
        cant:=cant+aux.cantp;
        precioact:=precioact+aux.cantp*aux.precio;
        cantotal:=cantotal+aux.cantp;
        if aux.color=1 then
         contn:=contn+aux.cantp;
        Read(arch,aux);
       end;
    Writeln(' ',cent2,'               ',cant,'               ',precioact:8:2);
     end;
   end;
   Writeln('Cantidad total: ',cantotal);
   Writeln('Porcentaje de prendas negras: ',((contn/cantotal)*100):3:2,'%');
end;

  var
  arch:FTR;

 begin
  Assign(arch,'STOCK.DAT');
  lista(arch);
  Readln();
end.

