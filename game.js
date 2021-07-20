<script>

function getOption() {
  var obj = document.getElementById("mySelect");
  var output = obj.options[obj.selectedIndex].text;
  var tex = "You picked ";
  document.getElementById("choice").innerHTML = tex.concat(output,".");
}
const choices = ["rock", "paper", "scissors"];

function computerTurn() {
var select = Math.floor(Math.random() * 3);
var tex2 = "The computer picked ";
document.getElementById("demo2").innerHTML = tex2.concat(choices[select],".");
}
</script>
