<?php
declare(strict_types=1);

namespace Leones\Concordance;

class Helper
{
    public static function readCsvToArray(string $file): array
    {
        $csv = array_map('str_getcsv', file($file));
        array_walk($csv, function (&$a) use ($csv) {
            $a = array_combine($csv[0], $a);
        });

        return $csv;
    }

    public static function filePath(string $file): string
    {
        return __DIR__ . '/../../data/addresses/' . $file;
    }

}
