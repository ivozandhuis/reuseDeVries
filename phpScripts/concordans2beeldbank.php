<?php
declare(strict_types=1);

require_once __DIR__ . '/vendor/autoload.php';

// first clean the concordance
$converter = new \Leones\Concordance\Converter();
$converter->run();

// then search for links
$linker = new \Leones\Concordance\Linker();
$linker->run();