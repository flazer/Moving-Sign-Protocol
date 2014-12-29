#!/usr/bin/env php
<?php

  /*
    This is file is used as a valid callback from gammu-smsd.
    URL for more information have a look there:
    http://de.wammu.eu/docs/manual/smsd/

    You will find an example of a working gammuconfig 
    in "gammu-example"-folder .
  */


  if(!isset($argv[1])) die();

  $name = $argv[1];

  $log = "/var/www/bar/smslog";
  $file = "/var/spool/gammu/inbox/".$name;

  $time = time();
  $text = escapeshellcmd(file_get_contents($file));
  if(!$text) die();

  $meta = explode(".",$name);
  $meta = explode("_",$meta[0]);
  array_pop($meta);
  $number = array_pop($meta);
  unlink($file);

  $data = json_decode(file_get_contents($log));
  if(!is_array($data)) $data = array();
  $data[] = array(
        'time' => $time,
        'number' => $number,
        'text' => $text
  );

  file_put_contents($log, json_encode($data));
  exec('python /path/to/movingSign/led.py "'.$text.'" -c"auto"', $output);
?>
