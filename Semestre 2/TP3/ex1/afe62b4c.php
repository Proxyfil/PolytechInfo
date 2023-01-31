<?php

$before  = '<!DOCTYPE html><html><head><meta charset="UTF-8">';
$before .= '<title>Réception Données</title></head><body>';
$after   = '</body></html>';


echo $before;

echo ('<h1>Source de la demande</h1>');

echo ($_SERVER['HTTP_REFERER']);

echo ('<h1>Méthode détectée</h1>');

if ($_SERVER['REQUEST_METHOD'] =="POST")
	echo ("<p> Réception avec méthode POST </p>");
else
if ($_SERVER['REQUEST_METHOD'] =="GET")
	echo ("<p> Réception avec méthode GET </p>");

echo ('<h1>Données accessibles sur le serveur</h1>');

switch($_SERVER['REQUEST_METHOD'])
{
	case 'GET': var_dump($_GET); break;
	case 'POST': var_dump($_POST); break;
}

echo ('<h1>Données concernant les fichiers reçus </h1>');

var_dump($_FILES);

echo ('<h1>Données serveur </h1>');

$indicesServer = array('PHP_SELF', 
'argv', 
'argc', 
'GATEWAY_INTERFACE', 
'SERVER_ADDR', 
'SERVER_NAME', 
'SERVER_SOFTWARE', 
'SERVER_PROTOCOL', 
'REQUEST_METHOD', 
'REQUEST_TIME', 
'REQUEST_TIME_FLOAT', 
'QUERY_STRING', 
'DOCUMENT_ROOT', 
'HTTP_ACCEPT', 
'HTTP_ACCEPT_CHARSET', 
'HTTP_ACCEPT_ENCODING', 
'HTTP_ACCEPT_LANGUAGE', 
'HTTP_CONNECTION', 
'HTTP_HOST', 
'HTTP_REFERER', 
'HTTP_USER_AGENT', 
'HTTPS', 
'REMOTE_ADDR', 
'REMOTE_HOST', 
'REMOTE_PORT', 
'REMOTE_USER', 
'REDIRECT_REMOTE_USER', 
'SCRIPT_FILENAME', 
'SERVER_ADMIN', 
'SERVER_PORT', 
'SERVER_SIGNATURE', 
'PATH_TRANSLATED', 
'SCRIPT_NAME', 
'REQUEST_URI', 
'PHP_AUTH_DIGEST', 
'PHP_AUTH_USER', 
'PHP_AUTH_PW', 
'AUTH_TYPE', 
'PATH_INFO', 
'ORIG_PATH_INFO') ; 

echo '<table cellpadding="10">' ; 
foreach ($indicesServer as $arg) { 
    if (isset($_SERVER[$arg])) { 
        echo '<tr><td>'.$arg.'</td><td>' . $_SERVER[$arg] . '</td></tr>' ; 
    } 
    else { 
        echo '<tr><td>'.$arg.'</td><td>-</td></tr>' ; 
    } 
} 
echo '</table>' ; 

echo $after;


	
?>