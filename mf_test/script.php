<?php
require_once 'stemm_es.php';

array_shift($argv);
$request = array();
foreach ($argv as $arg) {
       array_push($request,stemm_es::stemm($arg));

    }

fwrite(STDOUT, implode(' ',$request));

?>
