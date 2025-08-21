program ejer5;
 const
   ph: 1000 , pm: 1200 ; IVA: 0.21
 var
  talleh: char
  tipcam,canth,cantm,cantSh,cantXM,resth,restm,contcamhtotal,contcammtotal:integer
  importe:real;
begin
  repeat
   Writeln('colocar 1 para camisas de hombre y 2 para camisas de mujer)
   Readln(tipcam)
   case tipcam of
   1 : Writeln('cuantas talle S?')
       Readln(cantSh)
       Writeln('cuantas talle M?')
       Readln(resth)
       contcamhtotal:=contcamhtotal+resth
       Writeln('cuantas talle L?')
       Readln(resth)
       contcamhtotal:=contcamhtotal+resth
       Writeln('cuantas talle X?')
       Readln(resth)
       contcamhtotal:=contcamhtotal+resth

   2:  Writeln('cuantas talle S?')
       Readln(restm)

       Writeln('cuantas talle M?')
       Readln(restm)
       contcammtotal:=contcamhtotal+restm
       Writeln('cuantas talle L?')
       Readln(restm)
       contcammtotal:=contcamhtotal+restm
       Writeln('cuantas talle X?')
       Readln(cantXM)

 if canth <>0 then
  Writeln('que talle
   Until canth=0
end.
                                  // preguntar si quiere de hombre y despues ofrecer cuantas de  cada talle, todo en distitnas variables
