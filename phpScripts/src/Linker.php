<?php
declare(strict_types=1);

namespace Leones\Concordance;

use League\Csv\Reader;
use League\Csv\Statement;
use League\Csv\Writer;

/**
 * Links the addresses from the beeldbank to HisGis
 */
class Linker
{
    private const SAA_IMAGES_FILE = 'saa-beeldbank-adressen.csv';
    private const HISGIS_FILE = 'adressenconcordans-unique.csv';
    private const FOUND_LINKS_FILE = 'link-locatiepunten-saa-beeldbank.csv';
    private const NOT_FOUND_LINKS_FILE = 'geen-link-locatiepunten-saa-beeldbank.csv';

    public function run(int $limit = 1000000):void
    {
        $concordance = Helper::readCsvToArray(Helper::filePath(self::HISGIS_FILE));

        $reader = Reader::createFromPath(Helper::filePath(self::SAA_IMAGES_FILE), 'r');
        $stmt = (new Statement())
            ->offset(0)
            ->limit($limit)
        ;
        $records = $stmt->process($reader);

        // prepare files to write
        $writerWithLinks = Writer::createFromPath(Helper::filePath(self::FOUND_LINKS_FILE), 'w+');
        $writerWithLinks->insertOne(['lp', 'beeldbankid', 'string']);

        $writerNotFound = Writer::createFromPath(Helper::filePath(self::NOT_FOUND_LINKS_FILE), 'w+');
        $writerNotFound->insertOne(['beeldbankid', 'string']);

        foreach ($records as $row) {
            $addressString = $row[1] . $row[2];

            $locationPointDef = array_column($concordance, 'string');
            $found_key = array_search($addressString, $locationPointDef);
            if ($found_key) {
                print "Found {$addressString}" . PHP_EOL;
                $writerWithLinks->insertOne([$concordance[$found_key]['lp'], $row[0], $addressString]);
            } else {
                $writerNotFound->insertOne([$row[0], $addressString]);
            }
        }

        print count($records) . '  records processed' . PHP_EOL;
    }

}
