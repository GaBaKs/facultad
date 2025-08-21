program ejer12;
procedure fibo(cota:integer);
var
   post:integer;
   ant:integer;
   aux:integer;
begin
  Writeln('1');
  Writeln('1');
  ant:=1;
  post:=1;
  aux:=0;
  repeat
  aux:=ant+post;
  ant:=post;
  post:=aux;
  Writeln(aux)
  until post>cota;

 end;
 var cota:integer; n:char;
begin
  While n<>'F' do
  begin
   repeat
   Writeln('escriba la cota a superar');
   Readln(cota);
   until cota>=1;
   fibo(cota);
   Writeln('desea continuar?(F para finalizar, cualquier otro boton para continuar)');
   Readln(n);
  end;
end.

