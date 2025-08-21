program ejer2;
 function funcion(t:word):word;
   begin
    if t=0 then
     funcion:=1
   else if Odd(t) then
    funcion:=funcion(t-1)
    else funcion:=1+funcion(t-1);
   end;
 var
   t:word;
begin
 Writeln(funcion(3));
 readln();
end.

