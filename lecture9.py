<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: #b0e4fe;
}

h1 {
    font-size: 50px;
    color: WHITE;
    font-family: "Showcard Gothic";
    text-align: center;
}
h2 {
   text-align:   end;
   font-family: "Algerian";
}
p { 
    color: ORANGE;
    font-family: "Lucida Calligraphy";
    font-size: 25px;
}
p1 {
     color: RED;
     text-align: center;
}
</style>
</head>
<body>

<h1>SET 2015</h1>
<h2>NAMES</h2>
<p>ONIMAGO SOLIAT</p>
<p>OYELEKE OYELOLA</p>
<p>ODANIKE GLORIA</p>
<p>AKPOGHENEBOR EGUONO</p>
<p>BAKI ENIOLA</p>
<p>PHILIP NWACHUKWU</p>
<p1>Just playing around</p1>
<p id="demo">Click the button below to change the color of this paragraph.</p>

<script>
function myFunction() {
    var x = document.getElementById("demo");
    x.style.fontSize = "25px"; 
    x.style.color = "red"; 
}
</script>

<button onclick="myFunction()">Click!</button>
</body>
