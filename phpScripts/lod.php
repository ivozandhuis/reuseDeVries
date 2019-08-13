<?php
declare(strict_types=1);

use League\Csv\Reader;
use League\Csv\Statement;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * Create the turtle file from the 'link-locatiepunten-saa-beeldbank.csv' file
 * With triples for the HISGIS location points and the beeldbank Identifiers
 */
$file = __DIR__ . '/../data/addresses/link-locatiepunten-saa-beeldbank.csv';
$fileToWrite = __DIR__ . '/../data/addresses/beeldbank-hisgis.ttl';

$reader = Reader::createFromPath($file, 'r');
$stmt = (new Statement())
    ->offset(1)
    //->limit(50)
;
$records = $stmt->process($reader);

$hisgisURI = 'https://hisgis.nl/resource/atm/lp-%s';
$saaURI = 'http://beeldbank.amsterdam.nl/afbeelding/%s';

if (file_exists($fileToWrite)) {
    unlink($fileToWrite);
}

\EasyRdf\RdfNamespace::set('dct', 'http://purl.org/dc/terms/');

function remove_utf8_bom($text)
{
    $bom = pack('H*', 'EFBBBF');
    $text = preg_replace("/^$bom/", '', $text);
    return $text;
}

$batch = 10000;
$i = 0;
foreach ($records as $row) {
    $i++;
    if ($i === 1) {
        $graph = new \EasyRdf\Graph();
    }

    $record = $graph->resource(sprintf($saaURI, remove_utf8_bom($row[1])));
    $graph->add($record, 'dct:spatial', $graph->resource(sprintf($hisgisURI, $row[0])));

    if ($i === $batch) {
        print 'Flush to file' . PHP_EOL;
        file_put_contents(
            $fileToWrite,
            $graph->serialise('turtle'),
            FILE_APPEND | LOCK_EX
        );
        $i = 0;
        $graph = null;
    }
}
//print $graph->serialise('turtle');
print 'All done' . PHP_EOL;