program ejer5;
 const
   max=50;
 type
   Tvec=array[1..max] of integer;

 procedure lectura(var vec:Tvec;var N:byte);
  var
    i:byte;
   begin
     Writeln('valores a ingresar');
     Readln(N);
     for i:=1 to N do
      begin
       Writeln('ingresa valor ',i);
       Readln(vec[i]);
      end;
   end;

function incisoa(vec:Tvec;N:byte):integer;
 begin
  if N=1 then
    incisoa:=vec[1]
  else
   incisoa:=vec[N]+incisoa(vec,N-1);
 end;

procedure incisob(vec:Tvec;N:byte);
 begin
  if N=1 then
   Write(vec[1])
  else
   begin
   incisob(vec,N-1);
  Write(vec[N],' ');
  end;
 end;

procedure incisoc(vec:Tvec;N:byte);
 begin
  Write(vec[N],' ');
  if N=2 then
   Write(vec[1])
  else
   incisoc(vec,N-1);
 end;

function incisod(vec:Tvec;N:byte):integer;
var
  max:integer;
 begin
  if N>0 then
   begin
   if incisod<vec[N] then
    begin
    incisod:=vec[N];
    end;
   end;
  if N>0 then
   incisod(vec,N-1);
 end;

function incisoe(vec:Tvec;N:byte):real;
 begin
  if N=1 then
   incisoe:=vec[N]
  else
   incisoe:=(vec[N]+incisoe(vec,N-1))/N;
 end;

 var
   vec:Tvec;
   N:byte;
begin
  lectura(vec,N);
  Writeln('inciso a: ',incisoa(vec,N));
  Write('inciso b: ');
  incisob(vec,N);
  Writeln('      inciso c: ');
  incisoc(vec,N);
  Writeln('     inciso d: ', incisod(vec,N));
  Writeln('     inciso e: ', incisoe(vec,N));
  Readln();
end.

