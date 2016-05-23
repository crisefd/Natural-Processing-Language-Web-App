<?php
require_once '/srv/npl_project/apps/freeling_app/helpers/stemm_es.php';
array_shift($argv);
$request = array();
foreach ($argv as $arg) {
       array_push($request,stemm_es::stemm($arg));
    }
fwrite(STDOUT, implode(' ',$request));
?>
