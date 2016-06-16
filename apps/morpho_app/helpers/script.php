<?php
$path = getcwd() . '/apps/freeling_app/helpers/stemm_es.php';
require_once($path);
array_shift($argv);
$request = array();
foreach ($argv as $arg) {
       array_push($request,stemm_es::stemm($arg));
    }
fwrite(STDOUT, implode(' ',$request));
?>
