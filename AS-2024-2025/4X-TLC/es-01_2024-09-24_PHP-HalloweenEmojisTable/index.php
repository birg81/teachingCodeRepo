<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" type="image/png" href="https://em-content.zobj.net/source/twitter/408/jack-o-lantern_1f383.png" />
<title>Halloween Emojis Table</title>
</head>
<body>
<?php
$ROWS = 10;
$COLS = 10;
// emojis List - Halloween Theme
$emojisList = [
	0x1f52e,	0x1f47b,	0x1f9db,	0x1f9df,	0x1f315,
	0x1f9d9,	0x1f480,	0x1f578,	0x1f577,	0x1f987,
	0x1fa93,	0x1fa7b,	0x1faa6,	0x1f9cc,	0x1f383
];
// size of emojis array
$N = count($emojisList);
// background colors list - Halloween Theme
$colorsList = [
	0xff8c00,	0x4b0082,	0xa4d65e,	0xa9a9a9,	0x8b4513
];
// size of colors array
$M = count($colorsList);
?>
<table>
<?php

for ($i = 0; $i < $ROWS; $i++) {
	echo "<tr>\n";
	for ($j = 0; $j < $COLS; $j++) {
		$color = str_pad(dechex($colorsList[($i + $j) % $M]), 6, 0, STR_PAD_LEFT);
		echo "<td style='background-color: #$color'>&#{$emojisList[($i + $j) % $N]};</td>\n";
	}
	echo "</tr>\n";
}
?>
</table>
</body>
</html>