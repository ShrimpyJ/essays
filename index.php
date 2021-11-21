<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Random Youtube Video Game Essay Title Generator</title>
</head>

<body>
  <?PHP
  echo shell_exec("python3 essay.py");
  ?>
</body>

<script>
function readFile()
{
    console.log("Hello world")
    fetch('genres.txt')
      .then(response => response.text())
      .then(text => console.log(text))
}
</script>

</html>
