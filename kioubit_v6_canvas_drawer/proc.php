<?php
$filename = $argv[1];
$pics = json_decode(file_get_contents($filename.'.json'),true);

$mod_x = 20;
$mod_y = 150;
$mod_x = 359;
$mod_y = 407;
$mod_x = 407;
$mod_y = 407;

$dyn_x = 0 + $mod_x;
$dyn_y = 0 + $mod_y;

$output = [];

foreach ($pics as $per_line) {
	//y
	foreach ($per_line as $per_bit) {
		//x
		$dyn_x = $dyn_x + 1;
		if ($per_bit !== false){
			$ip[] = dechex($dyn_x).':'.dechex($dyn_y).':11'.$per_bit;
		}
	}
	$dyn_x = 0 + $mod_x;
	$dyn_y = $dyn_y + 1;
}

$output = $ip;

file_put_contents($filename.'.ips.json',json_encode($output));