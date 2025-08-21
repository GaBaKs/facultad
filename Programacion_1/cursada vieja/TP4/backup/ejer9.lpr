program ejer9;
  function suma(n1,d1,n2,d2:integer):real;
  begin
    suma:=(n1/d1)+n2/d2;
   end;
  function producto(n1,d1,n2,d2:integer):real;
   begin
     producto:=(n1/d1)*(n2/d2);
   end;
var n1,d1,n2,d2 : integer;
begin
  Writeln('escriba n1');
  Readln(n1);
  Writeln('escriba d1');
  Readln(d1);
  Writeln('escriba n2');
  Readln(n2);
  Writeln('escriba d2');
  Readln(d2);
  Writeln('la suma es ',suma(n1,d1,n2,d2):8:2);
  Writeln('el producto es ',producto(n1,d1,n2,d2));
  Readln();
end.

